import socket
import netifaces as ni


def getIP():
    ni.ifaddresses('eth0')
    IP = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
    return IP


def readAuth(ip_address):
    with open("authconfig.ini", "r") as f:
        lines = f.readlines()
        external_ip = lines[7]
        print("Successfully updated Auth")
    with open("authconfig.ini", "w") as f:
        lines[7] = "external_ip=" + ip_address + "\n"
        f.writelines(lines)


def readChat(ip_address):
    with open("chatconfig.ini", "r") as f:
        lines = f.readlines()
        external_ip = lines[7]
        print("Successfully updated Chat")
    with open("chatconfig.ini", "w") as f:
        lines[7] = "external_ip=" + ip_address + "\n"
        f.writelines(lines)


def readMaster(ip_address):
    with open("masterconfig.ini", "r") as f:
        lines = f.readlines()
        external_ip = lines[7]
        print("Successfully updated Master")
    with open("masterconfig.ini", "w") as f:
        lines[7] = "external_ip=" + ip_address + "\n"
        f.writelines(lines)


external_ip = getIP()
readAuth(external_ip)
readChat(external_ip)
readMaster(external_ip)

print("Add this to your config in your client")
print(external_ip)
