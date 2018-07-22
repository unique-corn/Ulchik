from typing import Tuple, List


def min_convex_closure(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    def get_first_point(points: List[Tuple[int, int]]):
        return sorted(points, key=lambda x: x[1])[0]

    def get_angle(point1, point2):
        from math import atan2, pi

        x, y = abs(point1[0]) + point2[0], abs(point1[1]) + point2[1]
        return atan2(y, x)

    def get_next_point(current_point, points):
        angles = [(point, get_angle(current_point, point)) for point in points]
        print(f"angles = {sorted(angles, key=lambda x: x[1])}")
        return sorted(angles, key=lambda x: x[1])[0][0]

    result = []

    current_point = get_first_point(points)
    print(f"first point = {current_point}")
    result.append(current_point)
    points.remove(current_point)

    current_point = get_next_point(current_point, points)

    result.append(current_point)
    points.remove(current_point)
    points.append(result[0])
    print(result)

    for _ in range(len(points)):
        current_point = get_next_point(current_point, points)
        print(f"current point = {current_point}")

        if current_point == result[0]:
            print("The end :)")
            return result

        result.append(current_point)
        points.remove(current_point)
        print(f"result = {result}\n\npoints = {points}")
