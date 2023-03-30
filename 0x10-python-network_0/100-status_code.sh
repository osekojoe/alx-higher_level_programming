#!/bin/bash
# Send request to URL passed as an arg, displays only the status code response
curl -s -w "%{http_code}" "$1" -o /dev/null
