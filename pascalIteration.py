
# Pascal's Triangle program using Binomial Coefficient
 
# taking user input here
n = int(input("Enter the number of rows: "))
 
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    # we know that first element is always 1
    Bin_C = 1
    for j in range(1, i+1):
 

        print(' ', Bin_C, sep='', end='')
 
        # using Binomial Coefficient formula to find the numbers here
        Bin_C = Bin_C * (i - j) // j
    print() #printing new line