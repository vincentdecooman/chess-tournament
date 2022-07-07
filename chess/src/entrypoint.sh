#!/bin/bash
socat TCP-LISTEN:8164,reuseaddr,fork EXEC:"./chess-challenge.py"
