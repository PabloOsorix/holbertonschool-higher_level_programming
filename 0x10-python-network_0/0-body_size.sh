#!/bin/bash
# Bash script that displays the sizze of the body of the response

curl -s $1 | wc -c
