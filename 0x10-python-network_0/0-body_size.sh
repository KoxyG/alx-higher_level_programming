#!/bin/bash
# This is a script that takes in and send a request to that URL to display the size of the body response

curl -s "$1" | wc -c
