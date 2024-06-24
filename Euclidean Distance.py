import math

# Define list of points
points = [(1, 2), (3, 4), (6, 8), (2, 1), (7, 3)]

# Calculate distance between two points
def euclideanDistance(point1, point2):
    return(math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2))

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Find minimum distance
min_distance = min(distances)

# Show minimum distance
print(f"Minimum distance : {round(min_distance,2)}")
