import FreeCAD, FreeCADGui
import config
import apilib
class DefineEdgeLoop:
    def Activated(self):
        edgesArray = config.edgesArray
        try:
            subElementNamesArray = list(FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames)
            subElementNamesArray.append(subElementNamesArray[0])
            for ind in range(int(len(subElementNamesArray) // 2)):
                index1 = ind * 2
                index2 = ind * 2 + 1
                index3 = ind * 2 + 2
                v1 = subElementNamesArray[index1]
                v2 = subElementNamesArray[index3]
                e = subElementNamesArray[index2]

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
        except:
            pass

    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/DefineEdgeLoop.png")
        return {'Pixmap': icon_str, 'MenuText': 'Edge Loop',
                'ToolTip': 'Define a loop of edges (multiple edges) from selected features. \
                The selection format is: V-E-V-E-...-V'}
FreeCADGui.addCommand('Define Edge Loop', DefineEdgeLoop())