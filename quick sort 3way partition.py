
# coding: utf-8

# In[49]:


# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    #print(x)
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    p=j
    y=a[j]
    #print('before')
    #print(a)
    #print('l,p,y')
    #print(l,p,y)
    for i in range(l,j):
        if i<p:
            if a[i]==y:
                #print('i have come here')
                p=p-1
                a[i], a[p]=a[p], a[i]
    #print('after')
    #print(a)
            
    return j, p
    
    pass

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m, p = partition3(a, l, r)
   
    randomized_quick_sort(a, l, p - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

    


# In[50]:





# In[35]:




