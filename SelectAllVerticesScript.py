import FreeCAD, FreeCADGui, sys
class SelectAllVertices:
    def Activated(self):
        from PySide import QtCore
        from PySide import QtGui
        designFileName = FreeCAD.ActiveDocument.Name
        reply = QtGui.QInputDialog.getText(None, "Selecting all vertices", "Enter the number of vertices :")
        if reply[1]:
            replyText = reply[0]
            numOfVertices = int(replyText)
            for i in range(1, numOfVertices + 1):
                FreeCAD.Gui.Selection.addSelection(designFileName, 'Body', 'Vertex' + str(i))
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Operation cancelled")
            msgBox.exec_()
    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/SelectAllVertices.png")
        return {'Pixmap': icon_str,'MenuText': 'Select All Vertices',
                'ToolTip': 'All the vertices with vertex number up to the entered number are selected'}
FreeCADGui.addCommand('Select All Vertices', SelectAllVertices())