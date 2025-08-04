#Merge Sort

#Logic
def merge_sort(array_nums):
    #check
    if len(array_nums) > 1: 
        #sub array - from beginning to the middle point
        left_arr_nums = array_nums[:len(array_nums)//2]
        #sub array - from the middle point to the end
        right_arr_nums = array_nums[len(array_nums)//2:]
        
        #recursion conditiom
        merge_sort(left_arr_nums)
        merge_sort(right_arr_nums)
        
        #merging condition 
        i = 0 #left array index
        j = 0 #right array index
        k = 0 #merged array index
        
        while i < len(left_arr_nums) and j < len(right_arr_nums):
            #comparison
            if left_arr_nums[i] < right_arr_nums[j]:
                array_nums[k] = left_arr_nums[i]
                i += 1
            
            else:
                array_nums[k] = right_arr_nums[j]
                j += 1
            
            k += 1
        
        #left array
        while i < len(left_arr_nums):
            array_nums[k] = left_arr_nums[i]
            i += 1
            k += 1
        
        #right array
        while j < len(right_arr_nums):
            array_nums[k] = right_arr_nums[j]
            j += 1
            k += 1
        
#array
array_nums = [100, 7, 49, 1, 70, 36, 39, 69, 92, 48]
merge_sort(array_nums)

print(array_nums)