def insertion_sort_desc_order(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        position = i
        while position > 0 and arr[position - 1] < key :
            arr[position] = arr[position - 1]
            position = position - 1
            arr[position] = key

if __name__ == "__main__":
    array = [56,78,90,2,1,67,88, 99]
    print('original array:',array) 
    insertion_sort_desc_order(array)
    print("sorted array in desending order:",array)