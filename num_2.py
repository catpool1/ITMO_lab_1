from consts import CSI, RESET, ZERO

def pattern(radius: int, count: int):
    for shift in range(count):
        for y in range(radius, 0, -1):
            s = 1
            for x in range(round((radius**2 - y**2)**0.5) + 1, radius+1):
                if round((radius**2 - x**2)**0.5) == y:
                    s += 1
            
            print(f"{CSI}{round((radius**2 - y**2)**0.5)*2 + shift*4*radius}C{CSI}47m{'  ' * s}{RESET}")

        for y in range(1, radius + 1):
            s = 1
            for x in range(round((radius**2 - y**2)**0.5) + 1, radius+1):
                if round((radius**2 - x**2)**0.5) == y:
                    s += 1

            print(f"{CSI}1A{CSI}{radius*2 - round((radius**2 - y**2)**0.5)*2 - s*2 + 2 + radius*2 + shift*4*radius}C{CSI}47m{'  ' * s}{RESET}", end=f"{ZERO}")

    print(f"{CSI}{radius-1}B")

rad, cnt = map(int, input('Radius, count: ').split())

pattern(rad, cnt)