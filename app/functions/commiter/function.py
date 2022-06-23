# DI:

import json
import os
from subprocess import run, PIPE
import requests
import time
import socket


def create_response(body, code=200):
    return {
        "statusCode": code,
        "body": json.dumps(body)
    }


def handler(event, context):
    hostname = socket.getfqdn()
    ip = socket.gethostbyname(socket.gethostname())

    try:
        with open("/mnt/efs/{}.txt".format(int(time.time())), "w") as fw:
            fw.write("hello world")
    except Exception as e:
        print("EEEE {}".format(e))
        return create_response({
            "e": "323"
        })


    url = "http://3.220.57.224"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print("internet connection available.")
        return create_response({
            "s": 1,
            "ip": ip,
            "dir": os.listdir("/mnt/efs")
        })
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(exception)
        print("No internet connection.")
        return create_response({
            "s": 0,
            "ip": ip
        })
