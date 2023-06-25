
def fibonaci(n): 
    if n <= 1: 
        return n 
    else: 
        return fibonaci(n - 1) + fibonaci(n - 2) 
number = int(input()) 
# check if the number is valid 
if number <= 0: 
    print("Please enter a positive integer") 
else: 
    print("Fibonacci sequence:") 
    for i in range(number): 
        print(fibonaci(i)) 
