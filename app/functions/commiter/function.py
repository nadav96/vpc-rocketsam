# DI:

import json
import os
from subprocess import run, PIPE
import requests
import socket


def create_response(body, code=200):
    return {
        "statusCode": code,
        "body": json.dumps(body)
    }


def handler(event, context):
    hostname = socket.getfqdn()
    ip = socket.gethostbyname(socket.gethostname())


    url = "http://3.220.57.224"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print("internet connection available.")
        return create_response({
            "s": 1,
            "ip": ip
        })
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(exception)
        print("No internet connection.")
        return create_response({
            "s": 0,
            "ip": ip
        })
