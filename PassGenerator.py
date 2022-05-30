import random
from os import system

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "`~!@#$%^&*()-_=+[{]}\|;:,<.>/?"

def option():
    op = input("\nYou haven't choosed any option, do you want to continye [y/N]: ")
    if op == "y" or op == "Y":
        system("clear")
        choice()
    else:
        print("\nBye\n")
        exit()

def check(lcase,ucase,num,sym):
    use_for = ""
    if lcase == "y" or lcase == "Y":
        use_for = use_for + lower_case
    if ucase == "y" or ucase == "Y":
        use_for = use_for + upper_case
    if num == "y" or num == "Y":
        use_for = use_for + numbers
    if sym == "y" or sym == "Y":
        use_for = use_for + symbols
    if (lcase == "n" or lcase == "N") and (ucase == "n" or ucase == "N") and (num == "n" or num == "N") and (sym == "n" or sym == "N"):
        option()
    else:
        main(use_for)

def choice():
    print("Things to be included in your password:\n")
    lcase = input("Lowercase [y/N] : ")
    ucase = input("Uppercase [y/N] : ")
    num = input("Numbers [y/N] : ")
    sym = input("Symbols [y/N] : ")
    check(lcase,ucase,num,sym)

# use_for = lower_case + upper_case + numbers + symbols

def main(use_for):
    passLen = int(input("\nEnter the Length of the password: "))
    # length_for_passwd = passLen
    passwd = "".join(random.sample(use_for, passLen))
    print("\nThe generated password: ", passwd)

choice()