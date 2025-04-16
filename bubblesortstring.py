# Bubble Sorting with String
def bubble_sort(l):
    for p in range(len(l)-1):
        for q in range(len(l)-1):
            if len(l[q])>len(l[q+1]):
                l[q],l[q+1]=l[q+1],l[q]
        print(l)
    return l
l=list(map(str,input().split()))
print('Before Sorting:',l)
s=bubble_sort(l)
print('After Sorting:',s)
