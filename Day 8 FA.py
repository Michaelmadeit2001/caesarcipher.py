# Write your code below this line 👇
'''

Prime numbers are numbers that can only be cleanly divided by themselves and 1.

'''

def prime_checker(n): 
    
    if n <= 1:
        print("This is not a valid input")
        return
    for nums in range(2,n):
        if n % nums == 0:
            print(f'{n} is not a prime number.')
            return
        else:
            print("This is a prime number")
            return






# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(n)

