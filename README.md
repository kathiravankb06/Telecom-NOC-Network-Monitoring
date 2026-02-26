# Telecom NOC Network Monitoring & Backhaul Link Failure Analysis

## 📌 Overview
This project implements a **real-time Telecom Network Operations Center (NOC) monitoring system** that tracks the availability of **Core, Aggregation, and Backhaul** network links.  
It continuously checks link reachability, detects failures, logs outage events with timestamps, and calculates downtime duration for operational and SLA analysis.

The project simulates how telecom operators monitor network health and respond to outages in live environments.

---

## 🎯 Objective
The objective of this project is to:
- Detect network link failures in real time
- Record failure and restoration timestamps
- Calculate downtime duration
- Simulate telecom NOC fault monitoring workflows
- Understand cascading failures across telecom network layers

---

## 🏗️ Telecom Network Architecture (Conceptual)
Core Network
│
Aggregation Layer
│
Backhaul Transport
│
Access Network (Towers / Sites)


Each layer is monitored independently to observe failure propagation and service impact.

---

## ⚙️ Features
- Real-time monitoring of network links  
- Core, Aggregation, and Backhaul visibility  
- UP/DOWN state change detection  
- Timestamp-based event logging  
- Downtime calculation (ongoing & completed outages)  
- Console-based NOC-style output  
- Handles link flapping scenarios  

---

## 🧠 How It Works
1. The monitoring system starts and initializes all network components  
2. Each component is probed at fixed intervals (ICMP/TCP checks)  
3. If a component responds, its status is marked **UP**  
4. If it fails to respond, its status is marked **DOWN**  
5. Only **state changes** (UP → DOWN or DOWN → UP) are logged  
6. Downtime is calculated using failure and restoration timestamps  
7. Logs can be analyzed for outage patterns and SLA impact  

---

## 🖥️ Sample Output
Telecom NOC Monitoring Started
Core changed to UP at 10:00:01
Aggregation changed to UP at 10:00:01
Backhaul changed to UP at 10:00:01

Core changed to DOWN at 10:02:15
Backhaul changed to DOWN at 10:02:15


This indicates a major upstream or shared infrastructure failure affecting multiple layers.

---

## 🛠️ Technologies Used
- Python  
- ICMP Ping / TCP Socket Probing  
- Real-time Logging  
- Windows / Linux Environment  

---

## 🧪 Testing & Simulation
The project can be tested by:
- Disconnecting network connectivity
- Blocking ICMP using firewall rules
- Changing monitored IP addresses
- Running the script on different networks (Wi-Fi / Mobile hotspot)

Note: Some networks block ICMP, which may cause links to appear DOWN even when internet access is available.

---

## ⚠️ Limitations
- Detects reachability issues only (logical monitoring)
- Does not pinpoint physical fault locations
- Does not include SNMP, optical power, or RF telemetry
- No automated ticketing or dashboard visualization

These limitations reflect the difference between a monitoring prototype and enterprise NOC systems.

---

## 🚀 Future Enhancements
- SNMP-based interface and device monitoring  
- Email/SMS alert notifications  
- Web-based real-time dashboard  
- Network topology mapping  
- Alarm correlation for root cause analysis  
- Redundant monitoring nodes  

---

## 🏢 Real-World Applications
- Telecom Network Operations Centers (NOC)  
- ISP network monitoring  
- Backhaul and transport link analysis  
- Data center network monitoring  
- SLA uptime and downtime reporting  

---

## 📚 Key Learnings
- Real-time network monitoring principles  
- Telecom Core, Aggregation, and Backhaul architecture  
- Failure detection and outage tracking  
- Downtime calculation and SLA relevance  
- Cascading failure behavior in networks  

---

## 💼 Job Relevance
This project is directly relevant to roles such as:
- NOC Engineer  
- Network Support Engineer  
- Telecom Operations Engineer  
- Backhaul Support Engineer  
- ISP Monitoring Engineer  

It demonstrates practical understanding of **telecom fault monitoring and operations**, not just programming.

---

## 📄 License
This project is intended for educational and learning purposes.
