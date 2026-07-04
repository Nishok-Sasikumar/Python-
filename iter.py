def iteration(*x):
    x = iter(x)
    sum =0
    sum += next(x)
    sum += next(x)
    sum += next(x)
    return sum

print(iteration(10,20,30))