num = int(input("Enter a Number:"))

if num>1:
    #iterate from 2 to n/2
    for i in range (2, num//2):
        #if num is divide by 2 or n/2 then return false
        if (num % i==0):
            print(num,"is not prime.")
            break
    else:
        print(num,"is a prime")
else:
    print(num,"is not prime")
