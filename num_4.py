from consts import CSI, RESET

p1 = 0
p2 = 0
cnt1 = 0
cnt2 = 0

with open('sequence.txt') as f:
    for n, i in enumerate(f.readlines()):
        i = float(i)

        if n % 2 == 0:
            p2 += i
            cnt2 += 1
        else:
            p1 += i
            cnt1 += i


p1 = p1/cnt1
p2 = p2/cnt2

p1, p2 = round(p1/((p1+p2)/100)), round(p2/((p1+p2)/100))

print(f"{p1}% {CSI}41m{' '*p1}{RESET}")
print(f"{p2}% {CSI}44m{' '*p2}{RESET}")