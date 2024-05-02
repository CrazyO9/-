# find 1 to 100 of all prime numbers.

def isPrimeNum(num):
    dividNum = 2
    if num >= 1:
        while dividNum <= num:
            if num % dividNum == 0 and num != dividNum:
                return False
            dividNum += 1
        return True
    else:
        return False
    
prime_num = [idx for idx in range(100) if isPrimeNum(idx)]
print(prime_num)
