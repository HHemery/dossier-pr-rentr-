import random as rd


def just_price(n):
    c = rd.randint(1, 100)  # prices product
    print(c)
    for i in range(n):
        d = rd.randint(0, 100)  # prices player
        print(d)
        if c == d:
            return "bravo"
        else:
            if c < d:
                print("eleve")
            else:
                print("low")
        if i == n-1:
            return "perdu"
