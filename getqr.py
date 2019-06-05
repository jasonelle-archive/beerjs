#!/usr/bin/env python3

"""
    Before running this script
    1 - Start a python server with `$ python3 -m http.server`
    2 - Start ngrok server with `$ ngrok http 8000`
    3 - Install QR Code Image Generator https://fukuchi.org/works/qrencode/
"""

import json
import sys
import os
from urllib.request import urlopen

def main():

    # Obtain the information from ngrok server
    with urlopen("http://localhost:4040/api/tunnels") as raw:
        data = json.load(raw)

        qr = None
        for tunnel in data["tunnels"]:
            url = tunnel["public_url"]
            if url.startswith("https"):
                qr = url

    if qr:
        output = "endpoint-base.png"
        directory = "qrcodes"

        print(f"Generated QR for URL {qr}")

        os.system(f"mkdir {directory}")
        os.system(f"qrencode -o {directory}/{output} {qr}")

        apps = [
            "beerjs.json",
            "qr.json"
        ]
        
        for app in apps:
            output = f"{app}.png"
            command = f"{directory}/{output} {qr}/apps/{app}"
            
            print(f"Generated QR for URL {command}")
            
            os.system(f"qrencode -o {command}")
            os.system(f"open {directory}/{output}")


        # Open other files
        os.system("open pwapp.png")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

