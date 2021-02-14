#!/usr/bin/python3

import os
import requests
from requests import Request, Session

# site: https://self-signed.badssl.com
# state should be: good, selfsigned certificate provided
# verification: enabled

badssl_startsite = "https://self-signed.badssl.com"
https_verification = True

def test_good_call():
    try:
        print("Starting a request to " + badssl_startsite)
        os.environ["REQUESTS_CA_BUNDLE"]="selfsigned2.crt"
        s = Session()
        req = Request('GET', badssl_startsite)
        prepped = s.prepare_request(req)
        settings = s.merge_environment_settings(prepped.url, {}, None, None, None)
        resp = s.send(prepped, **settings)
    except Exception as e:
        print("There was an error requesting " + badssl_startsite)
        print("Error:"+str(e))
        return
    print("Request returned successfully")

if __name__ == "__main__":
    test_good_call()

