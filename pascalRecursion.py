def pas_tri(numRows):
    '''Print Pascal's triangle with numRows.'''
    if numRows == 1:
        return [[1]] #in case of like if some type number of row is 1 then we'll simply return 1
    else:
        res_arr = pas_tri(numRows-1) # recursive call to pas_tri
        # here using the previous row to calculate current row 
        cur_row = [1] # every rows starting element is 1
        prev_row = res_arr[-1] 
        for i in range(len(prev_row)-1):
            # we are calculating the sum of 2 elements for the current index.
            cur_row.append(prev_row[i] + prev_row[i+1]) 
        cur_row += [1] # every rows ending element is 1
        res_arr.append(cur_row)
        return res_arr
        
tri_array = pas_tri(int(input("Enter the number of rows: ")))

for i,row in enumerate(tri_array):
  for j in range(len(tri_array) - i + 1):
    print(end=" ") # leading spaces
  for j in row:
    print(j, end=" ") # printing
  print()  # print new line