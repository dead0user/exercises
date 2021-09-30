def count(*args) -> str:
    sum = 0
    for numb in args:
        sum += numb
    return str(sum)


print(count(2, 4, 1, 2, 4, 5, 10))
