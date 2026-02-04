import numpy as np

def dot(arr1 , arr2):
    return np.dot(arr1,arr2, out=None)

def norm(arr1 ):
    return np.linalg.norm(arr1)

def add(arr1,arr2 ):
    return np.add(arr1,arr2,)

def multi(arr1,n ):
    v= np.array([arr1])
    return n*v

def proj(arr1,arr2):
    bb= np.dot(arr2,arr2)
    if(bb != 0):
        return (np.dot(arr1,arr2) / np.dot(arr2,arr2) * arr2)
    
    return np.zeros_like(arr1)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(dot(a, b))  
print(norm(a))          
print(add(a, b))        
print(multi(2, a))  
print(proj(a, b))             