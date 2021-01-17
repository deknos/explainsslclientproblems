package main

import (
    "fmt"
    "net/http"
    "crypto/tls"
)

func main() {
    http.DefaultTransport.(*http.Transport).TLSClientConfig = &tls.Config{InsecureSkipVerify: true}
    fmt.Println("Testing for https://wrong.host.badssl.com")
    _, err := http.Get("https://wrong.host.badssl.com")
    if err != nil {
        fmt.Println(err)
    }
}
