def fibo(n):
    if n in [0,1]:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("Give me a number: "))
print("fibo({}) = {}".format(num, fibo(num)))


