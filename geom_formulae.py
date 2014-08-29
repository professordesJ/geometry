
def equilateral_triangle_perimeter(side):
    """
    'equilateral_triangle_perimeter' calculates an equilateral triangle's perimeter given a side length:
    >>> equilateral_triangle_perimeter(4)
    12
    :param side: the side length
    :return: the perimeter
    """
    return 3*side


def equilateral_triangle_area(side):
    """
    'equilateral_triangle_area' calculates an equilateral triangle's area given a side length:
    >>> equilateral_triangle_perimeter(4)
    12
    :param side: the side length
    :return: the area
    """
    return 3**(1/2)*side/4



def cube_volume(side):
    """
    'cube_volume' calculates a cube's volume given a side length:
    >>> cube_volume(4)
    64

    :param side: the side length
    :return: the volume
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


def tetrahedron_volume(side):
    """
    'regular_pentagon_perimeter' calculates an equilateral triangle's perimeter given a side length:
    >>> tetrahedron_volume(4)
    20
    :param side: the side length
    :return: the volume
    """
    return (side**3)/(6*2**(1/2))


def tetrahedron_area(side):
    """
    'regular_pentagon_area' calculates a regular tetrahedron's surface area given a side length:
    >>> tetrahedron_area(4)
    12
    :param side: the side length
    :return: the area
    """
    return 3**(1/2)*side

def ellipsoid_volume(axis1,axis2,axis3):
    """
    'ellipsoid_voulme' calculates an ellipsoid's surface volume given the axes:
    >>> ellipsoid_volume(1,2,3)
    12
    :param axis1,axis2,axis3: the axes lengths
    :return: the voulme
    """
    return 4*pi*axis1*axis2*axis3/3


if __name__ == "__main__":
    from numpy import *
    sampleSide, saxis1, saxis2, saxis3 = 4,1,2,3
    print(" sample side:",
          sampleSide,"\n",
          "equilateral triangle perimeter:",
          equilateral_triangle_perimeter(sampleSide),
          "  equilateral triangle area:",
          equilateral_triangle_area(sampleSide),"\n",
          "cube volume:",
          cube_volume(sampleSide),"\n",
          "regular pentagon perimeter:",
          regular_pentagon_perimeter(sampleSide),
          " regular pentagon area:",
          regular_pentagon_area(sampleSide),"\n",
          "tetrahedron_volume:",
          tetrahedron_volume(sampleSide),
          " tetrahedron area:",
          tetrahedron_area(sampleSide),"\n",
          "ellipsoid volume:",
          ellipsoid_volume(saxis1,saxis2,saxis3)
    )




