def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3,int(num**.5)):
        if num % i == 0:
            return False
    return True

for i in range(1,101):
    if is_prime(i) == True:
        print(i)
