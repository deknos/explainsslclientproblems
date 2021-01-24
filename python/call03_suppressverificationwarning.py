#!/usr/bin/python3

import warnings
import contextlib

import requests
from urllib3.exceptions import InsecureRequestWarning

# site: https://badssl.com
# state should be: good
# verification: disabled
# comment: suppress warning about disabled verification via changing context and adapter

badssl_startsite = "https://badssl.com"
https_verification = False
old_merge_environment_settings = requests.Session.merge_environment_settings

def verification_on():
    if https_verification:
        print("Verification is enabled")
    else:
        print("Verification is disabled")

@contextlib.contextmanager
def no_ssl_verification():
    opened_adapters = set()

    def merge_environment_settings(self, url, proxies, stream, verify, cert):
        # Verification happens only once per connection so we need to close
        # all the opened adapters once we're done. Otherwise, the effects of
        # verify=False persist beyond the end of this context manager.
        opened_adapters.add(self.get_adapter(url))

        settings = old_merge_environment_settings(self, url, proxies, stream, verify, cert)
        settings['verify'] = False

        return settings

    requests.Session.merge_environment_settings = merge_environment_settings

    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', InsecureRequestWarning)
            yield
    finally:
        requests.Session.merge_environment_settings = old_merge_environment_settings

        for adapter in opened_adapters:
            try:
                adapter.close()
            except:
                pass

def test_suppressed_verification_warning():
    with no_ssl_verification():
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
    test_suppressed_verification_warning()

