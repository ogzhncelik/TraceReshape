# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FreehandReshape
                                 A QGIS plugin
 A plugin for reshaping polygons by holding down the mouse button
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-07-08
        copyright            : (C) 2025 by ogzhncelik
        email                : ogzhn.celik@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FreehandReshape class from file FreehandReshape.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from . import resources
    from .trace_reshape import TraceReshape
    return TraceReshape(iface)
