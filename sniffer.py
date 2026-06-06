from scapy.all import sniff, IP, TCP, UDP, Raw

def process(pkt):
    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst

        if TCP in pkt:
            proto = "TCP"
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport
        elif UDP in pkt:
            proto = "UDP"
            sport = pkt[UDP].sport
            dport = pkt[UDP].dport
        else:
            return

        # label common ports
        labels = {80: "HTTP", 443: "HTTPS", 22: "SSH", 53: "DNS", 21: "FTP"}
        label = labels.get(dport, labels.get(sport, ""))

        print(f"[{proto}] {src}:{sport} → {dst}:{dport}  {label}")

        if Raw in pkt:
            payload = pkt[Raw].load[:60]
            print(f"  payload: {payload}")

print("[*] Sniffing... Ctrl+C to stop")
sniff(filter="tcp or udp", prn=process, store=False)