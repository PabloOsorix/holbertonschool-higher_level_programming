#!/bin/bash
# Bash script that displays the sizze of the body of the response

curl -sI "$1" | grep Content-Length: | cut -d " " -f 2
