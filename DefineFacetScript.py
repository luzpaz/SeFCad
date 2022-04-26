import FreeCAD, FreeCADGui, config, apilib
from PySide import QtCore
from PySide import QtGui
class DefineFacet:
    def Activated(self):
        verticesArray = config.verticesArray
        edgesArray = config.edgesArray
        facetsArray = config.facetsArray
        try:
            edgesOfFacet = []
            for i in range(len(FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames) - 1):
                selectedVertex1 = FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[
                    i % (len(FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames) - 1)].replace("Vertex", "")
                selectedVertex2 = FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[
                    (i + 1) % (len(FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames) - 1)].replace("Vertex", "")
                ddFlag = 0

                for e in edgesArray:
                    if selectedVertex1 == e.v1 and selectedVertex2 == e.v2:
                        edgesOfFacet.append(e.edgeNum)
                        ddFlag = 1
                        print(e.edgeNum)
                    elif selectedVertex2 == e.v1 and selectedVertex1 == e.v2:
                        edgesOfFacet.append("-" + e.edgeNum)
                        ddFlag = 1
                        print("-" + e.edgeNum)
                if not ddFlag:
                    pass
                else:
                    faceInstance = apilib.facetClass(FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[-1].replace("Face", ""),
                                              edgesOfFacet)

            aFlag = 0
            for f in facetsArray:
                if f.faceNum == faceInstance.faceNum:
                    aFlag = aFlag + 1
            if aFlag:
                print("Face already defined")
            else:
                facetsArray.append(faceInstance)
                config.facetsArray = facetsArray
                print("Face successfully defined")

            FreeCAD.Gui.Selection.clearSelection()

        except:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Select features first")
            msgBox.exec_()
    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/DefineFacet.png")
        return {'Pixmap': icon_str,'MenuText': 'Facet',
                'ToolTip': 'Define a facet from selected features. Selection format \
                          is: V-V-...-V-F'}
FreeCADGui.addCommand('Define Facet', DefineFacet())