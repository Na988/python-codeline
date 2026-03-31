
def validIP(ip):
    parts = ip.split(".")

    for i in parts:
        if not i.isdigit():
            print(f"\nWrong!!  {ip} : IP address must consist only of digits (no letters or special characters).\n")
            return False
        
        num = int(i)
        if num < 0 or num > 255:
            print(f"\nWrong!!  {ip} : IP address must be a number between 0 and 255 (inclusive).\n")
            return False
        
    if len(parts) != 4:
        print(f"\nWrong!!  {ip} : IP address must contain exactly four octets separated by periods (.)\n")
        return False
    
    else:
        print(f"\n{ip} : IP Address is correct!!!\n")
        print()
        print()
        return True
    


def subnetcalculator(ip, cidr):
    print()
    print()
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


def validCIDR(x):
    if int(x) < 24 or int(x) > 32:
        return False
    
    if not x.isdigit(): 
        return False
    
    else: return True
    



print()
print("----------------------------------")
#get input from user
user_ip = input("enter an ip address:  ")
while not validIP(user_ip):
    print("----------------------------------")
    user_ip = input("enter a new ip address:  ")

#get cidr
print("----------------------------------")
user_Cidr = input ("enter CIDR:  ")
while not validCIDR(user_Cidr):
    print("----------------------------------")
    user_Cidr = input ("enter new CIDR:  ")

#call subnetcalcultor
subnetcalculator(user_ip, user_Cidr)
print("----------------------------------")

            