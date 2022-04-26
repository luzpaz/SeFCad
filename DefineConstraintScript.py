import FreeCAD, FreeCADGui, config, apilib
from PySide import QtCore
from PySide import QtGui


class DefineConstraint:
    def Activated(self):
        verticesArray = config.verticesArray
        edgesArray = config.edgesArray
        facetsArray = config.facetsArray
        try:
            allSelected = FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames
            reply = QtGui.QInputDialog.getText(None, "Add constraints", "Enter the constraints :")
            if reply[1]:
                replyText = reply[0]
                constraintString = replyText
                for s in allSelected:
                    if "Vertex" in s:
                        vertexObj = next((v for v in verticesArray if v.vertexNum == s.replace("Vertex", "")), None)
                        vertexObj.constraints = vertexObj.constraints + constraintString + " "
                    if "Edge" in s:
                        edgeObj = next((e for e in edgesArray if e.edgeNum == s.replace("Edge", "")), None)
                        edgeObj.constraints = edgeObj.constraints + constraintString + " "
                    if "Face" in s:
                        faceObj = next((f for f in facetsArray if f.faceNum == s.replace("Face", "")), None)
                        faceObj.constraints = faceObj.constraints + constraintString + " "
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText("Operation cancelled")
                msgBox.exec_()

            # file_object.write(e + " " + v1 + " "  + v2 +"\n")
            # file_object.close()
            config.verticesArray = verticesArray
            config.edgesArray = edgesArray
            config.facetsArray = facetsArray
            FreeCAD.Gui.Selection.clearSelection()
        except:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Select features first")
            msgBox.exec_()

    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/DefineConstraint.png")
        return {'Pixmap': icon_str, 'MenuText': 'Add Constraint',
                'ToolTip': 'Desired constraint string is added to the selected feature(s)'}

FreeCADGui.addCommand('Define Constraint', DefineConstraint())