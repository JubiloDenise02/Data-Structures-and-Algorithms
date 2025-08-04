#Bubble Sort

#logic
def bub_sort(array_nums):
    #outer loop
    for i in range(len(array_nums)- 1, 0, -1):
        #inner loop
        for j in range(i):
            #check 
            if array_nums[j] > array_nums[j+1]:
                #swap
                temp_v = array_nums[j]
                array_nums[j] = array_nums[j+1]
                array_nums[j+1] = temp_v
        

#array
array_nums = [100, 7, 49, 1, 70, 36, 39, 69, 92, 48]
bub_sort(array_nums)

print(array_nums)