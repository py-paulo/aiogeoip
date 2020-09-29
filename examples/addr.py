import socket

DOMAINs = [
    'www.google.com',
    'www.facebook.com',
    'www.github.com',
    'www.youtube.com'
]

IPs = [socket.gethostbyname(domain) for domain in DOMAINs]
