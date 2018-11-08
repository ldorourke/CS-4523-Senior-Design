#!/bin/sh
docker rm seniordesign 2> /dev/null || true 
docker run -it -p 8000:8000 -v "$PWD:/home/SeniorDesign" seniordesign bash