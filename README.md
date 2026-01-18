# Unicorn-Vision
Welcome to Unicorn Vision! A vision system that can stream a robot POV to a website, deployable on Raspberry Pis!

<img width="500" height="500" alt="Pink Fluffy Unicorns Logo" src="https://github.com/user-attachments/assets/ac02c1a1-983c-4ac1-a59a-60bd9b3d0015" />

## About
### What is Unicorn Vision?
Unicorn Vision is a side project started by The Pink Fluffy Unicorns [83] to explore how to integrate vision into MiniFRC through Raspberry Pis. The program can currently stream video from the RPI to a dedicated website for viewing the feed.

### What boards does it support?
Currently, Unicorn Vision is known to support the Raspberry Pi 5 and Camera Module 2 with possible future testing revealing support for the Raspberry Pi Zero 2 WH.

### Why was Unicorn Vision made?
Unicorn Vision was created mainly to solve the problem of depth perception of the driver as well as providing an open avenue for us and other teams to expand on vision systems such as object detection, april tag detection, and small AI model usage.

## Setup
1. Get a Raspberry Pi ([RPI 5](https://www.raspberrypi.com/products/raspberry-pi-5/) or [RPI Zero 2 WH](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) are recommended)
2. Install RPI OS on the SD card and setup the PI
3. Go to `Terminal` and ensure all packages are updated through `sudo apt update`
4. Check the IP Address of the Pi through entering `ifconfig` in the terminal and looking at the address beside `INET`
5. Click on the Raspberry Pi icon, go to programming, then click on `Geany`
6. Copy and paste the `main.py` file onto the IDE and save the file (*WARNING: Ensure the file has the .py extension*)
7. Click the `Run` button to start up the vision system
8. On your computer browser, enter in `http://<PI-IP-ADDRESS-HERE>:8080/video_feed`
