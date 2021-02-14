#!/usr/bin/python3

import sys
import os
import requests
from requests import Request, Session


badssl_startsite = "https://self-signed.badssl.com"
https_verification = True
cert_file = "/tmp/selfsigned4.crt"

# other potential solutions: https://stackoverflow.com/a/58246407 or
# https://www.electricmonk.nl/log/2018/06/02/ssl-tls-client-certificate-verification-with-python-v3-4-sslcontext/

#def get_certificate(host, port, cert_file_pathname):
#    with requests.get("https://" + host, verify = False) as response:
#        der = response.raw.connection.sock.getpeercert(binary_form=True)
#    with open(cert_file_pathname, "w") as f:
#        f.write(der)

#def get_certificate(host, port, cert_file_pathname):
#     import ssl
#     with open(cert_file_pathname, "wb") as f:
#         cert = ssl.get_server_certificate((host, port))
#         f.write(ssl.PEM_cert_to_DER_cert(cert))

#def get_certificate(host, port, cert_file_pathname):
#    import OpenSSL
#    import ssl
#    cert = ssl.get_server_certificate((host, port))
#    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
#    der = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_ASN1, x509)
#    with open(cert_file_pathname, 'wb') as f: 
#        f.write(der)

def get_certificate(host,port, cert_file_pathname):
    import get_cert
    cert = get_cert.get_certificate("https://" + host)
    with open(cert_file_pathname, "w") as f:
        f.write(cert)


def test_good_call(certfile):
    try:
        print("Starting a request to " + badssl_startsite)
        os.environ["REQUESTS_CA_BUNDLE"]=certfile
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
    get_certificate("self-signed.badssl.com", 443, cert_file)
    test_good_call(cert_file)

