
def selection_sort(lst: list) -> None :
    i = 0
    length = len(lst)
    while i < length :
        j = i
        while j < length :
            position = lst.index(min(lst))                
            temp = lst[position]
            lst[position] = temp
            print(lst)
            print(position)
            print(temp)
            j += 1
        i += 1
selection_sort([4,3,2,1])
'''
lst = [1,2,3,4]
i = 0
length = len(lst)
while i < length :
    j = i
    while j < length :
        print(lst[j])
        j += 1
    i += 1
'''
