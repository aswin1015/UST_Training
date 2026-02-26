#!/usr/bin/env bash

WATCH_DIR="/var"    
DEST_DIR="/tmp"     
THRESHOLD=90        

USAGE=$(df -P "$WATCH_DIR" | awk 'NR==2  {print $5}' | sed 's/%//')

if (( USAGE < THRESHOLD )); then
  echo "Disk usage is ${USAGE}%. Below threshold. No action taken."
  exit 0
fi

