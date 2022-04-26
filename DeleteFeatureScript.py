import FreeCAD, FreeCADGui, config, apilib
from PySide import QtCore
from PySide import QtGui


class DeleteFeature:
    def Activated(self):
        verticesArray = config.verticesArray
        edgesArray = config.edgesArray
        facetsArray = config.facetsArray
        try:
            selection = FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames
            qm = QtGui.QMessageBox()
            qm.setText("Are you sure to delete the selected features")
            qm.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
            answer = qm.exec_()

            if answer == QtGui.QMessageBox.Yes:
                for selected in selection:
                    dFlag = 0
                    if "Vertex" in selected:
                        for element in verticesArray:
                            if element.vertexNum == selected.replace("Vertex", ""):
                                dFlag = dFlag + 1
                                verticesArray.remove(element)
                    elif "Edge" in selected:
                        for element in edgesArray:
                            if element.edgeNum == selected.replace("Edge", ""):
                                dFlag = dFlag + 1
                                edgesArray.remove(element)
                    elif "Face" in selected:
                        for element in facetsArray:
                            if element.faceNum == selected.replace("Face", ""):
                                dFlag = dFlag + 1
                                facetsArray.remove(element)
                    if dFlag:
                        print("Feature removed successfully")
                    else:
                        print("Feature could not be found")

                FreeCAD.Gui.Selection.clearSelection()
            else:
                pass
        except:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Select features first")
            msgBox.exec_()
    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/DeleteFeature.png")
        return {'Pixmap': icon_str, 'MenuText': 'Delete features',
                'ToolTip': 'Delete selected features if defined'}

FreeCADGui.addCommand('Delete Feature', DeleteFeature())