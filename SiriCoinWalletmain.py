import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from tkinter.ttk import *
from time import sleep
import os
import re
import requests
from web3 import Web3


root = tk.Tk()
root.title("SiriCoin Desktop Wallet")
root.iconbitmap('icon.ico')
root.option_add("*tearOff", False) # This is always a good idea
root.geometry("1000x590")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.resizable(False,False)# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "proxttk-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("proxttk-dark")
label2 = ttk.Label(root, text="Loading SiriCoin Wallet..", font="Times 10")

def refreshbal():
    bal = w3.eth.getBalance(optdata)
    label4 = ttk.Label(root, text=f"Your SiriCoin Balance: {bal}", font="Times 14", foreground="Cyan")
    label4.place(x=400, y=150)

def slidebar():
    import time
    progress_bar=Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
    progress_bar.place(x=300, y=200, width=400)
    progress_bar['value']=10
    label2.place(x=450, y=240)
    root.update_idletasks()
    time.sleep(1)
    progress_bar['value']=20
    root.update_idletasks()
    time.sleep(1)
    progress_bar['value']=30
    root.update_idletasks()
    time.sleep(1)
    progress_bar['value']=40
    root.update_idletasks()
    time.sleep(1)
    progress_bar['value']=50
    root.update_idletasks()
    time.sleep(1)
    progress_bar['value']=60
    root.update_idletasks()
    time.sleep(1)
    progress_bar['value']=70
    root.update_idletasks()
    time.sleep(1)
    progress_bar['value']=80
    root.update_idletasks()
    time.sleep(1)
    progress_bar['value']=90
    root.update_idletasks()
    time.sleep(1)
    progress_bar['value']=100
    label2.destroy()
    progress_bar.destroy()
    button1.destroy()
    if os.path.exists("data.txt"):
        file = open("data.txt")
        data = file.readline()
        global optdata
        optdata = str(data)
        label4 = ttk.Label(root, text="-----------------------------------------------------------------Additional Wallet Information-------------------------------------------------------------------------", font="Times 14")
        label4.place(x=0, y=250)
        label5 = ttk.Label(root, text="Mainnet Info", font="Times 15")
        label5.place(x=0, y=300)
        try:
            global w3
            w3 = Web3(Web3.HTTPProvider("https://siricoin-node-1.dynamic-dns.net:5005/web3"))
            label6 = ttk.Label(root, text="SiriCoin Mainnet:", font="Times 10", foreground="white")
            label6.place(x=0, y=350)
            label7 = ttk.Label(root, text="Connected", font="Times 10", foreground="green")
            label7.place(x=110, y=350)
        except requests.exceptions.ConnectionError:
            label8 = ttk.Label(root, text="SiriCoin Mainnet:", font="Times 10", foreground="white")
            label8.place(x=0, y=350)
            label9 = ttk.Label(root, text="Error Connecting", font="Times 10", foreground="red")
            label9.place(x=110, y=350)
        label3 = ttk.Label(root, text=f"Your SiriCoin Address: {data}", font="Times 14", foreground="#E255CC")
        label3.place(x=200, y=100)
        button2 = ttk.Button(root, text="Refresh Balance", style="AccentButton", command=refreshbal)
        button2.place(x=450, y=200)
        refreshbal()
        label10 = ttk.Label(root, text="Mainnet Version: v1.2.2", font="Times 10", foreground="white")
        label10.place(x=0, y=400)
        label11 = ttk.Label(root, text="Wallet Version: v1.0.0", font="Times 10", foreground="white")
        label11.place(x=0, y=450)
        label12 = ttk.Label(root, text="Released on: 2-03-2022", font="Times 10", foreground="white")
        label12.place(x=0, y=500)
        label13 = ttk.Label(root, text="SiriCoin Community Links", font="Times 15", foreground="white")
        label13.place(x=500, y=300)
        label14 = ttk.Label(root, text="SiriCoin Website: siricoin.tech", font="Times 10", foreground="white")
        label14.place(x=350, y=350)
        label15 = ttk.Label(root, text="SiriCoin Docs: docs.siricoin.tech", font="Times 10", foreground="white")
        label15.place(x=350, y=400)
        label16 = ttk.Label(root, text="SiriCoin Discord: discord.gg/FcczUFeuAx", font="Times 10", foreground="white")
        label16.place(x=350, y=450)
        label17 = ttk.Label(root, text="SiriCoin Telegram: t.me/SiriCoinCommunity", font="Times 10", foreground="white")
        label17.place(x=350, y=500)
        label18 = ttk.Label(root, text="SiriCoin Instagram: instagram.com/_siricoin/", font="Times 10", foreground="white")
        label18.place(x=650, y=350)
        label19 = ttk.Label(root, text="SiriCoin Reddit: reddit.com/r/SiriCoin/", font="Times 10", foreground="white")
        label19.place(x=650, y=400)
        label20 = ttk.Label(root, text="SiriCoin Youtube: youtube.com/c/UCwIpg_DrZLATfEteoIJBBqA", font="Times 10", foreground="white")
        label20.place(x=650, y=450)
        label21 = ttk.Label(root, text="SiriCoin Github: github.com/siricoin-project", font="Times 10", foreground="white")
        label21.place(x=650, y=500)
    else:
        messagebox.showerror('SiriCoin Wallet Error', '''
    Error: No Wallet address found in file data.txt
    Please run SiriCoinWalletsetup.exe or 
    SiriCoinWalletsetup.py before you run this file.''')
        root.quit()
                
button1 = ttk.Button(root, text="Start Wallet",style="AccentButton", command=slidebar, width=50)
button1.place(x=330, y=400)
label1 = ttk.Label(root, text="SiriCoin Crypto Wallet", font="Times 14", foreground="Cyan")
label1.place(x=400, y=0)
labell = ttk.Label(root, text="Designed by Shreyas-ITB from SiriCoin", font="Times 10", foreground="#E255CC")
labell.place(x=375, y=30)

root.mainloop()