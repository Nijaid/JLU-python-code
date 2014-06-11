import math
import numpy
import matplotlib as mpl

"""
Pre-defined colormaps for GC plots.
"""

def Star(x, y, size, numpoints=5, rotation=0):
    """
    Calculate the vertices for a star. You can set the star's central
    position, its size, number of sides, and rotation.

    Inputs:
    x = x center coordinate
    y = y center coordinate
    size = size (in image coordinates)
    numpoints = number of points on the star (default = 5)
    rotation = angle of the star (default = 0)

    Example:
    star = gccolors.Star(0.5, 0.5, 0.1)
    fill(star[0], star[1], fill=False, edgecolor='r')
    """

    scale = size / math.sqrt(math.pi)

    r = scale * numpy.ones(numpoints * 2)
    r[1::2] *= 0.4

    theta = 2.0 * math.pi / (2 * numpoints)
    theta *= numpy.arange(2 * numpoints)
    theta += rotation

    verts_x = r * numpy.sin(theta)
    verts_y = r * numpy.cos(theta)

    return (verts_x, verts_y)
    

def idl_rainbow():
    cdict = {}
    cdict['red'] = []
    cdict['green'] = []
    cdict['blue'] = []

    r = numpy.array([   0,  4,  9,  13,  18,  22,  27,  31,  36,  40,  45,  50,  54,  58,  61,  64,  68,  69,  72,  74,  77,  79,  80,  82,  83,  85,  84,  86,  87,  88,  86,  87,  87,  87,  85,  84,  84,  84,  83,  79,  78,  77,  76,  71,  70,  68,  66,  60,  58,  55,  53,  46,  43,  40,  36,  33,  25,  21,  16,  12,   4,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   4,   8,  12,  21,  25,  29,  33,  42,  46,  51,  55,  63,  67,  72,  76,  80,  89,  93,  97, 101, 110, 114, 119, 123, 131, 135, 140, 144, 153, 157, 161, 165, 169, 178, 182, 187, 191, 199, 203, 208, 212, 221, 225, 229, 233, 242, 246, 250, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                    dtype=float)
    g = numpy.array([   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   4,   8,  16,  21,  25,  29,  38,  42,  46,  51,  55,  63,  67,  72,  76,  84,  89,  93,  97, 106, 110, 114, 119, 127, 131, 135, 140, 144, 152, 157, 161, 165, 174, 178, 182, 187, 195, 199, 203, 208, 216, 220, 225, 229, 233, 242, 246, 250, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 250, 242, 238, 233, 229, 221, 216, 212, 208, 199, 195, 191, 187, 178, 174, 170, 165, 161, 153, 148, 144, 140, 131, 127, 123, 119, 110, 106, 102,  97,  89,  85,  80,  76,  72,  63,  59,  55,  51,  42,  38,  34,  29,  21,  17,  12,   8,   0],
                    dtype=float)
    b = numpy.array([   0,   3,   7,  10,  14,  19,  23,  28,  32,  38,  43,  48,  53,  59,  63,  68,  72,  77,  81,  86,  91,  95, 100, 104, 109, 113, 118, 122, 127, 132, 136, 141, 145, 150, 154, 159, 163, 168, 173, 177, 182, 186, 191, 195, 200, 204, 209, 214, 218, 223, 227, 232, 236, 241, 245, 250, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 246, 242, 238, 233, 225, 220, 216, 212, 203, 199, 195, 191, 187, 178, 174, 170, 165, 157, 152, 148, 144, 135, 131, 127, 123, 114, 110, 106, 102,  97,  89,  84,  80,  76,  67,  63,  59,  55,  46,  42,  38,  34,  25,  21,  16,  12,   8,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                    dtype=float)

    for i in range(len(r)):
        rtuple = (i / 255.0, r[i] / 255.0, r[i] / 255.0)
        cdict['red'].append(rtuple)

        gtuple = (i / 255.0, g[i] / 255.0, g[i] / 255.0)
        cdict['green'].append(gtuple)

        btuple = (i / 255.0, b[i] / 255.0, b[i] / 255.0)
        cdict['blue'].append(btuple)

    return mpl.colors.LinearSegmentedColormap('colormap', cdict, 1024)

    
