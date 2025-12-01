from scapy.all import PcapReader, IP, TCP, UDP
import pandas as pd
import numpy as np

pcap_file = "Wednesday-workingHours.pcap"  # the file with attacks
output_csv = "test_data.csv"               # the input for our detector

class Flow:
    def __init__(self, src_ip, dst_ip, src_port, dst_port, proto, timestamp):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.proto = proto
        
        self.start_time = timestamp
        self.last_time = timestamp
        
        self.packet_count = 1
        self.byte_count = 0
    
    def update(self, timestamp, size):
        self.packet_count += 1
        self.byte_count += size
        self.last_time = max(self.last_time, timestamp) # ensure time always moves forward

    def get_features(self):
        # 1. calculate duration
        duration = self.last_time - self.start_time
        
        # software engineering fix: prevent divide by zero
        # if duration is 0, assume it took a tiny amount of time (e.g., 1 microsecond)
        if duration == 0:
            duration = 0.000001
            
        # 2. calculate rates
        bytes_per_sec = self.byte_count / duration
        packets_per_sec = self.packet_count / duration
        
        # 3. return a dictionary (this becomes a csv row later)
        return {
            "duration": duration,
            "total_bytes": self.byte_count,
            "total_packets": self.packet_count,
            "bytes_per_sec": bytes_per_sec,
            "packets_per_sec": packets_per_sec,
            "proto": self.proto,
            "src_port": self.src_port,
            "dst_port": self.dst_port
        }

def get_flow_key(packet):
    if packet.haslayer(IP):
        ip = packet[IP]
        src_ip = ip.src
        dst_ip = ip.dst
        proto = ip.proto
        
        src_port = 0
        dst_port = 0
        
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            
        # sorting ips/ports to ensure bidirectional flows are grouped
        ips = sorted([src_ip, dst_ip])
        ports = sorted([src_port, dst_port])
        return (ips[0], ips[1], ports[0], ports[1], proto)
    return None

def main():
    active_flows = {}
    print(f"[*] processing {pcap_file}...")
    
    count = 0
    try:
        with PcapReader(pcap_file) as pcap:
            for packet in pcap:
                if packet.haslayer(IP):
                    key = get_flow_key(packet)
                    timestamp = float(packet.time)
                    length = packet[IP].len
                    
                    if key in active_flows:
                        active_flows[key].update(timestamp, length)
                    else:
                        active_flows[key] = Flow(key[0], key[1], key[2], key[3], key[4], timestamp)
                
                count += 1
                if count % 20000 == 0:
                    print(f"processed {count} packets... active flows: {len(active_flows)}")
                
                # let's process 100,000 packets to get a good dataset size
                if count >= 100000:
                    break
    except Exception as e:
        print(f"error reading pcap: {e}")

    print(f"\n[DONE] generating dataset from {len(active_flows)} flows...")
    
    # --- export to csv ---
    # this is the link between "network" and "ai"
    data = []
    for flow in active_flows.values():
        data.append(flow.get_features())
        
    df = pd.DataFrame(data)
    
    # save to file
    df.to_csv(output_csv, index=False)
    print(f"[SUCCESS] saved training data to {output_csv}")
    print(df.head()) # show the first few rows

if __name__ == "__main__":
    main()