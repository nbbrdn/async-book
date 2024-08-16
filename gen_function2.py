def pause():
    print("generator working...")
    while True:
        print(a)
        yield a


gen = pause()
print(gen)

a = 10
print(next(gen))

a = 20
print(next(gen))
