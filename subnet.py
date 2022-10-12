# Subnet/Supernet Address Calculator
# by Mike Rotella, 2022

from binary import *


def subnet_calc(ip, mask):
    """
    :param ip: Dotted decimal format IP
    :param mask: Dotted decimal format mask
    :return: List with network address, mask length, broadcast address, first host IP,
        and last host IP as strings.
    """
    # Split the IP as a string into a list of strings and do basic error checking
    ip = DottedDecimalString(ip).convert_ip_to_dotted_decimal_list()
    if isinstance(ip, int):
        return ip
    # Split the mask as a string into a list of strings and do basic error checking
    mask = DottedDecimalString(mask).convert_mask_to_dotted_decimal_list()
    if isinstance(mask, int):
        return mask
    # Convert the mask list into binary and put it in a list
    binary_mask = DottedDecimalList(mask)
    binary_mask = binary_mask.convert_validated_mask_to_binary_list()
    if isinstance(binary_mask, int):
        return binary_mask
    # Calculate the length of the bitmask and store in a string to return
    cidr = calculate_mask_length(binary_mask)
    # Set supernet flag if applicable
    supernet = False
    if int(cidr) < 8:
        supernet = True
    # Calculate the network address and store it in a list to convert later
    subnet = []
    for (ipbits, maskbits) in zip(ip, mask):
        # Do a logical AND on the integer values of the IP and mask lists
        number = int(ipbits) & int(maskbits)
        subnet.append(str(number))
    # Convert the network address to binary and store in a list for later calculation
    binary_subnet = DottedDecimalList(subnet).convert_dotted_decimal_list_to_binary_list()
    # Calculate broadcast info from network and mask binary lists
    broadcast_list = calculate_broadcast(binary_subnet,binary_mask)
    # Format the network address to dotted decimal and store in a string
    subnet_string = DottedDecimalList(subnet).convert_to_dotted_decimal()
    # Store the broadcast address in a string
    broadcast = broadcast_list[1]
    # Calculate first and last host IPs based on the network and broadcast as binary lists
    range = calculate_host_range(binary_subnet,broadcast_list[0], cidr)
    first_host_ip = range[0]
    last_host_ip = range[1]
    return [subnet_string, cidr, broadcast, first_host_ip, last_host_ip, supernet]


def calculate_host_range(subnet, broadcast, cidr):
    """
    :param subnet: Network address as a binary list
    :param broadcast: Broadcast address as 32-bit binary in string
    :param cidr: Bitmask length
    :return: List of first host IP and last host IP
    """
    # Convert binary list to 32-bit binary string
    network_long = BinaryList(subnet).convert_to_long_binary()
    # Catch /31 and /32 special cases
    if int(cidr) > 30:
        first_host = str(bin(int(network_long, 2)))
        last_host = str(bin(int(broadcast, 2)))
    # First host IP is network address + 1
    # Last host IP is broadcast address - 1
    else:
        first_host = str(bin(int(network_long, 2) + 1))
        last_host = str(bin(int(broadcast, 2) - 1))
    # Convert long binary to dotted binary
    first_host_dotted_binary = BinaryString(first_host).convert_to_dotted_binary()
    last_host_dotted_binary = BinaryString(last_host).convert_to_dotted_binary()
    # Convert dotted binary to dotted-decimal strings
    first_host_ip = DottedBinaryList(first_host_dotted_binary).convert_dotted_binary_to_dotted_decimal()
    last_host_ip = DottedBinaryList(last_host_dotted_binary).convert_dotted_binary_to_dotted_decimal()
    return [first_host_ip, last_host_ip]


def calculate_mask_length(mask):
    """
    :param mask: Mask as binary list
    :return: Slash notation bitmask length
    """
    cidr = mask.count("1")
    return cidr


def calculate_broadcast_binary(network, mask):
    """
    :param network: Network address as binary list
    :param mask: Mask as binary list
    :return: Broadcast address in binary as string
    """
    # Calculate host bits from mask
    host_bits = mask.count("0")
    # Calculate network size
    host_bits_squared = 2 ** host_bits - 1
    network_long = BinaryList(network).convert_to_long_binary()
    # Broadcast address is network address + maximum number of hosts
    broadcast_address = int(network_long, 2) + host_bits_squared
    return str(bin(broadcast_address))


def calculate_broadcast(subnet, mask):
    """
    :param subnet: Network address as binary list
    :param mask: Subnet mask as binary list
    :return:
    """
    # Calculate the broadcast address as a binary string
    binary_broadcast = calculate_broadcast_binary(subnet, mask)
    # Convert the string to dotted binary list
    dotted_binary = BinaryString(binary_broadcast).convert_to_dotted_binary()
    # dotted_binary = convert_to_dotted_binary(binary_broadcast)
    # Convert to dotted decimal
    broadcast = DottedBinaryList(dotted_binary).convert_dotted_binary_to_dotted_decimal()
    return [binary_broadcast, broadcast]


def check_mask_format(mask):
    """
    :param mask: Mask input
    :return: Mask as dotted decimal if not already in that format
    """
    if len(mask) < 4:
        # Accepts / notation and bit-length
        mask = mask.replace("/", "")
        mask = BitmaskString(mask).convert_bitmask_to_dotted_decimal()
    return mask

