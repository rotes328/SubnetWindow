def errno(code):
    text = None
    match code:
        case 1:
            text = "Invalid IPv4 Address or Mask"
        case 2:
            text = "Invalid IPv4 Address"
        case 3:
            text = "Invalid Mask"
        case 4:
            text = "Mask cannot be /0."
        case 5:
            text = "Mask cannot be longer than 32 bits."
        case 6:
            text = "IP cannot start with 0"
        case 7:
            text = "Multicast IP; not a subnet."
    return text
