import time

CSI = '\x1b['
ZERO = f'{CSI}0G'
ERASE = f'{CSI}2K'
RESET = f'{CSI}0m'


def animate(size, frames_count):
    colors = range(1, 231)
    for _ in range(frames_count):
        for color in colors:
            draw_romb(size, color)
            print(f"{CSI}{size}A{ZERO}", end="", flush=True)
            time.sleep(0.1)



def draw_line(offset, filled, color):
    offset_part = f"{' ' * offset}"
    filled_part = f"{CSI}48;5;{color}m{' ' * filled}"
    line = f"{ERASE}{offset_part}{filled_part}{RESET}"
    print(line)



def draw_romb(size, color):
    center = size // 2
    offset = center
    filled = 1

    for line in range(size):
        draw_line(offset, filled, color)

        if line < center:
            filled += 2
            offset -= 1
        else:
            filled -= 2
            offset += 1


animate(7, 1)