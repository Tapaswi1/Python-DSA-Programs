# Selection Sort
def selection_sort(l):
    for i in range(len(l)):
        min_index=i
        for j in range(i+1,len(l)):
            if(l[j]<l[min_index]):
                min_index=j
        l[i],l[min_index]=l[min_index],l[i]
        print(l)
    return(l)
l=list(map(int,input().split()))
print("Before Sorting:",l)
s=selection_sort(l)
print("After Sorting:",s)
