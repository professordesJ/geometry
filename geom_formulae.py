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



def cube_area(side):
    """
    'cube_area' calculates a cube's surface area given a side length:
    >>> cube_area(4)
    96

    :param side: the side length
    :return: the area
    """
    return 6*side*side


def cube_volume(side):
    """
    'cube_volume' calculates a cube's voulme given a side length:
    >>> cube_volume(4)
    64

    :param side: the side length
    :return: the volume (units^3 from side)
    """
    return side*side*side





if __name__ == "__main__":
    sampleSide = 4
    print(" sample side:",
          sampleSide,"\n",
          "square area:",
          square_area(sampleSide),
          "square perimeter:",
          square_perimeter(sampleSide),"\n"
          " equilateral triangle perimeter:",
          equilateral_triangle_perimeter(sampleSide),
          "  equilateral triangle area:",
          equilateral_triangle_area(sampleSide),"\n",
          "cube area:",
          cube_area(sampleSide),
          "  cube volume:",
          cube_volume(sampleSide),

    )




