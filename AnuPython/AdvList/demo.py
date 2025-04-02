#demo 1 *****************************

def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

primes = [x for x in range(2,51) if is_prime(x)]

print(primes)

#demo 2 *****************************

prices = [120,85,150,70,200,95]
disc_price = [price*0.8 if price>100 else price for price in prices]
print(disc_price)