#!/bin/bash
# cURL POST params - send POST request to URL, displays response body.
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -sX POST "$1"
