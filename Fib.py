n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

first = 0
second = 1
series = []

for i in range(n):
    series.append(first)
    first, second = second, first + second

print(series)