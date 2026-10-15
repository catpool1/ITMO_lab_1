from consts import CSI, RESET

print('^ y')
for y in range(10, -1, -1):
    if y != 0:
        print(f"|{CSI}{y*2}C{CSI}47m  {RESET}")
    else:
        print(f"|{CSI}47m  {RESET}")
print(f'#------------------------> x')