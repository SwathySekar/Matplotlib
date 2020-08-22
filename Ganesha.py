#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:09:32 2020
@author: SwathySekar
Reference documentation : https://matplotlib.org/api/patches_api.html
"""
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle,Circle,RegularPolygon

canvasX, canvasY = 0.5, 0.5
grid = [[0.44,0.58],[0.44,0.56],[0.44,0.54],
        [0.44,0.5], [0.49,0.5], [0.45,0.3],
        [0.483,0.3],[0.51,0.3], [0.465,0.7],
        [0.325,0.4],[0.545,0.4]
        ]

vibhootiWidth = 0.05
eyeRadius = 0.007

plt.figure()
currentAxis = plt.gca()
#Rectangle Patch
currentAxis.add_patch(Rectangle((someX - .1, someY - .1), 0.13, 0.2, alpha=1,color = 'orange'))
currentAxis.add_patch(Rectangle(grid[0], vibhootiWidth, 0.000, alpha=1,color ='White'))
currentAxis.add_patch(Rectangle(grid[1], vibhootiWidth, 0.001, alpha=1,color ='White'))
currentAxis.add_patch(Rectangle(grid[2], vibhootiWidth, 0.001, alpha=1,color ='White'))
#Circular Patch
currentAxis.add_patch(Circle(grid[3], eyeRadius, alpha=1,color ='Black'))
currentAxis.add_patch(Circle(grid[4], eyeRadius, alpha=1,color ='Black'))

#Rectangle Patch for Trunk
currentAxis.add_patch(Rectangle(grid[5], 0.03, 0.18, alpha=1,color ='Red'))
currentAxis.add_patch(Rectangle(grid[6], 0.03, 0.03, alpha=1,color ='Red'))
currentAxis.add_patch(Rectangle(grid[7], 0.02, 0.06, alpha=1,color ='Red'))

#Polygon Patch for crown
currentAxis.add_patch(RegularPolygon(grid[8], 5, 0.1))

#Rectangle Patch for Ears
currentAxis.add_patch(Rectangle(grid[9], 0.06, 0.2, alpha=1,color ='Red'))
currentAxis.add_patch(Rectangle(grid[10], 0.06, 0.2, alpha=1,color ='Red'))

plt.show()
