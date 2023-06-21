def can(this):
    match(this):
        case("Да"):
             return 2
        case("Нет, но хочу научиться"):
            return 1
        case("Нет, и не хочу учиться"):
            return 0
def test(age,prog,three_d,reason):
    result = 0
    if age >= 11 and age <=15:
        result += 2
        result += can(prog)
        result += can(three_d)
