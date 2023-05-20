def pascal_memoization(row, col, memo):
    if col == 0 or col == row:
        return 1
    elif (row, col) in memo:
        return memo[(row, col)]
    else:
        result = pascal_memoization(row - 1, col - 1, memo) + pascal_memoization(row - 1, col, memo)
        memo[(row, col)] = result
        return result



def show_pas(n):
    memo = {}  # Create an empty dictionary to store calculated values
    for i in range(n):
        for j in range(pp-i+1):
            print(end=" ") # leading spaces
        for j in range(i + 1):
            print(pascal_memoization(i, j, memo), end=" ")
        print()
        
pp = int(input("Enter the number of rows: "))
show_pas(pp)



