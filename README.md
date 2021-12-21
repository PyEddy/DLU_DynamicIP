# DLU_DynamicIP
This python script scans eth0 and grabs the IP then adds that IP to "external_ip" in the required config files in the DarkflameServer

This is built mainly for WSL2 users

# Dependancies

    Python 3.8
    netifaces
    
# How to use

Place the main.py file in DarkflameServer/build where your config files are located
 #### It should look like this
      authconfig.ini
      chatconfig.ini
      masterconfig.ini
      main.py
      
 #### How to run the script
      Run this in the WSL2 terminal (make sure you are in your build directory)
      
      python3 main.py
