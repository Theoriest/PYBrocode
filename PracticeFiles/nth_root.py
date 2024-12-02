nth = int(input("Enter the nth number for which to find root to"))
num = int(input("Enter the number for which to find nth root"))
prime = False
prime_num = []
factors = {}
power = 0
root = 1
#find prime numbers from zero to half the number
Max = int(num / nth)
for i in range(1,Max+1):
    for j in range(1,i):
        if i == j:
            continue
        elif i % j == 0 and j != 1:
            prime = False
            break
        else:
            prime = True
#add the prime numbers to prime_num list
    if prime:
        prime_num.append(i)

#find the factors for the prime numbers for the number
for p_num in prime_num:
    while num % p_num == 0 and num != 0 :
        num = num / p_num
        power = power + 1
        factors.update({p_num:power})
    power = 0
    if num == 1:
        break
#find the root
for factor in factors:
    root = root * factor ** (factors.get(factor) / nth)
print(factors)
print(root)
