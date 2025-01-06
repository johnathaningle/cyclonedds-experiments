import socket
from time import sleep

MCAST_GRP = "224.0.0.1"  # Multicast group
MCAST_PORT = 5007        # Port number

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Set TTL (Time to Live) for multicast packets
ttl = 1  # Local network
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Send multicast messages
while True:
    message = "Hello, Multicast!".encode()
    sock.sendto(message, (MCAST_GRP, MCAST_PORT))
    print(f"Message sent to {MCAST_GRP}:{MCAST_PORT}")
    #sleep for 1 second
    sleep(1)

# Close the socket
