import FreeCAD, FreeCADGui, config, apilib
from PySide import QtCore
from PySide import QtGui
class fa2fe:
    def Activated(self):
        verticesArray = config.verticesArray
        edgesArray = config.edgesArray
        facetsArray = config.facetsArray
        bodiesArray = config.bodiesArray
        folder = QtGui.QFileDialog.getExistingDirectory()
        if folder:
            reply = QtGui.QInputDialog.getText(None, "", "Enter SE arrays file name:")
            if reply[1]:
                FE_file_name = reply[0]
                FE_file_name = FE_file_name + ".fe"
                feFile = open(folder + "/" + FE_file_name, "w")

                def vertexSortFunc(v):
                    return int(v.vertexNum)

                verticesArray.sort(key=vertexSortFunc)

                feFile.write("Vertices\n")

                for v in verticesArray:
                    feFile.write(v.vertexNum + " " + str(v.xCoor) + " " + str(v.yCoor) + " " + str(
                        v.zCoor) + " " + v.constraints + "\n")

                feFile.write("Edges \n")

                def edgeSortFunc(e):
                    return int(e.edgeNum)

                edgesArray.sort(key=edgeSortFunc)

                for e in edgesArray:
                    feFile.write(e.edgeNum + " " + e.v1 + " " + e.v2 + " " + e.constraints + "\n")

                feFile.write("Faces \n")

                def facetSortFunc(f):
                    return int(f.faceNum)

                facetsArray.sort(key=facetSortFunc)

                for f in facetsArray:
                    arrayToWrite = ""
                    for e in f.edges:
                        arrayToWrite = arrayToWrite + " " + e
                    feFile.write(f.faceNum + arrayToWrite + " " + f.constraints + " "   "\n")

                feFile.write("Bodies \n")

                def bodySortFunc(b):
                    return int(b.bodyNum)

                bodiesArray.sort(key=bodySortFunc)

                for b in bodiesArray:
                    arrayToWrite = ""
                    for f in b.faceList:
                        arrayToWrite = arrayToWrite + " " + f
                    feFile.write(str(b.bodyNum) + arrayToWrite + " " + b.constraints + " "   "\n")

                feFile.close()
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText("Save cancelled")
                msgBox.exec_()
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Save cancelled")
            msgBox.exec_()
    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/fa2fe.png")
        return {'Pixmap': icon_str,'MenuText': 'fa2fe',
                'ToolTip': 'Parse feature buffers into a .fe file'}
FreeCADGui.addCommand('fa2fe', fa2fe())