@echo off
echo There are 
findstr /C:"Received = 0" results.txt | find /c /v ""
echo active ip addresses on your local network
