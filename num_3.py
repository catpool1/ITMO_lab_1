from consts import CSI, RESET
import os
import time


def f():
    print(f"{CSI}4B{CSI}3C{CSI}48;2;232;190;172m{'  '}{RESET}")
    print(f"{CSI}3C{CSI}40m{'  '}{RESET}")
    print(f"{CSI}3C{CSI}40m{'  '}{RESET}")


br_cl = f'{CSI}48;2;158;56;32m'
br_cl_2 = f'{CSI}48;2;71;25;14m'
br_sm = f"{br_cl_2}{' '}{br_cl}{' '*2}"


for i in range(5):
    os.system("cls")
    f()
    print(f"{CSI}5A{CSI}7C{br_cl}{' '*4}{RESET}")
    time.sleep(0.15)

    os.system("cls")
    f()
    print(f"{CSI}7A{CSI}11C{br_cl}{' '*8}{RESET}")
    print(f"{CSI}{7+4}C{br_cl}{' '*8}{RESET}")
    time.sleep(0.15)

    os.system("cls")
    f()
    print(f"{CSI}6A{CSI}14C{br_cl}{' '*16}{RESET}")
    print(f"{CSI}14C{br_cl}{' '*3}{br_sm * 4}{br_cl}{' '}{RESET}")
    print(f"{CSI}14C{br_cl}{' '*16}{RESET}")
    time.sleep(0.15)

    os.system("cls")
    f()
    print(f"{CSI}2A{CSI}14C{br_cl}{' '*19}{RESET}")
    print(f"{CSI}14C{br_cl}{' '*3}{br_sm * 5}{br_cl}{' '}{RESET}")
    print(f"{CSI}14C{br_cl}{' '*3}{br_sm * 5}{br_cl}{' '}{RESET}")
    print(f"{CSI}14C{br_cl}{' '*19}{RESET}")
    time.sleep(0.5)