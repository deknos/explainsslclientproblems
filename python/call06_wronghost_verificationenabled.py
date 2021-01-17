#!/usr/bin/python3

import requests

# site: https://badssl.com
# state should be: bad, certificate does not match host
# verification: enabled
# comment: should give SSLError

badssl_startsite = "https://wrong.host.badssl.com"
https_verification = True

def verification_on():
    if https_verification:
        print("Verification is enabled")
    else:
        print("Verification is disabled")

def test_good_call():
    try:
        print("Starting a request to " + badssl_startsite)
        requests.get(badssl_startsite, verify = https_verification)
    except Exception as e:
        print("There was an error requesting " + badssl_startsite)
        print("Error:"+str(e))
        return
    print("Request returned successfully")

if __name__ == "__main__":
    verification_on()
    test_good_call()

