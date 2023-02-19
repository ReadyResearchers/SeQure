# import other py files
import cf7
import ninjaForm
import wpForms
import os

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear() # clear screen
    print("[+] Welcome to SeQure!\n") # starting prompt
    url = input("[+] Enter the URL you would like to check: ")
    print("\n\t[+] Which plugin are you checking for?")
    print("\n\t[1] Contact Form 7 \n\t[2] Ninja Forms \n\t[3] WPForms")
    choice = input("\n\t[+] Enter plugin choice: ")
    print("------------------------------------------------------------------------------------------")
    if (choice == 1):
        cf7.reflectedCrossSite(url)
    elif (choice == 2):
        ninjaForm.reflectedCrossSite(url)
    else:
        wpForms.reflectedCrossSite(url)