#!/bin/bash
# Get the byte size of the HTTP response header
curl -s "$1" | wc -c
