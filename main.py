import netifaces as ni


def getIP():
    """Grabs the IP from the eth0 interface"""
    try:
        ni.ifaddresses('eth0')
        IP = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        return IP
    except:
        print("Error: Couldn't find eth0 interface")
        print("Make sure to read the README.md before using this tool")
        exit()


def readAuth(ip_address):
    """Reads authconfig and writes the grabbed ip to external_ip"""
    with open("authconfig.ini", "r") as f:
        lines = f.readlines()
        external_ip = lines[7]
        print("Successfully updated Auth")
    with open("authconfig.ini", "w") as f:
        lines[7] = "external_ip=" + ip_address + "\n"
        f.writelines(lines)
        f.close()


def readChat(ip_address):
    """Reads chatconfig and writes the grabbed ip to external_ip"""
    with open("chatconfig.ini", "r") as f:
        lines = f.readlines()
        external_ip = lines[7]
        print("Successfully updated Chat")
    with open("chatconfig.ini", "w") as f:
        lines[7] = "external_ip=" + ip_address + "\n"
        f.writelines(lines)
        f.close()


def readMaster(ip_address):
    """Reads masterconfig and writes the grabbed ip to external_ip"""
    with open("masterconfig.ini", "r") as f:
        lines = f.readlines()
        external_ip = lines[7]
        print("Successfully updated Master")
    with open("masterconfig.ini", "w") as f:
        lines[7] = "external_ip=" + ip_address + "\n"
        f.writelines(lines)
        f.close()


external_ip = getIP()
readAuth(external_ip)
readChat(external_ip)
readMaster(external_ip)

print("Add this to your config in your client")
print(external_ip)
