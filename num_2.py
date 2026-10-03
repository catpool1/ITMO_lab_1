from consts import CSI, RESET, ZERO

for y in range(5):
    for x in range(20):
        if x**2 + (4-y)**2 == 25:
            print(f'{CSI}{x}C{CSI}47m{"  "}{RESET}{ZERO}', end='')
        if (x-20)**2 + (4-y)**2 == 25:
            print(f'{CSI}{x}C{CSI}47m{"  "}{RESET}')