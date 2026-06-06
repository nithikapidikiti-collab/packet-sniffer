# Packet Sniffer

A live network packet capture and analysis tool built with Python and Scapy. Captures real TCP and UDP traffic, decodes protocol layers, and displays payloads in real time.

## How to run

Requires admin/root privileges to access raw sockets.

```
# Mac/Linux
sudo python3 sniffer.py

# Windows (run VS Code as Administrator)
python3 sniffer.py
```

## Demo

```
[TCP] 192.168.0.203:49573 → 140.82.112.21:443  HTTPS
[TCP] 192.168.0.203:63329 → 44.194.254.103:443  HTTPS
[UDP] 192.168.0.181:5353 → 224.0.0.251:5353
  payload: b'::REQUEST-ADT-IOT-DEVICE-INFO:;'
```

Captured live traffic including HTTPS connections to GitHub, multicast DNS device discovery, and IoT device broadcasts on the local network.

## Concepts demonstrated

- Raw socket capture with Scapy
- TCP and UDP packet decoding
- Network layer analysis (IP, TCP, UDP)
- Common port identification (HTTP, HTTPS, SSH, DNS, FTP)
- Payload inspection and display

## What I'd add next

- Save captures to .pcap files (openable in Wireshark)
- Filter by IP address or port
- DNS query decoder
- Real-time traffic graph

## Ethical use

Only run on networks you own or have permission to monitor.
```

Save, then push:

```
git add .
git commit -m "docs: add README"
git push origin main
```