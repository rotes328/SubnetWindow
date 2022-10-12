# Mike Rotella 2022
from tkinter import messagebox
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

class DottedDecimalString:
    def __init__(self, dotted_decimal_string):
        """
        :param dotted_decimal_string: Dotted decimal as string
                                      (e.g. "172.16.200.210")
        """
        self.dotted_decimal_string = dotted_decimal_string

    def __str__(self):
        return str(self.dotted_decimal_string)

    def convert_ip_to_dotted_decimal_list(self):
        """
        :return: Valid IP as dotted decimal list
        """
        octets = self.dotted_decimal_string.split(".")
        # Error if list doesn't have 4 elements
        if len(octets) != 4:
            mistake = True
            return mistake
        # try:
        octetList = []
        for octet in octets:
        # Error if IPv4 invalid or not number
            if int(octet) not in range(0, 256):
                mistake = True
                return mistake
            else:
                octetList.append(octet)
        if int(octetList[0]) == 0:
                mistake = True
                return mistake
                # error_text = error(6)
                # messagebox.showerror("Python Error", error_text)
        elif int(octetList[0]) > 256:
                mistake = True
                return mistake
                # error_text = error(2)
                # messagebox.showerror("Python Error", error_text)
        elif int(octetList[0]) > 223:
                mistake = True
                return mistake
                # error_text = error(7)
                # messagebox.showerror("Python Error", error_text)
        # except ValueError:
            # error_text = error(2)
            # messagebox.showerror("Python Error", error_text)
        return octetList

    def convert_mask_to_dotted_decimal_list(self):
        """
        :return: Dotted decimal mask as list (e.g. ['255', '255', '0', '0']
        """
        octets = self.dotted_decimal_string.split(".")
        # Error without 4 elements
        if len(octets) != 4:
            mistake = True
            return mistake
            # error_text = error(3)
            # messagebox.showerror("Python Error", error_text)
        else:
            return octets


