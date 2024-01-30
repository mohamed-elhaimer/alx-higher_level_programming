#!/bin/bash
#request the server to respond with a message containing You got me!
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"
