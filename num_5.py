from consts import CSI, RESET, ZERO

# print('^ y')

# for _ in range(10):
#     print('|')

# print(f'{CSI}1A', end='')

# for x in range(10):
#     if x > 1:
#         print(f"{CSI}{x+1}A{CSI}47m  {RESET}", end=f'{CSI}{10-x}B')
#     elif x == 1:
#         print(f"{CSI}1A{CSI}47m  {RESET}", end=f'{CSI}{10-x}B')
#     else:
#         print(f"{CSI}1C{CSI}47m  {RESET}", end='')

# print(f'{ZERO}{CSI}12B#------------------------> x')


print('^ y')
for y in range(10, -1, -1):
    if y != 0:
        print(f"|{CSI}{y*2}C{CSI}47m  {RESET}")
    else:
        print(f"|{CSI}47m  {RESET}")
print(f'#------------------------> x')