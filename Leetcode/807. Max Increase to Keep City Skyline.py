# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    lenAll = len(grid)
    lenItem = len(grid[1])
    skyline_H = []  # len = lenAll   - Horizontal view (from right or left)
    skyline_V = []  # len = lenItem  - Vertical view (from top or bottom)
    skyline_V_temp = []
    gridDifference = []
    for j in range(lenItem):
        skyline_H.append(max(grid[j]))
    for j in range(lenItem):
        for i in range(lenAll):
            skyline_V_temp.append(grid[i][j])
        skyline_V.append(max(skyline_V_temp))
        skyline_V_temp = []
    for i in range(lenAll):
        for j in range(lenItem):
            gridDifference.append(min(skyline_H[i], skyline_V[j]) - grid[i][j])
    return sum(gridDifference)