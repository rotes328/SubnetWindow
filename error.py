# Mike Rotella 2022

def error(code):
    # Used to flag errors
    if code == 1:
        print("Invalid IPv4 address or mask.")
    elif code == 2:
        print("Invalid IPv4 address.")
    elif code == 3:
        print("Invalid mask.")
    elif code == 4:
        print("Mask cannot be /0.")
    elif code == 5:
        print("Mask cannot be longer than 32 bits.")
    elif code == 6:
        print("IP cannot start with 0.")
    elif code == 7:
        print("Multicast IP; not a subnet.")
    quit(-1)
