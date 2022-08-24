# Subnet Calculator

by Mike Rotella, 2022
___

My goal with this was to create a Python script that uses no libraries to calculate IPv4
network addresses, broadcast addresses, and network ranges.

The script takes a valid IPv4 IP as input and a valid mask in either dotted decimal notation
or slash notation with or without the slash and returns the network address, broadcast address,
and host range.

If the mask length is less than 8, the script calculates the supernet block.
___
Examples:

Bitmask:

>Enter the IP address: 192.168.1.50
>
>Enter the mask: 255.255.255.0
>
>The network address is: 192.168.1.0/24.
>
>The broadcast address is 192.168.1.255.
>
>The host range is 192.168.1.1 - 192.168.1.254
___
Mask length:

>Enter the IP address: 172.16.4.99
>
>Enter the mask: 27
>
>The network address is: 172.16.4.96/27.
>
>The broadcast address is 172.16.4.127.
>
>The host range is 172.16.4.97 - 172.16.4.126
___
CIDR Notation:

>Enter the IP address: 10.200.128.0
>
>Enter the mask: /10
>
>The network address is: 10.192.0.0/10.
>
>The broadcast address is 10.255.255.255.
>
>The host range is 10.192.0.1 - 10.255.255.254
___
Supernet:

>Enter the IP address: 172.0.0.0
>
>Enter the mask: /7
>
>The CIDR range is 172.0.0.1 - 173.255.255.254
