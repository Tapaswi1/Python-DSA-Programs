# Merged Sorting
def merged(left,right):
    i=0
    j=0
    merged=[]
    while(i<len(left)) and (j<len(right)):
        if(left[i]<right[j]):
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j=j+1
    merged=merged+left[i:]+right[j:]
    return merged        
def merge(l):
    mid=len(l)//2
    if(len(l)==1):
        return l
    else:
        left=merge(l[:mid])
        right=merge(l[mid:])
    return merged(left,right)
l=[40,60,30,50,10,20]
print('Before Sorting:',l)
m=merge(l)
print("After Sorting:",m)
