def factorial(num):
    print("Valor incial: ", num)
    if num > 1:
        num = num * factorial(num - 1)
    print("valor final ->", num)
    return num


print(factorial(5))

