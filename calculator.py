def get_name(text: str):
    return input(f"Input the {text}: ")


def take_least_number(n):
    return n % 10


class CoupleCalculator:
    def __init__(self):
        self.constant = "TRUELOVE"
        self.couple_number = []

    def calculate(self, name1: str, name2: str):
        couple_name = "".join(name1.upper().split()) + "".join(name2.upper().split())
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
        result_number = "".join([str(s) for s in couple_number]) + "%"
        return result_number


if __name__ == "__main__":
    calculator = CoupleCalculator()
    calculator.calculate()
