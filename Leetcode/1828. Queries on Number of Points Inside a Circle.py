# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
    q = len(queries)
    p = len(points)
    output = [0] * q
    for i in range(q):
        for j in range(p):
            if math.sqrt(pow((points[j][0] - queries[i][0:2][0]), 2) + pow((points[j][1] - queries[i][0:2][1]), 2)) <= \
                    queries[i][2]:
                output[i] += 1
    return output