#!/usr/bin/python3

import socket
import requests
import sys
import ssl
import OpenSSL

# site: https://wrong.host.badssl.com
# state should be: bad, certificate does not match certificate
# verification: enabled
# comment: gives exception chain on call

badssl_site = "https://wrong.host.badssl.com"
https_verification = True

# chained exceptions code copied from stack overflow:
# http://jaredrobinson.com/blog/iterating-the-python3-exception-chain/

def chained_exceptions(exc_info=None):
    """
    Adapted from: https://github.com/getsentry/raven-python/pull/811/files?diff=unified

    Return a generator iterator over an exception's chain.

    The exceptions are yielded from outermost to innermost (i.e. last to
    first when viewing a stack trace).
    """
    if not exc_info or exc_info is True:
        exc_info = sys.exc_info()

    if not exc_info:
        raise ValueError("No exception found")

    yield exc_info
    exc_type, exc, exc_traceback = exc_info

    while True:
        if exc.__suppress_context__:
            # Then __cause__ should be used instead.
            exc = exc.__cause__
        else:
            exc = exc.__context__
        if exc is None:
            break
        yield type(exc), exc, exc.__traceback__

def chained_exception_types(e=None):
    """
    Return a generator iterator of exception types in the exception chain

    The exceptions are yielded from outermost to innermost (i.e. last to
    first when viewing a stack trace).

    Adapted from: https://github.com/getsentry/raven-python/pull/811/files?diff=unified
    """
    if not e or e is True:
        e = sys.exc_info()[1]

    if not e:
        raise ValueError("No exception found")

    yield type(e)

    while True:
        if e.__suppress_context__:
            # Then __cause__ should be used instead.
            e = e.__cause__
        else:
            e = e.__context__
        if e is None:
            break
        yield type(e)

def verification_on():
    if https_verification:
        print("Verification is enabled")
    else:
        print("Verification is disabled")


def test_exception_chain():
    saved_exception = None
    try:
        resp = requests.get(badssl_site, verify = https_verification)
    except Exception as e:
        saved_exception = e
    if saved_exception:
        print("Iterating exception chain for a saved exception...")
        for t, ex, tb in chained_exceptions((type(saved_exception), saved_exception, saved_exception.__traceback__)):
            print("\ttype:", t, "Exception:", ex)

if __name__ == "__main__":
    verification_on()
    test_exception_chain()

