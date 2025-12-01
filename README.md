```Markdown
\# // NIDS\_FORENSIC\_TOOL\_V5



!\[Python](https://img.shields.io/badge/PYTHON-3.11-000000?style=for-the-badge\&logo=python\&logoColor=white)

!\[TensorFlow](https://img.shields.io/badge/TENSORFLOW-KERAS-000000?style=for-the-badge\&logo=tensorflow\&logoColor=white)

!\[Streamlit](https://img.shields.io/badge/INTERFACE-STREAMLIT-D71920?style=for-the-badge\&logo=streamlit\&logoColor=white)



```text

SYSTEM\_STATUS:   ONLINE

ARCHITECTURE:    DEEP\_LEARNING\_AUTOENCODER

TARGET:          DOS\_ATTACK\_VECTORS

UI\_THEME:        INDUSTRIAL

````



-----



\## // 01\\\_SYSTEM\\\_OVERVIEW



This project is a \*\*Network Intrusion Detection System (NIDS)\*\* designed to identify anomalies in network traffic using Deep Learning.



Unlike traditional signature-based firewalls, this system utilizes an \*\*Autoencoder Neural Network\*\* to learn the statistical baseline of "Benign" traffic. Any traffic flow that deviates mathematically from this baseline is flagged as a potential threat.



\### \[ CORE\\\_CAPABILITIES ]



> \*\*TRAFFIC ANALYSIS:\*\* Real-time processing of TCP/UDP flows.  

> \*\*ANOMALY DETECTION:\*\* Identifies DoS/DDoS attacks via Reconstruction Error (MSE).  

> \*\*VISUAL FORENSICS:\*\* Log-scale visualization of attack vectors.  

> \*\*REPORTING:\*\* Automated generation of forensic CSV logs.



-----



\## // 02\\\_ARCHITECTURE\\\_PIPELINE



The system follows a strict linear processing pipeline:



```text

\[ SOURCE\_DATA ] (.pcap/.csv)

&nbsp;      |

&nbsp;      v

\[ INGESTION\_LAYER ]

(Scapy: Flow Aggregation \& Feature Extraction)

&nbsp;      |

&nbsp;      v

\[ PREPROCESSING ]

(MinMax Normalization 0.0 -> 1.0)

&nbsp;      |

&nbsp;      v

\[ INFERENCE\_CORE ]

(TensorFlow: Autoencoder Compression)

&nbsp;      |

&nbsp;      v

\[ DECISION\_LOGIC ]

(MSE Calculation > Threshold = ATTACK)

&nbsp;      |

&nbsp;      v

\[ UI\_PRESENTATION ]

(Streamlit: Dashboard \& Alerts)

```



-----



\## // 03\\\_INSTALLATION\\\_PROTOCOL



\### 1\\. CLONE\\\_REPOSITORY



```bash

git clone \[https://github.com/KiarashAkbari/NIDS-Forensic-Tool.git](https://github.com/KiarashAkbari/NIDS-Forensic-Tool.git)

cd NIDS-Forensic-Tool

```



\### 2\\. INITIALIZE\\\_ENVIRONMENT



```bash

\# Recommended: Python 3.11

pip install -r requirements.txt

```



\### 3\\. EXECUTE\\\_SYSTEM



```bash

streamlit run app.py

```



-----



\## // 04\\\_FILE\\\_STRUCTURE



```text

/ROOT

├── app.py                   # \[ENTRY\_POINT] Main Dashboard Logic

├── requirements.txt         # Dependency Manifest

├── nids\_autoencoder.keras   # Trained Neural Network (The Brain)

├── scaler.save              # Normalization Logic (The Filter)

│

├── src/                     # \[SOURCE\_CODE]

│   ├── flow\_builder.py      # Network Parser

│   ├── train\_model.py       # Training Script

│   └── detect.py            # CLI Verification

│

└── README.md                # System Documentation

```



-----



\## // 05\\\_PERFORMANCE\\\_METRICS



\*\*DATASET:\*\* CIC-IDS2017 (Canadian Institute for Cybersecurity)



| METRIC | VALUE |

| :--- | :--- |

| \*\*TRAINING\\\_DATA\*\* | Monday (Benign Traffic Only) |

| \*\*TEST\\\_DATA\*\* | Wednesday (DoS / Heartbleed) |

| \*\*NORMAL\\\_MSE\*\* | \\~0.002 (Low Error) |

| \*\*ATTACK\\\_MSE\*\* | \\~100.0+ (Critical Error) |

| \*\*DETECTION\\\_RATE\*\* | \\~99.8% on DoS Vectors |



-----



\## // 06\\\_ENGINEER\\\_INFO



```text

DEVELOPER: KIARASH AKBARI

COURSE: COMPUTER NETWORKS \& SOFTWARE ENGINEERING

GITHUB: https://github.com/KiarashAkbari```



-----



\*For educational and forensic research purposes only.\*



```


