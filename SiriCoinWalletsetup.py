import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from web3 import Web3
import json
import os

root = tk.Tk()
root.title("SiriCoin Desktop Wallet Setup")
root.iconbitmap('icon.ico')
root.option_add("*tearOff", False) # This is always a good idea
root.geometry("590x590")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.resizable(False,False)# Create a style
style = ttk.Style(root)
w3 = Web3(Web3.HTTPProvider("https://siricoin-node-1.dynamic-dns.net:5005/web3"))

# Import the tcl file
root.tk.call("source", "proxttk-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("proxttk-dark")

def onclick():
    try:
        bal = w3.eth.getBalance(entry1.get())
        data = open("data.txt", "w")
        data.write(entry1.get())
        messagebox.showinfo("SiriCoin Wallet Setup", "Done Saving data file you may run SiriCoinWalletmain now.")
        root.quit()
    except:
        messagebox.showerror("SiriCoin Wallet Setup Error", "Please enter a valid SiriCoin Address")   

d = tk.IntVar(value=2)
# Label
label1 = ttk.Label(root, text="SiriCoin Wallet OneTime Setup",font="Times 16" ,justify="center",foreground="#E255CC")
label1.pack()
label2 = ttk.Label(root, text="v1.0.0 By SiriDevs", font="Times 10", foreground="cyan")
label2.pack(pady=5)
# Entry
entry1 = ttk.Entry(root)
entry1.insert(0, "Enter Your SiriCoin address")
entry1.place(x=150, y=200, width=300)
button1 = ttk.Button(root, text="Finish Setup",style="AccentButton", width=20, command=onclick)
button1.place(x=200, y=350)
root.mainloop()