````markdown
# // NIDS_FORENSIC_TOOL_V5

![Python](https://img.shields.io/badge/PYTHON-3.11-000000?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TENSORFLOW-KERAS-000000?style=for-the-badge&logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/INTERFACE-STREAMLIT-D71920?style=for-the-badge&logo=streamlit&logoColor=white)


SYSTEM_STATUS:   ONLINE
ARCHITECTURE:    DEEP_LEARNING_AUTOENCODER
TARGET:          DOS_ATTACK_VECTORS
UI_THEME:        INDUSTRIAL
````

-----

## // 01\_SYSTEM\_OVERVIEW

This project is a **Network Intrusion Detection System (NIDS)** designed to identify anomalies in network traffic using Deep Learning.

Unlike traditional signature-based firewalls, this system utilizes an **Autoencoder Neural Network** to learn the statistical baseline of "Benign" traffic. Any traffic flow that deviates mathematically from this baseline is flagged as a potential threat.

### [ CORE\_CAPABILITIES ]

> **TRAFFIC ANALYSIS:** Real-time processing of TCP/UDP flows.  
> **ANOMALY DETECTION:** Identifies DoS/DDoS attacks via Reconstruction Error (MSE).  
> **VISUAL FORENSICS:** Log-scale visualization of attack vectors.  
> **REPORTING:** Automated generation of forensic CSV logs.

-----

## // 02\_ARCHITECTURE\_PIPELINE

The system follows a strict linear processing pipeline:

```
[ SOURCE_DATA ] (.pcap/.csv)
       |
       v
[ INGESTION_LAYER ]
(Scapy: Flow Aggregation & Feature Extraction)
       |
       v
[ PREPROCESSING ]
(MinMax Normalization 0.0 -> 1.0)
       |
       v
[ INFERENCE_CORE ]
(TensorFlow: Autoencoder Compression)
       |
       v
[ DECISION_LOGIC ]
(MSE Calculation > Threshold = ATTACK)
       |
       v
[ UI_PRESENTATION ]
(Streamlit: Dashboard & Alerts)
```

-----

## // 03\_INSTALLATION\_PROTOCOL

### 1\. CLONE\_REPOSITORY

```bash
git clone [https://github.com/YOUR_USERNAME/NIDS-Forensic-Tool.git](https://github.com/YOUR_USERNAME/NIDS-Forensic-Tool.git)
cd NIDS-Forensic-Tool
```

### 2\. INITIALIZE\_ENVIRONMENT

```bash
# Recommended: Python 3.11
pip install -r requirements.txt
```

### 3\. EXECUTE\_SYSTEM

```bash
streamlit run app.py
```

-----

## // 04\_FILE\_STRUCTURE

```text
/ROOT
├── app.py                   # [ENTRY_POINT] Main Dashboard Logic
├── requirements.txt         # Dependency Manifest
├── nids_autoencoder.keras   # Trained Neural Network (The Brain)
├── scaler.save              # Normalization Logic (The Filter)
│
├── src/                     # [SOURCE_CODE]
│   ├── flow_builder.py      # Network Parser
│   ├── train_model.py       # Training Script
│   └── detect.py            # CLI Verification
│
└── README.md                # System Documentation
```

-----

## // 05\_PERFORMANCE\_METRICS

**DATASET:** CIC-IDS2017 (Canadian Institute for Cybersecurity)

| METRIC | VALUE |
| :--- | :--- |
| **TRAINING\_DATA** | Monday (Benign Traffic Only) |
| **TEST\_DATA** | Wednesday (DoS / Heartbleed) |
| **NORMAL\_MSE** | \~0.002 (Low Error) |
| **ATTACK\_MSE** | \~100.0+ (Critical Error) |
| **DETECTION\_RATE** | \~99.8% on DoS Vectors |

-----

## // 06\_ENGINEER\_INFO

```text
DEVELOPER: KIARASH AKBARI
COURSE: COMPUTER NETWORKS & SOFTWARE ENGINEERING
GITHUB: https://github.com/KiarashAkbari
```

-----

*For educational and forensic research purposes only.*

```


