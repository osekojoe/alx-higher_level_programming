#!/bin/bash
# Make request to 0.0.0.0:5000/catch_me, get response - 'You got me!'
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H  "Origin:School"
