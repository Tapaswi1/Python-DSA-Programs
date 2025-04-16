def bubble_sort(l):
    for p in range(len(l)-1):
        for q in range(len(l)-1):
            if l[q]>l[q+1]:
                l[q],l[q+1]=l[q+1],l[q]
        print(l)
    return l
l=list(map(int,input().split()))
print('Before sorting :',l)
s=bubble_sort(l)
print('After sorting:',s)
