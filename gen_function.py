def square():
    for e in range(0, 11, 2):
        yield e**2


gen = square()
print(gen)

for i in gen:
    print(i)
