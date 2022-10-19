from tkinter import *
from subnet import *


def check_input(input1, input2):
    # If input is invalid length, return error code
    if len(input1) > 15:
        return 2
    elif len(input2) > 15:
        return 3
    elif len(input1) == 0 and len(input2) == 0:
        return 0
    else:
        return None


def clear_output():
    output1.config(text="")
    output2.config(text="")
    output3.config(text="")


def clear_output_params():
    network_output.configure(text="")
    broadcast_output.configure(text="")
    hostrange_output.configure(text="")


def paint_normal_status():
    status_bar.configure(text="© Mike Rotella 2022", fg="black", bg="#F0F0F0", font="Helvetica 14")


def paint_normal_window():
    output1.config(text="Network Address")
    output2.config(text="Broadcast Address")
    output3.config(text="Host Range")


def output(values):
    supernet = values[5]
    if supernet is None:
        output1.config(text="Bitmask")
        clear_output_params()
        network_output.configure(text="")
        broadcast_output.configure(text="")
        hostrange_output.configure(text="")
        network_output.configure(text=values[0])
        return
    network_address_out = "{}/{}".format(values[0], values[1])
    hostrange = "{}  -  {}".format(values[3], values[4])
    if supernet is False:
        paint_normal_window()
        clear_output_params()
        network_output.configure(text=network_address_out)
        broadcast_output.configure(text=values[2])
        hostrange_output.configure(text=hostrange)
    else:
        output1.config(text="CIDR Range")
        clear_output_params()
        network_output.configure(text="")
        broadcast_output.configure(text="")
        hostrange_output.configure(text="")
        network_output.configure(text=hostrange)


def paint_blank_status():
    network_output.configure(text="----------")
    broadcast_output.configure(text="----------")
    hostrange_output.configure(text="----------")


def error_status(text):
    paint_normal_window()
    status_bar.configure(text=text, bg="red", fg="white", font="Helvetica 14 bold")
    paint_blank_status()


def errno(code):
    text=None
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
    error_status(text)


def calculate_subnet():
    paint_normal_window()
    paint_blank_status()
    ip = ip_input.get()
    mask = subnet_input.get()
    check = check_input(ip, mask)
    if check == 0:
        return
    elif isinstance(check, int):
        errno(check)
        return
    if len(mask) < 4:
        mask = check_mask_format(mask)
        if isinstance(mask, int):
            errno(mask)
    # Calculate the bitmask if no IP
        if not ip:
            mask_check = mask_calc(mask)
            if mask_check is True:      # Mask is valid
                values = [mask]
                for x in range(1,6): values.insert(x,None)
                clear_output()
                output(values)
            else:                       # Mask is invalid
                return errno(mask_check)
            paint_normal_status()
            return
    # Calculate the values info
    values = subnet_calc(ip, mask)
    if isinstance(values,int):
        errno(values)
        return
    clear_output()
    output(values)
    paint_normal_status()


def run_app():
    calculate_subnet()


# Create Window
win = Tk()
win.title("Subnet Calculator")
win.geometry("320x180")
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

# Create labels
ip_label = Label(win, text="IP Address")
mask_label = Label(win, text="Mask")
output1 = Label(win, text="Network Address")
output2 = Label(win, text="Broadcast Address")
output3 = Label(win, text="Host Range")
network_output = Label(win, text="----------", font="Courier 12 bold")
broadcast_output = Label(win, text="----------", font="Courier 12 bold")
hostrange_output = Label(win, text="----------", font="Courier 12 bold")
status_bar = Label(win, text="© Mike Rotella 2022", fg="black", relief=SUNKEN, bg="#F0F0F0", font="Helvetica 14")

# Create input fields
ip_input = Entry(win)
subnet_input = Entry(win)

# Organize grid
ip_label.grid(row=0)
mask_label.grid(row=1)
output1.grid(row=2)
output2.grid(row=3)
output3.grid(row=4)
status_bar.grid(row=6, column=0, columnspan=2, sticky = W+E)
ip_input.grid(row=0, column=1)
subnet_input.grid(row=1, column=1)
network_output.grid(row=2, column=1)
broadcast_output.grid(row=3, column=1)
hostrange_output.grid(row=4, column=1)

# Bind return to run the app
win.bind('<Return>', lambda e: run_app())

# Create buttons
exit_button = Button(win, text="Exit", command=win.quit)
exit_button.grid(row=5, column=0, sticky=W+E)
calculate = Button(win, text="Calculate", command=calculate_subnet)
calculate.grid(row=5, column=1, sticky=W+E, pady=4)


if __name__ == "__main__":
    win.mainloop()
