def heap_short(array,index):
    left=2*index+1
    right=2*index+2
    large=index
    if left<=len(array) and right<=len(array):
        if array[left]>array[index]:
            large=left
        if array[right]>array[large]:
            large=right
        if large!=index:
            array[index],array[large]=array[large],array[index]
            heap_short(array,large)
def heap_create(array):
    last=len(array)//2
    for i in range(last,-1,-1):
        heap_short(array,i)
    return array
array=[2,7,5,4,3,9,8]


print(heap_create(array))


