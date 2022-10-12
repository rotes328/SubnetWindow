from tkinter import *
from subnet import *
from functools import partial

def calculate_subnet():
    # line1 = label1
    # line2 = label2
    # line3 = label3
    # print(line1)
    try:
        ip = ip_input.get()
        mask = subnet_input.get()

        mask = check_mask_format(mask)
        # Calculate the values info
        # subnet_calc(ip, str(mask))
        values = subnet_calc(ip, mask)
        if values is True:
            network_output.configure(text="Error")
            broadcast_output.configure(text="Error")
            hostrange_output.configure(text="Error")
            # messagebox.showerror("Python Error", "Error!")
        else:
            network_address_out = "{}/{}".format(values[0],values[1])
            hostrange = "{}  -  {}".format(values[3], values[4])
            supernet = values[5]
            output1.config(text="")
            output2.config(text="")
            output3.config(text="")
            if supernet is False:
                output1.config(text="Network Address")
                output2.config(text="Broadcast Address")
                output3.config(text="Host Range")
                # Label(win, text="Network Address").grid(row=2)
                # Label(win, text="Broadcast Address").grid(row=3)
                # Label(win, text="Host Range").grid(row=4)
                network_output.configure(text="")
                broadcast_output.configure(text="")
                hostrange_output.configure(text="")
                network_output.configure(text=network_address_out)
                broadcast_output.configure(text=values[2])
                hostrange_output.configure(text=hostrange)
                # print(f"The network address is: {values[0]}/{values[1]}.")
                # print(f"The broadcast address is {values[2]}.")
                # print(f"The host range is {values[3]} - {values[4]}")
            else:
                output1.config(text="CIDR Range")
                # output2.config(text="")
                # output3.config(text="")
                # Label(win, text="CIDR Range").grid(row=2)
                # Label(win, text="").grid(row=3)
                # Label(win, text="").grid(row=4)
                network_output.configure(text="")
                broadcast_output.configure(text="")
                hostrange_output.configure(text="")
                network_output.configure(text=hostrange)
                # broadcast_output.configure(text=values[2])
                # hostrange_output.configure(text=hostrange)
                # print(f"The CIDR range is {values[3]} - {values[4]}")
    except Exception as e:
        network_output.configure(text="Error")
        broadcast_output.configure(text="Error")
        hostrange_output.configure(text="Error")


win = Tk()
win.title("Subnet Calculator")
# win.geometry("400x300")
ip_label = Label(win, text='IP Address')
mask_label = Label(win, text='Mask')
output1 = Label(win, text="Network Address")
output2 = Label(win, text="Broadcast Address")
output3 = Label(win, text="Host Range")
ip_label.grid(row=0)
mask_label.grid(row=1)
output1.grid(row=2)
output2.grid(row=3)
output3.grid(row=4)
# Label(win, text="").grid(row=5)

ip_input = Entry(win)
subnet_input = Entry(win)
network_output = Label(win, text="", font=("Courier 12 bold"))
broadcast_output = Label(win, text="", font=("Courier 12 bold"))
network_output_mask = Label(win, text="", font=("Courier 12 bold"))
hostrange_output = Label(win, text="", font=("Courier 12 bold"))

ip_input.grid(row=0, column=1)
subnet_input.grid(row=1, column=1)
network_output.grid(row=2, column=1)
broadcast_output.grid(row=3, column=1)
hostrange_output.grid(row=4, column=1)


Button(win, text='Exit', command=win.quit).grid(row=5, column=0, sticky=W, pady=4)
Button(win, text='Calculate', command=calculate_subnet).grid(row=5, column=1, sticky=W, pady=4)

mainloop()
