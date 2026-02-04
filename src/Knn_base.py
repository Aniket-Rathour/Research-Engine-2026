import numpy as np

b= np.array([9,8])

points = [
    (np.array([1,1]), "A"),
    (np.array([2,2]), "A"),
    (np.array([8,8]), "B"),
    (np.array([9,9]), "B"),
]
distance = []
k=1

for x,y  in points:
    check =b - x
    dist = np.linalg.norm(check)
    distance.append((dist,y))

distance.sort(key= lambda x:x[0])
neighbors = distance[:k]
labels = [label for _, label in neighbors]
prediction = max(set(labels) , key= labels.count)
print(prediction)


#  FOR PURE NUMPY NO PYTHON = 

X = np.array([
    [1, 1],
    [2, 2],
    [8, 8],
    [9, 9]
])

y = np.array(["A", "A", "B", "B"])
b = np.array([9, 8])

diff = X - b
dists = np.linalg.norm(diff, axis=1)

idx = np.argsort(dists)

k=1
nearest = y[idx[:k]]
print(nearest)