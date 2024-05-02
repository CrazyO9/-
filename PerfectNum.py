# real factor* of sum equal itself
# real factor: factor except itself

def isPerfectNumber(num: int):
    real_factor = [idx for idx in range(1,num+1) if num%idx == 0 and num != idx]
    return sum(real_factor) == num

# user_input = int(input("enter a number: "))
perfect_numbers = [idx for idx in range(1,1000) if isPerfectNumber(idx)]

print(perfect_numbers)