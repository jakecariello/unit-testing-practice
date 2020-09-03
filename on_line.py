from typing import Tuple

def on_line(first_point: Tuple[float], second_point: Tuple[float], x: float) -> float:
    x1, y1 = first_point
    x2, y2 = second_point
    m = (y2 - y1) / (x2 - x1)

    return y1 + (m * (x - x1))

