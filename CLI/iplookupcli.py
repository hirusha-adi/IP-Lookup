import requests # 'pip install requests' in terminal to install this

# main function of this program
def get_ip_info():
    # gets the IP address from the user, hitting enter would pass this step and the API will show the information about your Public IP address
    inputip = input("[+] Enter the IPv4 address: ")
    # here, we are using the requests which we imported before and using it to get the data from the API (NOTE: THIS API DOESN'T NEED AN API KEY TO WORK)
    r = requests.get('http://ip-api.com/json/' + inputip)
    # will converted the above data ( which we got )  to json format from bytes
    data = r.json()
    # this will get the particular things from the json and print it origanizedly
    ipinfo = f'\n[+] Status: {data["status"]} \n[+] Country: {data["country"]} \n[+] Country Code: {data["countryCode"]} \n[+] Region: {data["region"]} \n[+] Region Name: {data["regionName"]} \n[+] City: {data["city"]} \n[+] ZIP: {data["zip"]} \n[+] Latitude: {data["lat"]} \n[+] Longitude: {data["lon"]} \n[+] TimeZone: {data["timezone"]} \n[+] ISP: {data["isp"]} \n[+] Organization: {data["org"]} \n[+] ASN: {data["as"]} \n[+] Query: {data["query"]} \n   '
    # print the output of the above step
    print(ipinfo)
    # this will ask weather you wan't to save the result to a file
    saveyn = input("\n[!] Do you wan't to save it to a file? y or n: ")
    # if you enter "y" for the above input
    if saveyn == "y" or "yes" or "Yes" or "Y" or "YES":
        # the program will try to create a file ( if a file is already there, the content will be added to the end of the existing file, if the file names are the same)
        try:
            # will ask for the file name
            filenametosave = input("[!] Enter the file name with extension: ")
            # will create a new file in the name you entered above, if the name is the same, this will append the text to the end of the same file
            file = open(filenametosave, "w+")
            # write the conent to the file
            file.write(ipinfo)
            # close the file and unload it from the memory
            file.close()
            # will print its successfully saved
            print("[+] Saved details to " + filenametosave + " successfully!")
        # if any error occured while creating the file
        except:
            # it will print this
            print("\n[-] File creation error!")
    # if you enter "n" for the above 'saveyn', it will exceute this
    elif saveyn == "n" or "no" or "No" or "N" or "YES": 
        # this will print a line to the user to see
        print("\n[-] No file will be created!")
    # if you entered something invalid like 'dog' instead of y or n or yes or no
    else:
        # then this will take place
        print("[-] Please enter a valid input! ( y or n )")

# puts ths script in an infinite loop
while True:
    # this will try call the function
    try:
        # call the main function, we named it as this, so now, we call it
        get_ip_info()
    # if you click Ctrl+C , the program will exit, and it is called keyboard interrupt
    except (KeyboardInterrupt, SystemExit):
        # will print this as an indication to the user
        print("[!] Exitting program! - made by ZeaCeR#5641")
        # will break the inifnite loop
        break