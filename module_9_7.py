# Декораторы

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        k = 0
        for i in range(2, result // 2 + 1):
            if result % i == 0:
                k = k + 1
        if k == 0:
            return f"Простое - {result}"
        else:
            return f"Составное - {result}"
    return wrapper


@is_prime
def sum_three(a,b,c):
    return a + b + c

a,b,c, = 3,4,5
print(sum_three(a,b,c))
a,b,c, = 2,3,6
print(sum_three(a,b,c))


