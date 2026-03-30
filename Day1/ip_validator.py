
def validIP(ip):

    parts = ip.split(".")

    if len(parts) != 4:
        print("{parts} : IP address must contain exactly four octets separated by periods (.) ")
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
        return True
    


while True:
    user_i = input("enter an ip address:   ")

    if user_i == "":
        break

    validIP(user_i)
    print()

            


