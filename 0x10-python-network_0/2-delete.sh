#!/bin/bash
# Sends DELETE request to URL passed as first argument and display the body of the response
curl -s -X DELETE "${1}"
