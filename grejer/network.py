import socket
import requests

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    