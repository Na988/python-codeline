
def validIP(ip):

    parts = ip.split(".")

    if len(parts) != 4:
        print("/n/n{parts} : IP address must contain exactly four octets separated by periods (.) ")
        return False
    
    for i in parts:
        if not i.isdigit():
            print("{parts} : IP address must consist only of digits (no letters or special characters).")
            return False
        
        num = int(i)

        if num < 0 or num > 255:
            print("{parts} : IP address must be a number between 0 and 255 (inclusive).")
            return False
    
    else:
        print(f"{parts} : IP Address is correct!!!")
        print()
        print()
        return True
    


def subnetcalculator(ip, cidr):
    last_octet = int(ip.split(".")[-1])
    rest_octet = ip.rsplit(".", 1)[0]
    print("--- Subnet Calculator ---")

    #network address
    block_size = 2  **(32 - int(cidr)) 
    network = (last_octet // block_size) * block_size
    print(f"Network Address: {rest_octet}.{network}")

    #broascast address
    broadcast = (network + block_size) - 1
    print(f"Broadcast Address: {rest_octet}.{broadcast}")

    #usable ips
    usable = (2 ** (32 - int(cidr))) - 2
    print(f"Number of Usable Hosts: {usable}")
    print()
    print()










#grt input from user
user_ip = input("enter an ip address:  ")
user_Cidr = input ("enter CIDR:  ")

#call valid ip to validate the ip address
validIP(user_ip)

#call subnetcalcultor
subnetcalculator(user_ip, user_Cidr)
print()

            