#!/bin/bash
# script that takes in a URL, nds a POST request and email/subject header variables
curl -sX POST "$1" -H "email: test@gmail.com" -H "subject: I will always be here for PLD"
