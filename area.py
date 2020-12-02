from const import PI

def calc_round_area(radius):
    return PI * (radius ** 2)

def main():
    print("calc_round_area: ", calc_round_area(4))

main()
