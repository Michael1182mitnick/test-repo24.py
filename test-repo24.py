# Write a function to 
# multiple 2 numbers 
# without using multiplication
# to solve it I use recursion
def helper(a, b, counter):
    if (counter == 0):
        return 0
    
    return a + helper(a, b, counter - 1)

def multiply(a, b):
    # your code goes here 
    if (a == 0 or b == 0):
        return 0
    
    return helper(a, b, b)

print(multiply(7, 7))
print(multiply( 7, 0))
print(multiply(3, 30))
print(multiply(1, 3))