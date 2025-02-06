print("Type an integer:")
n = int(input())

primeNumbers = []
for i in range(2, n):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime: 
        primeNumbers.append(i)

print("All prime numbers under " + str(n) + " are:")
print(primeNumbers)
print("A total of " + str(len(primeNumbers)) + " prime numbers.")