#!/usr/bin/python3

import socket
import requests
import sys
import ssl
import OpenSSL

from pyasn1_modules import pem, rfc2459
from pyasn1.codec.der import decoder

# comment: downloads certificate
# you also can test the certificate with "openssl x509 -noout -text -in selfsigned.crt"

badssl_site = "self-signed.badssl.com"
cert_file_name = "selfsigned.crt"
https_verification = True
print_certificate_on_stdout = True

def verification_on():
    if https_verification:
        print("Verification is enabled")
    else:
        print("Verification is disabled")

def download_certificate():
    certificate = ssl.get_server_certificate((badssl_site, 443))
    with open(cert_file_name, "w") as f:
        f.write(certificate)
    if print_certificate_on_stdout:
        substrate = pem.readPemFromFile(open(cert_file_name))
        cert = decoder.decode(substrate, asn1Spec=rfc2459.Certificate())[0]
        print(cert.prettyPrint())

if __name__ == "__main__":
    verification_on()
    download_certificate()

