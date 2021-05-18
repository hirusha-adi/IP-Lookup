import requests
from tkinter import *
# from tkinter import Tk, Button, Label, Entry, Text # END is not defined here
import tkinter.font as font
from tkinter import messagebox

root = Tk()
root.title("IP Info by ZeaCeR#5641")
root['background'] = "#303030"
root.resizable(False, False)


# font properties
fontforbtns = font.Font(family="Arial", size="15", weight="bold")

ipadrrfromuser = Entry(root, width=25, borderwidth=5, bg="#111111", fg="#17FE00")
ipadrrfromuser.grid(row=2, column=0, columnspan=2)
ipadrrfromuser['font'] = fontforbtns


def ipinfoshit():
    ipfromuser = ipadrrfromuser.get()
    r = requests.get('http://ip-api.com/json/' + ipfromuser) # include the ip
    data = r.json()
    ipinfo = f'\n[+] Status: {data["status"]} \n[+] Country: {data["country"]} \n[+] Country Code: {data["countryCode"]} \n[+] Region: {data["region"]} \n[+] Region Name: {data["regionName"]} \n[+] City: {data["city"]} \n[+] ZIP: {data["zip"]} \n[+] Latitude: {data["lat"]} \n[+] Longitude: {data["lon"]} \n[+] TimeZone: {data["timezone"]} \n[+] ISP: {data["isp"]} \n[+] Organization: {data["org"]} \n[+] ASN: {data["as"]} \n[+] Query: {data["query"]} \n'
    tmain.insert(END, ipinfo)

def savetoFile():
    ipfromuser = ipadrrfromuser.get()
    texttowritetoFile = tmain.get("1.0", "end")
    file = open(ipfromuser + "_ip.txt", 'wb')
    file.write(texttowritetoFile)
    file.close()

def clearshit():
    tmain.delete("1.0", END)

def exittheprogram():
    root.quit()
    messagebox.showinfo('Made by ZeaCeR#5641', 'Thank you for using the program! Make sure to Share!')

# label main on top
labelontobbruh = Label(root, text="IP Info - v0.1 - Made by ZeaCeR#5641",  bg='#303030', fg='#17FE00')
labelontobbruh.grid(row=0, column=0, columnspan=3)

# main text area
fontfortbox = font.Font(family="Arial", weight="bold")
tmain = Text(root, height=18, width=50, bg="#111111", fg="#17FE00")
tmain.grid(row=1, column=0, columnspan=3)
tmain['font'] = fontfortbox

# buttons
bfind = Button(root, text="FIND", command=ipinfoshit, padx=60, bg="#4F4F4F", fg="#17FE00")
bfind.grid(row=2, column=2, columnspan=1)
bfind['font'] = fontforbtns

bclear = Button(root, text="Clear", command=clearshit, padx=40, bg="#4F4F4F", fg="#17FE00")
bclear.grid(row=3, column=0, columnspan=1)
bclear['font'] = fontforbtns

bsavetofile = Button(root, text="Save to File", command=savetoFile, padx=10, bg="#4F4F4F", fg="#17FE00")
bsavetofile.grid(row=3, column=1, columnspan=1)
bsavetofile['font'] = fontforbtns

bexit = Button(root, text="Exit", command=exittheprogram, padx=64, bg="#4F4F4F", fg="#E90000")
bexit.grid(row=3, column=2, columnspan=1)
bexit['font'] = fontforbtns


root.mainloop()
