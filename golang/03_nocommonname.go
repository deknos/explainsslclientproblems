package main

import (
    "fmt"
    "net/http"
    "crypto/tls"
)

func main() {
    http.DefaultTransport.(*http.Transport).TLSClientConfig = &tls.Config{InsecureSkipVerify: true}
    fmt.Println("Testing for https://no-common-name.badssl.com")
    _, err := http.Get("https://no-common-name.badssl.com")
    if err != nil {
        fmt.Println(err)
    }
}
