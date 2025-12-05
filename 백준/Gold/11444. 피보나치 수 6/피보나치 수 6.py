MOD = 1000000007

def fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n // 2)
        c = (a * ((b * 2 - a) % MOD)) % MOD
        d = (a * a + b * b) % MOD
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, (c + d) % MOD)

n = int(input())
print(fib(n)[0] % MOD)