package main

import (
    "fmt"
    "net/http"
    "crypto/tls"
)

func main() {
    tr := &http.Transport{
        TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    }
    client := &http.Client{Transport: tr}
    _, err := client.Get("https://golang.org/")
    if err != nil {
        fmt.Println(err)
    }
}
