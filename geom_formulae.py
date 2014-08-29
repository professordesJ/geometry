
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


def regular_pentagon_perimeter(side):
    """
    'regular_pentagon_perimeter' calculates an equilateral triangle's perimeter given a side length:
    >>> regular_pentagon_perimeter(4)
    20
    :param side: the side length
    :return: the perimeter
    """
    return 5*side


def regular_pentagon_area(side):
    """
    'regular_pentagon_area' calculates a regular pentagon's area given a side length:
    >>> regular_pentagon_area(4)
    12
    :param side: the side length
    :return: the area
    """
    return (5*(5+2*5**(1/2)))**(1/2)*side**2/4



if __name__ == "__main__":
    sampleSide = 4
    print(" sample side:",
          sampleSide,"\n",
          "equilateral triangle perimeter:",
          equilateral_triangle_perimeter(sampleSide),
          "  equilateral triangle area:",
          equilateral_triangle_area(sampleSide),"\n",
          "cube area:",
          cube_area(sampleSide),
          "  cube volume:",
          cube_volume(sampleSide),"\n",
          "regular pentagon perimeter:",
          regular_pentagon_perimeter(sampleSide),
          " regular pentagon area:",
          regular_pentagon_area(sampleSide)
    )




