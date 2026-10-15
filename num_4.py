from consts import CSI, RESET

even = 0
odd = 0
count_even = 0
count_odd = 0


with open('sequence.txt') as f:
    for n, i in enumerate(f.readlines()):
        i = float(i)

        if n % 2 == 0:
            odd += abs(i)
            count_odd += 1
        else:
            even += abs(i)
            count_even += 1


even = even/count_even
odd = odd/count_odd

even, odd = round(even/((even+odd)/100)), round(odd/((even+odd)/100))

print(f"Чётные:\t\t{even}% {CSI}41m{' '*even}{RESET}")
print(f"Нечётные:\t{odd}% {CSI}44m{' '*odd}{RESET}")