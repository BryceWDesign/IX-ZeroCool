"""
IX-ZeroCool Firewall Adapter

Interfaces with the local firewall or routing system to dynamically
adjust access rules based on detected threats or anomalies.
"""

import subprocess
from typing import List

class FirewallAdapter:
    def __init__(self):
        self.rules_applied: List[str] = []

    def block_ip(self, ip: str):
        rule = f"iptables -A INPUT -s {ip} -j DROP"
        self._apply_rule(rule)
        self.rules_applied.append(rule)
        print(f"[+] Blocked IP: {ip}")

    def allow_ip(self, ip: str):
        rule = f"iptables -A INPUT -s {ip} -j ACCEPT"
        self._apply_rule(rule)
        self.rules_applied.append(rule)
        print(f"[+] Allowed IP: {ip}")

    def flush_rules(self):
        flush_cmd = "iptables -F"
        subprocess.call(flush_cmd.split())
        self.rules_applied.clear()
        print("[*] Flushed all firewall rules.")

    def _apply_rule(self, rule: str):
        try:
            subprocess.call(rule.split())
        except Exception as e:
            print(f"[!] Failed to apply rule: {rule}")
            print(f"    Error: {e}")

# Example usage
if __name__ == "__main__":
    fw = FirewallAdapter()
    fw.block_ip("192.168.1.100")
    fw.allow_ip("192.168.1.200")
    fw.flush_rules()
