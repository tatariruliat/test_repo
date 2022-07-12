#(¬ (x  принадлежит  A) → (x  принадлежит  P)) → ((x  принадлежит  A) → (x  принадлежит  Q))
def f(x, a1, a2):
    return (not(a1 < x < a2) <= (25< x <50) <= ((a1 < x < a2) <= (32 < x <47)))

s = []
for a1 in range (-100, 100):
    for a2 in range (-100, 100):
        flag = True
        for x in range (-100, 100):
            if not (f(x, a1, a2)):
                flag = False
                if flag:
                    s.append(a2-a1)
print(max(s))