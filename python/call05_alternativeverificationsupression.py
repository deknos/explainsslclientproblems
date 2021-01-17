#!/usr/bin/python3

import requests
from urllib3.exceptions import InsecureRequestWarning

# site: https://revoked.badssl.com
# state should be: bad, revoked certificate
# verification: disabled
# comment: suppress warning about disabled verification via package configuration

badssl_startsite = "https://revoked.badssl.com"
https_verification = False

def verification_on():
    if https_verification:
        print("Verification is enabled")
    else:
        print("Verification is disabled")

def test_disabled_verification_with_warning():
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    # alternative: requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    try:
        print("Starting a request to " + badssl_startsite)
        requests.post(badssl_startsite, verify = https_verification)
    except Exception as e:
        print("There was an error requesting " + badssl_startsite)
        print("Error:"+e)
        return
    print("Request returned successfully")

if __name__ == "__main__":
    verification_on()
    test_disabled_verification_with_warning()

