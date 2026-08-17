class Point():

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.dist = -1 * math.sqrt(x**2 + y**2)

    def __lt__(self, other: Point):
        return self.dist < other.dist

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points_list = [Point(x, y) for x, y in points]
        heapq.heapify(points_list)

        while len(points_list) > k:
            heapq.heappop(points_list)
        
        return [(p.x, p.y) for p in points_list]


