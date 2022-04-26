import FreeCAD, FreeCADGui
import config, apilib
class DefineUnconnectedEdges:
    def Activated(self):
        from PySide import QtCore
        from PySide import QtGui
        edgesArray = config.edgesArray
        try:

            if len(FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames) % 3 == 0:
                for ind in range(int(len(FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames) / 3)):
                    index1 = ind * 3
                    index2 = ind * 3 + 1
                    index3 = ind * 3 + 2
                    v1 = FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[index1]
                    v2 = FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[index3]
                    e = FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[index2]

                    if "Vertex" in v1 and "Vertex" in v2 and "Edge" in e:
                        v1 = v1.replace("Vertex", "")
                        e = e.replace("Edge", "")
                        v2 = v2.replace("Vertex", "")

                        edgeInstance = apilib.edgeClass(e, v1, v2)

                        controlFlag = 0
                        for i in edgesArray:
                            if i.edgeNum == e:
                                controlFlag = controlFlag + 1

                        if controlFlag:
                            print("Edge already saved")
                        else:
                            edgesArray.append(edgeInstance)
                            config.edgesArray = edgesArray
                            print("Edges successfully written")
                    else:
                        print("Select features in correct order")

            FreeCAD.Gui.Selection.clearSelection()
        except:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Select features first")
            msgBox.exec_()
    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/DefineUnconnectedEdges.png")
        return {'Pixmap': icon_str,'MenuText': 'Unconnected Edges',
                'ToolTip': 'Define multiple unconnected edges from selected features. \
                           Selection format is: V-E-V-V-E-V-...-V-E-V'}
FreeCADGui.addCommand('Define Unconnected Edges', DefineUnconnectedEdges())