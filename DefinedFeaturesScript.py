import FreeCAD, FreeCADGui
import apilib
import config
from PySide import QtGui
from PySide import QtCore
import math
class DefinedFeatures:
    def Activated(self):



        class inputApp(QtGui.QDialog):
            def __init__(self, vArr, eArr, fArr):
                super(inputApp, self).__init__()
                self.inputWidegts = []
                self.vArr = vArr
                self.eArr = eArr
                self.fArr = fArr
                self.currentSelection = []
                self.listWidgetInside = []
                self.inputAppui()

            def inputAppui(self):
                mainLayout = QtGui.QVBoxLayout()
                listw = QtGui.QListWidget()
                listw.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
                listw.addItem("#######")
                listw.addItem("VERTICES")
                listw.addItem("#######")
                for v in self.vArr:
                    listw.addItem("Vertex" + str(v.vertexNum) + "     " + "x: " + str(v.xCoor) + "   " + "y: " + str(
                        v.yCoor) + "   " + "z: " + str(v.zCoor) + "     " + v.constraints)
                listw.addItem("#######")
                listw.addItem("  EDGES  ")
                listw.addItem("#######")
                for e in self.eArr:
                    listw.addItem(
                        "Edge" + str(e.edgeNum) + "     " + "1st vertex: " + str(e.v1) + "     " + "2nd vertex: " + str(
                            e.v2) + "     " + e.constraints)
                listw.addItem("#######")
                listw.addItem("  FACETS  ")
                listw.addItem("#######")
                for f in self.fArr:
                    arrayToAppend = ""
                    for fe in f.edges:
                        arrayToAppend = arrayToAppend + "Edge: " + str(fe) + "    "
                    listw.addItem("Face" + str(f.faceNum) + "   " + arrayToAppend + "     " + f.constraints)
                self.listWidgetInside = listw
                showButton = QtGui.QPushButton("Show")
                showButton.clicked.connect(self.showButtonFunc)

                mainLayout.addWidget(listw)
                mainLayout.addWidget(showButton)
                self.setLayout(mainLayout)
                self.setGeometry(500, 500, 500, 500)

            def showButtonFunc(self):
                self.currentSelection = self.listWidgetInside.selectedItems()
                for s in self.currentSelection:
                    FreeCAD.Gui.Selection.addSelection(config.designFileName, 'Body', s.text().split()[0])
                self.close()

        a = inputApp(config.verticesArray, config.edgesArray, config.facetsArray)
        a.exec_()

    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/DefinedFeatures.png")
        return {'Pixmap': icon_str,'MenuText': 'Defined Features',
                'ToolTip': 'A windows with a list of defined features is shown'}
FreeCADGui.addCommand('Defined Features', DefinedFeatures())