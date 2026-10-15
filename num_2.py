from consts import CSI, RESET, ZERO


def pattern(count: int):
    radius = 5

    for shift in range(count):
        for y in range(radius, 0, -1):
            stretch_by_x = 1
            for x in range(round((radius**2 - y**2)**0.5) + 1, radius+1):
                if round((radius**2 - x**2)**0.5) == y:
                    stretch_by_x += 1

            point_x = round((radius**2 - y**2)**0.5)*2 + shift*4*radius
            move_x = f"{CSI}{point_x}C"
            
            print(f"{move_x}{CSI}47m{'  ' * stretch_by_x}{RESET}")


        for y in range(1, radius + 1):
            stretch_by_x = 1
            for x in range(round((radius**2 - y**2)**0.5) + 1, radius+1):
                if round((radius**2 - x**2)**0.5) == y:
                    stretch_by_x += 1

            point_x = radius*2 - round((radius**2 - y**2)**0.5)*2 - \
                stretch_by_x*2 + 2 + radius*2 + shift*4*radius
            move_x = f"{CSI}{point_x}C"

            print(f"{CSI}1A{move_x}{CSI}47m{'  ' * stretch_by_x}{RESET}", 
                  end=f"{ZERO}")

    print(f"{CSI}{radius-1}B")


count_in = int(input('Count: '))
pattern(count_in)