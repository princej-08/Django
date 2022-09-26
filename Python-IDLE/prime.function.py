def isPrime(num):
    div=1
    cnt=0
    while div<=num:
        if num % div == 0:
            cnt = cnt+1

        div = div+1
    if cnt == 2:
        return True
    else:
        return False
n = int(input('Enter a Number: '))
res = isPrime(n)
if res:
    print('It is Prime Number')
else:
    print('It is not Prime Number')

for i in range(1,10+1):
    if i % 2 == 1:
        if isPrime(i):
            print(i)
