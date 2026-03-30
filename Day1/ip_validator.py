while(True):
    def validIP(ip):

        parts = ip.split(".")

        if len(parts) != 4:
            print("IP address must contain exactly four octets separated by periods (.) ")
            return False
        
        for i in parts:
            if not i.isdigit():
                print("IP address must consist only of digits (no letters or special characters).")
                return False
            
            num = int(i)

            if num < 0 or num > 255:
                print("IP address must be a number between 0 and 255 (inclusive).")
                return False
        
        else:
            print("IP Address is correct!!!")
            return True
        


    user_i = input("enter an ip address:   ")
    validIP(user_i)

            


