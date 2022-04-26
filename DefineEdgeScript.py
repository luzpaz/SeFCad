import FreeCAD, FreeCADGui, apilib, config
class DefineEdge:
    def Activated(self):
        from PySide import QtCore
        from PySide import QtGui
        import pickle
        edgesArray = config.edgesArray
        try:
            FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames
            if len(FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames) == 3:

                v1 = FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[0]
                v2 = FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[2]
                e = FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[1]

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
                        print("Edge successfully written")

                else:
                    print("Select features in correct order")

            else:
                print("Select 2 vertices and the edge")

            FreeCAD.Gui.Selection.clearSelection()
        except:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Select features first")
            msgBox.exec_()
    def GetResources(self):
        icon_str = FreeCAD.getHomePath() + "Mod/SeFCad/icons/DefineEdge.png"
        return {'Pixmap': icon_str,'MenuText': 'Edge',
                'ToolTip': 'Define a single edge. The selection format is: V-E-V'}
FreeCADGui.addCommand('Define Edge', DefineEdge())
