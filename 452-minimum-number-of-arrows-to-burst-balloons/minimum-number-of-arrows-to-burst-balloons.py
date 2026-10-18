class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])

        count = 1
        arrow_pos = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > arrow_pos:
                count += 1
                arrow_pos = points[i][1]

        return count