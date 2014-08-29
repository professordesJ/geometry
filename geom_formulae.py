def square_perimeter(side):
    """
    'square_perimeter' calculates a square's perimeter given a side length:
    >>> square_perimeter(4)
    16

    :param side: the side length
    :return: the perimeter (same units as side length)
    """
    return 4*side


def square_area(side):
    """
    'square_area' calculates a square's area given a side length:
    >>> square_area(4)
    16

    :param side: the side length
    :return: the area (units^2 from side)
    """
    return side*side



def equilateral_triangle_perimeter(side):
    """
    'equilateral_triangle_perimeter' calculates an equilateral triangle's perimeter given a side length:
    >>> equilateral_triangle_perimeter(4)
    12
    :param side: the side length
    :return: the perimeter (same units as side length)
    """
    return 3*side


def equilateral_triangle_area(side):
    """
    'equilateral_triangle_area' calculates an equilateral triangle's area given a side length:
    >>> equilateral_triangle_perimeter(4)
    12
    :param side: the side length
    :return: the perimeter (same units as side length)
    """
    return 3**(1/2)*side/4

if __name__ == "__main__":
    sampleSide = 4
    print("sample side:",
          sampleSide,
          "  square area:",
          square_area(sampleSide),
          "  square perimeter:",
          square_perimeter(sampleSide),
          "  equilateral triangle perimeter:",
          equilateral_triangle_perimeter(sampleSide),
          "  equilateral triangle area:",
          equilateral_triangle_area(sampleSide)
    )




