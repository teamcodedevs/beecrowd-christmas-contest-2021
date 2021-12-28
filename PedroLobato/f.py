def validate_cpf(value: str):
    digits = value.replace('-', '')
    if(digits == '' or len(digits) != 11):
        return False
    for j in range(2):
        s = 0

        i = 0
        while i < 9 + j:
            s += int(digits[i]) * (10 + j - i)
            i += 1

        checkDigit = 11 - (s % 11)

        if(checkDigit == 11 or checkDigit == 10):
            checkDigit = 0

        if(checkDigit != int(digits[9 + j])):
            return False

    return True


n = int(input())

for _ in range(n):
    n_cpf = input()
    print('HoHoHoHo!' if validate_cpf(n_cpf) else 'Muahahaha!')
