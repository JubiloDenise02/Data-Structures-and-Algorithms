#Selection Sort

#logic
def select_sort (array_nums):
    for i in range(9):
        #assigning i to hold min position
        min_pos = i
        
        for j in range(i, 10):
            #change the min position 
            #check 
            if array_nums[j] < array_nums[min_pos]:
                min_pos = j
            
        #swap
        temp_v = array_nums[i]
        array_nums[i] = array_nums[min_pos]
        array_nums[min_pos] = temp_v
        

#array
array_nums = [100, 7, 49, 1, 70, 36, 39, 69, 92, 48]

select_sort(array_nums)

print(array_nums)