import math

def prime_check(number1,number2):
    
    for i in range(2,int(math.sqrt(max(number1,number2)))):
        if number1%i==0:
            print("P not prime")
            return 0
        if number2%i==0:
            print("q not prime")
            return 0
    return 1

def check_co_prime(num, M):
    return math.gcd(num, M) == 1 

def get_smallest_co_prime(M):
    for i in range(2, M): # for every number *i* starting from 2 up to M
        if check_co_prime(i, M): # check if *i* is coprime with M
            return i # if it is, return i as the result
        
def encrypt(base,n,e):
    if(n==1):
        return 0
    c=1
    for i in range(0,e):
        c= (c*base)%n

    return c

def decrypt(base,n,d):
    if(n==1):
        return 0
    c=1
    for i in range(0,d):
        c= (c*base)%n

    return c

def main():
    p,q,phi,n,d,e=0,0,0,0,0,0
    p = int(input("P:"))
    q = int(input("Q:"))
    '''
    while prime_check(p,q)==0:
        p = int(input("P:"))
        q = int(input("Q:"))
    '''
    n=p*q
    phi=(p-1)*(q-1)
    e=get_smallest_co_prime(phi)
    val1=0
    while val1!=1:
        d+=1
        val1=(d*e)%phi

    print("n:",n)
    print("Phi:",phi)
    print("e:",e)
    print("d:",d)

    while True:
        mes=input("Message: ")
        for letter in mes:
            
            enc=encrypt(ord(letter),n,e)
            dec=chr(decrypt(enc,n,d))
            print("Encrypt:",enc,"\n","Decrypt:",dec)

if __name__ == "__main__":
    main()
