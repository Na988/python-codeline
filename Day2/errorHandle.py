
def numToInt(x):
    try:
        num = int(x)
        print("true")

    except ValueError:

        print("Enter a valid number")
        return None

    else:
        print("\nProccess is successful")
        return num

for i in range(2):
    user_i = input("enter a number:  ")
    numToInt(user_i)
