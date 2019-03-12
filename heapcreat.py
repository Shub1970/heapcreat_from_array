def max_heap(list, index):
    left=2*index+1
    right=2*index+2
    if left<=len(list) and list[left]>list[index]:
        large=left
    else:
        large=index
    if right<=len(list) and list[right]>list[large]:            #there is a bug insteas of index i have to put large
        large=right
    if large!=index:
        key=list[index]
        list[index]=list[large]
        list[large]=key
        max_heap(list,large)
def heapBuld(list):
    last=len(list)//2
    for i in range(0,last):            #also you can write "for i in range(last-1,-1,-1):"  insist of "for i in range(0,last):
        max_heap(list,i)
    return list

array=[5,1,9,4,6,3,8]
print(heapBuld(array))



