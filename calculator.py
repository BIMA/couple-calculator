def get_name(text: str):
    return input(f"Input the {text}: ").upper()


def take_least_number(n):
    return n % 10


class CoupleCalculator:
    def __init__(self):
        self.constant = "TRUELOVE"
        self.couple_number = []

    def calculate(self):
        name1 = get_name("NAMA KAMU")
        name2 = get_name("NAMA PASANGAN KAMU")
        couple_name = "".join(name1.split()) + "".join(name2.split())
        for w in self.constant:
            self.couple_number.append(couple_name.count(w))

        couple_number = [int(n) for n in self.couple_number]

        while True:
            print(couple_number)
            temp = []
            for c in range(len(couple_number) - 1):
                addition = couple_number[c] + couple_number[c + 1]
                temp.append(addition)
            couple_number = [take_least_number(n) for n in temp]
            if len(couple_number) == 2:
                break
        print(couple_number)
        print(f"Kecocokan cinta antara {name1} dan {name2} sebesar", "".join([str(s) for s in couple_number]) + "%")


if __name__ == "__main__":
    calculator = CoupleCalculator()
    calculator.calculate()
