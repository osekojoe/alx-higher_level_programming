#!/bin/bash
# cURL a JSON file - send JSON POST request to URL,displays body of response.
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
