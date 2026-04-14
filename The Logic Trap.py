# range(1, 21) starts at 1 and stops BEFORE 21
for i in range(1, 21):
    
    # 1. Check the hardest condition first (both 3 and 5)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        
    # 2. Check if it's only divisible by 3
    elif i % 3 == 0:
        print("Fizz")
        
    # 3. Check if it's only divisible by 5
    elif i % 5 == 0:
        print("Buzz")
        
    # 4. If none of the above, just print the number
    else:
        print(i)