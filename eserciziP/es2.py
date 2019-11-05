
def serie(n, s = 0):
    res = []
    def interna(n):
        if (n == 0):
            res.append(n)
            yield 0
        else:

            yield from interna(n-1)
            x = res.pop() + n
            res.append(x)
            yield x
    return interna(n)



gen = serie(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))