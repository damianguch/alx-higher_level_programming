#!/bin/bash
# Send a POST request with a custom header to trigger the desired response
curl -s -X POST -H "X-Payload: You got me!" http://0.0.0.0:5000/catch_me
