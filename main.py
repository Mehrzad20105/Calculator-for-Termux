#!/data/data/com.termux/files/usr/bin/env python

from colorama import Fore
import os
import time

os.system("clear")

class calculator:
    def basic():
        while (True):
            try:
                print()

                print(Fore.RESET, Fore.LIGHTCYAN_EX, "SUPER-CALCULATOR : BASIC")
                print(Fore.LIGHTCYAN_EX, "<CTRL>+C+ENTER / <CTRL>+D for QUIT")

                print(Fore.RESET, Fore.LIGHTGREEN_EX, "In Operation: \n\tType \"a\" for Addition.\n\tType \"s\" for Subtraction.\n\tType \"m\" for Multiplication.\n\tType \"d\" for Division.\n\tType \"p\" for Power of.\n\tType \"ms\" for Modulus.")
                print("-----------")
                n1 = float(input("Enter Number1: "))
                opr = str(input("Operation: "))
                n2 = float(input("Enter Number2: "))

                if (opr == "a"):
                    print(Fore.RESET, Fore.LIGHTCYAN_EX, "{} + {} = {}".format(n1, n2, n1 + n2))
                    time.sleep(3.2)
                    os.system("clear")

                elif (opr == "s"):
                    print(Fore.RESET, Fore.LIGHTCYAN_EX, "{} - {} = {}".format(n1, n2, n1 - n2))
                    time.sleep(3.2)
                    os.system("clear")

                elif (opr == "m"):
                    print(Fore.RESET, Fore.LIGHTCYAN_EX, "{} * {} = {}".format(n1, n2, n1 * n2))
                    time.sleep(3.2)
                    os.system("clear")

                elif (opr == "d"):
                    print(Fore.RESET, Fore.LIGHTCYAN_EX, "{} / {} = {}".format(n1, n2, n1 / n2))
                    time.sleep(3.2)
                    os.system("clear")

                elif (opr == "p"):
                    print(Fore.RESET, Fore.LIGHTCYAN_EX, "{} ** {} = {}".format(n1, n2, n1 ** n2))
                    time.sleep(3.2)
                    os.system("clear")

                elif (opr == "ms"):
                    print(Fore.RESET, Fore.LIGHTCYAN_EX, "{} % {} = {}".format(n1, n2, n1 % n2))
                    time.sleep(3.2)
                    os.system("clear")

                else:
                    print("Please Enter a valid value.")
                    time.sleep(2.2)
                    os.system("clear")
                    pass

                print()
                print()

            except ValueError:
                print("Please enter a valid value.")
                time.sleep(2.2)
                os.system("clear")
                pass
            except EOFError:
                os.system("clear")
                print("Thank you for download this script!")
                time.sleep(2.4)
                os.system("clear")
                quit()
            except KeyboardInterrupt:
                os.system("clear")
                print("Thank you for download this script!")
                time.sleep(2.4)
                os.system("clear")
                quit()
            except OverflowError:
                print()
                print("OVER-FLOW!!!")
                time.sleep(2)
                os.system("clear")
                pass

calculator.basic()

