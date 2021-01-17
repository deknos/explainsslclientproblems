#!/usr/bin/python3

import requests

# site: https://badssl.com
# state should be: good
# verification: disabled
# comment: warning on command line output on disabled verification

badssl_startsite = "https://badssl.com"
https_verification = False

def verification_on():
    if https_verification:
        print("Verification is enabled")
    else:
        print("Verification is disabled")

def test_disabled_verification_with_warning():
    try:
        print("Starting a request to " + badssl_startsite)
        requests.get(badssl_startsite, verify = https_verification)
        # This should output something like the following message:
        # InsecureRequestWarning: Unverified HTTPS request is being made to host 'badssl.com'. 
        # Adding certificate verification is strongly advised. 
        # See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    except Exception as e:
        print("There was an error requesting " + badssl_startsite)
        print("Error:"+e)
        return
    print("Request returned successfully")

if __name__ == "__main__":
    verification_on()
    test_disabled_verification_with_warning()