class BinaryList:
    def __init__(self, binary_list):
        """
        :param binary_list: A list of individual 1s and 0s in string format
        """
        self.binary_list = binary_list
        self.length = len(binary_list)

    def __str__(self):
        return str(self.binary_list)

    def pad(self, length):
        """
        Prepend binary list with leading 0s to fill a byte, nibble, etc.
        :param length: Length to make the return value
        :return: Padded binary list with 0s before the most significant bit
        """
        for i in range(len(self.binary_list), length):
            self.binary_list.insert(0, "0")
        return self.binary_list

    def reverse_pad(self, length):
        """
        Pad 0s to the end of a binary list up to the length to convert slash
        notation to dotted decimal
        :param length: Desired length (32 for IPv4)
        :return: Padded binary list with 0s after the least significant bit
        """
        for i in range(len(self.binary_list), length):
            self.binary_list.append("0")
        return self.binary_list

    def convert_list_to_dotted_binary(self):
        """
        :return: List of 4 lists, one per byte
        """
        dotted_binary = [self.binary_list[i * 8:(i + 1) * 8]
                         for i in range((len(self.binary_list) + 8 - 1) // 8)]
        return dotted_binary

    def convert_to_long_binary(self):
        """
        :return: Binary as string (e.g. "0b101011...")
        """
        binary = "".join(self.binary_list)
        binary = "0b{0}".format(binary)
        return binary


class DottedDecimalList:
    def __init__(self, dotted_decimal_list):
        """
        :param dotted_decimal_list: List of values in dotted decimal
                                    (e.g. ['172', '16', '10', '200']
        """
        self.dotted_decimal_list = dotted_decimal_list

    def __str__(self):
        return str(self.dotted_decimal_list)

    def convert_dotted_decimal_list_to_binary_list(self):
        """
        :return: Binary list padded with leading 0s
        """
        byte_list = []
        byte_list = ByteList(byte_list)
        for byte in self.dotted_decimal_list:
            clean_byte = BinaryString(str(bin(int(byte)))).remove_0b()
            clean_byte_padded = BinaryString(clean_byte).pad(8)
            byte_list.push(str(clean_byte_padded))
        # except ValueError:
            # error_text = error(1)
            # messagebox.showerror("Python Error", error_text)
        # Replace "0b"
        byte_list = byte_list.remove_0b()
        binary_str = ByteList(byte_list).convert_to_long_binary()
        binary_str = binary_str.remove_0b()
        # Convert to string
        binary_list_fixed = BinaryString(binary_str).convert_to_binary_list()
        # Convert to list to return
        # binary_list_fixed = list(binary_list_fixed)
        return binary_list_fixed

    def push(self, string):
        self.dotted_decimal_list.append(string)
        pass

    def convert_validated_mask_to_binary_list(self):
        """
        :return: Valid mask as binary list, if not valid an error will return
        """
        binary = []
        byte_list = ByteList(binary)
        for byte in self.dotted_decimal_list:
            # Convert to binary and append to binary list
            # Store in iterable list
            byte = BinaryString((bin(int(byte))))
            byte_clean = BinaryString(byte).remove_0b()
            byte_padded = BinaryString(byte_clean).pad(8)
            byte_list.push(str(byte_padded))
        # except ValueError:
            # error_text = error(3)
            # messagebox.showerror("Python Error", error_text)
        # Convert to binary string
        binary_str = str(byte_list.convert_to_long_binary().remove_0b())
        # No /0 mask
        if binary_str[0] == "0":
            mistake = True
            return mistake
        # Must be less than 32 bits
        if len(binary_str) > 32:
            mistake = True
            return mistake
        # Check is mask is valid (no 1s after a 0)
        for i in range(1, len(binary_str)):
            if binary_str[i] > binary_str[i - 1]:
                mistake = True
                return mistake
        # Convert to binary list to iterate
        binary_list_fixed_as_string = str(binary_str)
        binary_list_fixed = convert_to_list(binary_list_fixed_as_string)
        return binary_list_fixed

    def convert_to_dotted_decimal(self):
        """
        :return: Dotted decimal as string (e.g. "172.16.200.192")
        """
        DottedDecimalString = ".".join(self.dotted_decimal_list)
        return DottedDecimalString

class ByteList:
    def __init__(self, byte_list):
        """
        :param byte_list: List of byte in binary
        (e.g. ['0b11000000', '0b10101000', '0b1', '0b0'])
        """
        self.byte_list = byte_list

    def __str__(self):
        return str(self.byte_list)

    def push(self, binary_string):
        """
        :param binary_string: Binary string
        :return: Push to the end of the list
        """
        self.byte_list.append(binary_string)
        pass

    def convert_to_long_binary(self):
        """
        :return: Binary as string (e.g. "0b101011...")
        """
        # try:
        long_binary = "".join(self.byte_list)
        long_binary = "0b{0}".format(long_binary)
        long_binary = BinaryString(long_binary)
        return long_binary
        # except TypeError:
            # error_text = error(1)
            # messagebox.showerror("Python Error", error_text)
        # except UnboundLocalError:
            # error_text = error(1)
            # messagebox.showerror("Python Error", error_text)

    def remove_0b(self):
        """
        :return: Byte list without "0b"
        """
        for i in range(4):
            octet = self.byte_list[i]
            self.byte_list[i] = octet.replace("0b", "")
        return self.byte_list
        # except IndexError:
            # error_text = error(1)
            # messagebox.showerror("Python Error", error_text)


class DottedBinaryList:
    def __init__(self, dotted_binary):
        """
        :param dotted_binary: Dotted binary list
        (e.g. [['1', '1', '0', '0', '0', '0', '0', '0'], ['1', '0'...]...]
        """
        self.dotted_binary = dotted_binary

    def __str__(self):
        return str(self.dotted_binary)

    def convert_dotted_binary_to_dotted_decimal(self):
        """
        :return: Dotted decimal string (e.g. "10.20.14.200")
        """
        string_bytes = []
        dotted_decimal_list = []
        # Create list of 4 elements in binary
        for byte in self.dotted_binary:
            byte_str = "".join(byte)
            byte_str = byte_str.format("0b{0}")
            string_bytes.append(byte_str)
        # Convert binary to decimal
        for byte in string_bytes:
            decimal = str(int(byte, 2))
            dotted_decimal_list.append(decimal)
        # Add dots between bytes
        dotted_decimal = ".".join(dotted_decimal_list)
        dotted_decimal = str(DottedDecimalString(dotted_decimal))
        return dotted_decimal

class BitmaskString:
    def __init__(self, bitmask):
        """
        :param BitmaskString: String representing a mask between 1 and 32
        """
        self.bitmask = bitmask

    def __str__(self):
        return str(self.bitmask)

    def convert_bitmask_to_dotted_decimal(self):
        """
        :return: Mask as dotted decimal in string format
        """
        binary_mask = []
        for i in range(int(self.bitmask)):
            binary_mask.append("1")
        # except ValueError:
            # error_text = error(3)
            # messagebox.showerror("Python Error", error_text)
        binary_mask = BinaryList(binary_mask)
        binary_mask = binary_mask.reverse_pad(32)
        dotted_binary = BinaryList(binary_mask).convert_list_to_dotted_binary()
        dotted_decimal = DottedBinaryList(dotted_binary).convert_dotted_binary_to_dotted_decimal()
        return dotted_decimal


class BinaryString:
    def __init__(self, binary_string):
        """
        :param binary_string: String representing binary number
        """
        self.binary_string = binary_string

    def __str__(self):
        return str(self.binary_string)

    def remove_0b(self):
        """
        :return: Binary string without "0b"
        """
        self.binary_string = str(self.binary_string).replace("0b","")
        return self.binary_string

    def convert_to_binary_list(self):
        """
        :return: Binary list
        """
        list = []
        list[:0] = self.binary_string
        return list

    def pad(self, length):
        """
        Prepend binary string with leading 0s to fill a byte, nibble, etc.
        :param length: Length to make the return value
        :return: Padded binary string with 0s before most significant bit
        """
        for i in range(len(self.binary_string), length):
            self.binary_string = "0{0}".format(str(self.binary_string))
        return self.binary_string

    def convert_to_dotted_binary(self):
        """
        :return: List of 4 binary lists (dotted binary), one per byte
        """
        binary = self.binary_string.replace("0b","")
        list = []
        list[:0] = binary
        list = BinaryList(list).pad(32)
        dotted_binary = BinaryList(list).convert_list_to_dotted_binary()
        return dotted_binary


def convert_to_list(string):
    """
    :param string: String
    :return: List of each element
    """
    list=[]
    list[:0]=string
    return list
