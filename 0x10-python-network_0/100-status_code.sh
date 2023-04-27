#!/usr/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -I -s "$1" | awk '/^HTTP/{print $2}'
