"""
IX-ZeroCool Packet Sniffer

Monitors inbound and outbound traffic to detect anomalies,
protocol abuse, or suspicious data behavior in the AI mesh.
"""

import socket
import struct

class PacketSniffer:
    def __init__(self, interface="eth0"):
        self.interface = interface
        self.sock = None

    def initialize_socket(self):
        self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        self.sock.bind((self.interface, 0))
        print(f"[+] Listening on {self.interface}...")

    def start_sniffing(self, packet_limit=10):
        count = 0
        while count < packet_limit:
            raw_data, addr = self.sock.recvfrom(65535)
            eth_proto, data = self._unpack_ethernet_frame(raw_data)
            if eth_proto == 8:  # IPv4
                print(f"[>] IPv4 Packet from {addr}")
                count += 1

    def _unpack_ethernet_frame(self, data):
        dest_mac, src_mac, proto = struct.unpack('!6s6sH', data[:14])
        return socket.htons(proto), data[14:]

# Example usage
if __name__ == "__main__":
    sniffer = PacketSniffer(interface="lo")  # Loopback for safe local testing
    sniffer.initialize_socket()
    sniffer.start_sniffing(packet_limit=5)
