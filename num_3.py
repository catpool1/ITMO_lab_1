from consts import CSI, RESET
import os
import time


def draw_human():
    print(f"{CSI}4B{CSI}3C{CSI}48;2;232;190;172m{'  '}{RESET}")
    print(f"{CSI}3C{CSI}40m{'  '}{RESET}")
    print(f"{CSI}3C{CSI}40m{'  '}{RESET}")


brick_colour = f'{CSI}48;2;158;56;32m'
brick_colour_2 = f'{CSI}48;2;71;25;14m'
brick_part = f"{brick_colour_2}{' '}{brick_colour}{' '*2}"
brick_middle_3frame = f"{brick_colour}   {brick_part * 4}{brick_colour} "
brick_middle_4frame = f"{brick_colour}   {brick_part * 5}{brick_colour} "


for i in range(5):
    os.system("cls")
    draw_human()
    print(f"{CSI}5A{CSI}7C{brick_colour}{' '*4}{RESET}")
    time.sleep(0.1)

    os.system("cls")
    draw_human()
    print(f"{CSI}7A{CSI}11C{brick_colour}{' '*8}{RESET}")
    print(f"{CSI}{7+4}C{brick_colour}{' '*8}{RESET}")
    time.sleep(0.1)

    os.system("cls")
    draw_human()
    print(f"{CSI}6A{CSI}14C{brick_colour}{' '*16}{RESET}")
    print(f"{CSI}14C{brick_middle_3frame}{RESET}")
    print(f"{CSI}14C{brick_colour}{' '*16}{RESET}")
    time.sleep(0.1)

    os.system("cls")
    draw_human()
    print(f"{CSI}2A{CSI}14C{brick_colour}{' '*19}{RESET}")
    print(f"{CSI}14C{brick_middle_4frame}{RESET}")
    print(f"{CSI}14C{brick_middle_4frame}{RESET}")
    print(f"{CSI}14C{brick_colour}{' '*19}{RESET}")
    time.sleep(0.5)