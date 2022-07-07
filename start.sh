#!/bin/sh
docker build -t chess:0.1 -t chess:latest ./chess
docker run -d -p 8164:8164 chess:latest