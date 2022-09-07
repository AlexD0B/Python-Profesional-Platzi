def make_division_by(n):
    def divisor(m):
        return n % m
    return divisor

division_by_3 = make_division_by(3)
print(division_by_3(18))

division_by_5 = make_division_by(5)
print(division_by_5(100))

division_by_20 = make_division_by(20)
print(division_by_20(200))

    