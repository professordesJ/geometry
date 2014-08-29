from math import *


def equilateral_triangle_area(side):
    """
    'equilateral_triangle_area' calculates an equilateral triangle's area given a side length:
    >>> equilateral_triangle_area(4)
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


def ellipsoid_volume(axis1, axis2, axis3):
    """
    'ellipsoid_voulme' calculates an ellipsoid's volume given the axes:
    >>> ellipsoid_volume(1, 2, 3)
    12
    :param axis1,axis2,axis3: the axes lengths
    :return: the voulme
    """
    return 4*pi*axis1*axis2*axis3/3


def hypercube_d_volume(side, dimension):
    """
    'hypercube_d_volume' calculates a hypercube's  volume given the side length and dimension d:
    >>> hypercube_d_volume(2,3)
    8
    :param axis1,axis2,axis3: the axes lengths
    :return: the volume
    """
    return side**dimension


def simplex_d_volume(side, dimension):
    """
    'simplex_d_volume' calculates a hyupercube's  volume given the side length and dimension d:
    >>> hypercube_d_volume(2,3)
    8
    :param axis1,axis2,axis3: the axes lengths
    :return: the volume
    """
    return ((dimension+1)**(1/2))*side**dimension/(2**(dimension/2)*factorial(dimension))


def triangle_area_heron(sidea, sideb, sidec):
    """
    'triangle_area_heron' calculates a triangles's  area given the side lengths:
    >>> triangle_area_heron(2, 3, 4)
    8
    :param sidea,sideb,sidec: the side lengths
    :return: the area
    """
    s = (sidea + sideb + sidec)/2

    return (s*(s-sidea)*(s-sideb)*(s-sidec))**(1/2)


def triangle_area_2sides_included_angle(sidea, sideb, anglec):
    """
    'triangle_area_2sides_included_angle' calculates a triangles's  area given two side lengths and included angle:
    >>> triangle_area_2sides_included_angle(3, 4, pi/2)
    6
    :param sidea,sideb,sidec: the side lengths
    :return: the area
    """

    return sidea*sideb*sin(anglec)/2


def area_pizza_slice(radius, anglec):
    """
    'triangle_area_2sides_included_angle' calculates a triangles's  area given two side lengths and included angle:
    >>> area_pizza_slice(2, pi)
    pi**2
    :param radius, anglec: the radius and angle
    :return: the area
    """

    return radius**2*anglec/2


if __name__ == "__main__":
    from numpy import *
    sampleSide, sampleAxis1, sampleAxis2, sampleAxis3,  \
     sampleDimension, sampleSidea, sampleSideb, sampleSidec, sampleAnglec = 4, 1, 2, 3, 4, 3, 4, 5, pi/2
    print(" sample side:",
          sampleSide, "\n",
          "sample axes:",
          sampleAxis1, sampleAxis2, sampleAxis3, "\n",
          "sample dimension:",
          sampleDimension, "\n",
          "equilateral triangle area:",
          equilateral_triangle_area(sampleSide), "\n",
          "cube volume:",
          cube_volume(sampleSide), "\n",
          "simplex (d dim) volume:",
          simplex_d_volume(sampleSide, sampleDimension), "\n",
          "hypercube (d dim) volume:",
          hypercube_d_volume(sampleSide, sampleDimension), "\n",
          "regular pentagon area:",
          regular_pentagon_area(sampleSide), "\n",
          "tetrahedron_volume:",
          tetrahedron_volume(sampleSide), "\n"
          " ellipsoid volume:",
          ellipsoid_volume(sampleAxis1, sampleAxis2, sampleAxis3), "\n",
          "triangle area (Heron):",
          triangle_area_heron(sampleSidea, sampleSideb, sampleSidec), "\n",
          "triangle area (2sides, 1 angle):",
          triangle_area_2sides_included_angle(sampleSidea, sampleSideb, sampleAnglec), "\n",
          "area of a pizza slice (given radius, angle):",
          area_pizza_slice(sampleSidea, sampleAnglec))
