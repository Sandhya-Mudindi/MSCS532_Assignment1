def insertion_sort_desc_order(arr):
    for i in range(len(arr)):
        key = arr[i]  # select the current element
        position = i  #  start from first element

        # shift the largest element sorted part to the right side
        while position > 0 and arr[position - 1] < key :  
            arr[position] = arr[position - 1]
            position = position - 1
            
            # place the element at the correct position
            arr[position] = key  

if __name__ == "__main__":
    array = [56,78,90,2,1,67,88, 99]
    print('original array:',array) 
    insertion_sort_desc_order(array)
    print("sorted array in desending order:",array)