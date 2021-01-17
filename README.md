# explainsslclientproblems

With https://badssl.com i want to provide some samples, what can go wrong if SSL/Certificate Handling is disabled. 
Currently this is done in Python, but since Python uses OpenSSL for managing SSL Connections we may make use of Go which has a separate SSL implementation and may show some more exact information if the SSL-Management or Certificate Validation fails.

## Comments

* The problem is, that Python usually uses OpenSSL for Certificates. And this may be kind of sparse with information what the current problem is.
* At least with python i want to evaluate, WHICH failures modes we wanna play for, and perhaps look at Go, if that provides more information

## TODO

* more error modes to test for:
 * self signed certificates, good and bad
 * pinned certificates, good and badssl
 * https://dh480.badssl.com/
 * https://untrusted-root.badssl.com/
 * https://incomplete-chain.badssl.com/
* write a documentation block in each file for explaining what to learn
* clean up variable/function names
