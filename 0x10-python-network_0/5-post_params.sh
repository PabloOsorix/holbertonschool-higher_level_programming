#!/bin/bash
# script that takes in a URL, nds a POST request and email/subject header variables
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
