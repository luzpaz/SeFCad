from PySide import QtCore
from PySide import QtGui
import pickle, FreeCAD

def gui_getSEArrayFile(dir=None):
    """Select a file via a dialog and return the file name.
    """
    if dir is None: dir = './'
    fname = QtGui.QFileDialog.getOpenFileName(None, "Select the SE arrays file...",
                                              dir, filter=" Pickle files (*.txt)")
    return fname[0]


class edgeClass:
    def __init__(self, edgeNum, v1, v2, constraint=""):
        self.edgeNum = edgeNum
        self.v1 = v1
        self.v2 = v2
        self.constraints = constraint


class vertexClass:
    def __init__(self, vertexNum, x, y, z, constraint=""):
        self.vertexNum = vertexNum
        self.xCoor = x
        self.yCoor = y
        self.zCoor = z
        self.constraints = constraint


class facetClass:
    def __init__(self, faceNum, edgeList, constraint="", ghostFlag=False):
        self.faceNum = faceNum
        self.edges = edgeList
        self.constraints = constraint
        self.gf = ghostFlag


class bodyClass:
    def __init__(self, bodyNum, faceList, constraints=""):
        self.bodyNum = bodyNum
        self.faceList = faceList
        self.constraints = constraints


def facetSortFunc(f):
    return int(f.faceNum)


def edgeSortFunc(e):
    return int(e.edgeNum)


def vertexSortFunc(v):
    return int(v.vertexNum)


def bodySortFunc(b):
    return int(b.bodyNum)



