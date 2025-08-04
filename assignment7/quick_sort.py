#Quick Sort 

#Logic
def quick_sort(array_nums, left, right):
    #check
    if left < right:
        partition_position = partition(array_nums, left, right)
        #all elements that are less than the pivot element
        quick_sort(array_nums, left, partition_position - 1)
        #all elements that are greater then the pivot element
        quick_sort(array_nums, partition_position + 1, right)
        

def partition(array_nums, left, right):
    i = left
    j = right - 1
    pivot = array_nums[right]

    #check
    while i < j:
        #move i to right
        while i < right and array_nums[i] < pivot:
            i += 1
        #move j to left    
        while j > left and array_nums[j] >= pivot:
            j -= 1
        
        #check
        if i < j:
            #swap condition
            array_nums[i], array_nums[j] = array_nums[j], array_nums[i]
    
    #case 
    if array_nums[i] > pivot:
        #swap condition
        array_nums[i], array_nums[right] = array_nums[right], array_nums[i]
    
    return i    
        
            
                        
        
#array
array_nums = [100, 7, 49, 1, 70, 36, 39, 69, 92, 48]
quick_sort(array_nums, 0, len(array_nums) - 1)

print (array_nums)