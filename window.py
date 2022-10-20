from tkinter import *
from subnet import *


def clear_output():
    output1.config(text="")
    output2.config(text="")
    output3.config(text="")

def clear_output_params():
    network_output.configure(text="")
    broadcast_output.configure(text="")
    hostrange_output.configure(text="")

def output(values):
    supernet = values[5]
    network_address_out = "{}/{}".format(values[0], values[1])
    hostrange = "{}  -  {}".format(values[3], values[4])
    if supernet is False:
        output1.config(text="Network Address")
        output2.config(text="Broadcast Address")
        output3.config(text="Host Range")
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


def error_status(text):
    status_bar.configure(text=text, bg="red", fg="white", font="Helvetica 12 bold")
    network_output.configure(text="----------")
    broadcast_output.configure(text="----------")
    hostrange_output.configure(text="----------")

def error_message(code):
    if code == 1:
        text = "Invalid IPv4 Address or Mask"
    if code == 2:
        text = "Invalid IPv4 Address"
    elif code == 3:
        text = "Invalid Mask"
    elif code == 4:
        text = "Mask cannot be /0."
    elif code == 5:
        text = "Mask cannot be longer than 32 bits."
    elif code == 6:
        text = "IP cannot start with 0"
    elif code == 7:
        text = "Multicast IP; not a subnet."
    error_status(text)

def calculate_subnet():
    try:
        ip = ip_input.get()
        mask = subnet_input.get()
        mask = check_mask_format(mask)
        # Calculate the values info
        values = subnet_calc(ip, mask)
        if isinstance(values,int):
            error_message(values)
        else:
            clear_output()
            output(values)
            status_bar.configure(text="© Mike Rotella 2022", fg="black", bg="#F0F0F0", font="Helvetica 12")
    except Exception as e:
        error_message(1)


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
network_output = Label(win, text="----------", font=("Courier 10 bold"))
broadcast_output = Label(win, text="----------", font=("Courier 10 bold"))
hostrange_output = Label(win, text="----------", font=("Courier 10 bold"))
status_bar = Label(win, text="© Mike Rotella 2022", fg="black", relief=SUNKEN, bg="#F0F0F0", font="Helvetica 12")

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

# Create buttons
exit = Button(win, text="Exit", command=win.quit)
exit.grid(row=5, column=0, sticky=W+E)
calculate = Button(win, text="Calculate", command=calculate_subnet)
calculate.grid(row=5, column=1, sticky=W+E, pady=4)


def main():
    win.mainloop()


if __name__ == "__main__":
    main()