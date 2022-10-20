from random import randint as rand


def random_values():
    ip = [rand(1, 223)]
    for octet in range(3):
        octet = rand(1, 254)
        ip.append(octet)
    ip_address = "{}.{}.{}.{}".format(ip[0], ip[1], ip[2], ip[3])

    if ip[0] > 128:
        bitmask = rand(8, 32)
    elif ip[0] > 192:
        bitmask = rand(16, 32)
    else:
        bitmask = rand(24, 32)

    return ip_address, str(bitmask)
