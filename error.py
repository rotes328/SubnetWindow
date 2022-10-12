# Mike Rotella 2022

def error(code):
    # Used to flag errors
    if code == 1:
        errorcode = "Invalid IPv4 address or mask."
    elif code == 2:
        errorcode = "Invalid IPv4 address."
    elif code == 3:
        errorcode = "Invalid mask."
    elif code == 4:
        errorcode = "Mask cannot be /0."
    elif code == 5:
        errorcode = "Mask cannot be longer than 32 bits."
    elif code == 6:
        errorcode = "IP cannot start with 0."
    elif code == 7:
        errorcode = "Multicast IP; not a subnet."
    return errorcode
