#Insertion Sort

#Logic
def insertion_sort(array_nums):
    #outer loop
    for i in range(1, len(array_nums)):
        j = i 
        #inner loop
        #check
        while array_nums[j - 1] > array_nums[j] and j > 0:
            #swap condition
            array_nums[j - 1] , array_nums[j] = array_nums[j], array_nums[j -1]
            j -= 1

#array
array_nums = [100, 7, 49, 1, 70, 36, 39, 69, 92, 48]
insertion_sort(array_nums)

print(array_nums)