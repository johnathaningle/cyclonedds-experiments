import socket
import struct

MCAST_GRP = "224.0.0.1"  # Multicast group
MCAST_PORT = 5007        # Port number

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Allow multiple programs to use the same socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the multicast port
sock.bind(("", MCAST_PORT))

# Join the multicast group
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print(f"Listening on multicast group {MCAST_GRP}:{MCAST_PORT}")
while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received: {data.decode()} from {addr}")
