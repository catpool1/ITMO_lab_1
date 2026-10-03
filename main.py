import time
from consts import ZERO, ERASE

def draw_progress(task_num, width):
    for n in range(task_num):
        for filled in range(width):
            bar = f'{'#'*filled}{'-'*(width-filled-1)}'
            print(f'{ZERO}{ERASE}{n}: {bar}', end='', flush=True)
            time.sleep(0.1)

draw_progress(5, 10)