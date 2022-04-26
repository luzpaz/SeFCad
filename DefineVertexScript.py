import FreeCAD, FreeCADGui
import apilib
import config
class DefineVertex:
    def Activated(self):
        from PySide import QtGui
        verticesArray = config.verticesArray
        """import pickle
        pickle_array_dump_location = str(FreeCAD.getHomePath() + "Mod/SeFCad/Data/")
        with open(pickle_array_dump_location + "all_arrays.txt", "rb") as fp:
            all_arrays = pickle.load(fp)
            verticesArray=all_arrays['vertices']"""
        try:
            vertices = FreeCAD.Gui.Selection.getSelectionEx()[0].SubObjects
            for i in range(len(vertices)):
                sflag = 0
                for dv in verticesArray:
                    if dv.vertexNum == FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[i].replace("Vertex", ""):
                        sflag = sflag + 1
                if sflag:
                    print("Vertex already defined")
                else:
                    verticesArray.append(apilib.vertexClass(FreeCAD.Gui.Selection.getSelectionEx()[0].SubElementNames[i].replace("Vertex", ""), vertices[i].Point[0], vertices[i].Point[1], vertices[i].Point[2]))
            """all_arrays.update({'vertices': verticesArray})
            with open(pickle_array_dump_location + "all_arrays.txt", "wb") as f:
                pickle.dump(all_arrays, f)"""
            config.verticesArray = verticesArray
            FreeCAD.Gui.Selection.clearSelection()
        except:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Select features first")
            msgBox.exec_()


    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/DefineVertex.png")
        return {'Pixmap': icon_str,'MenuText': 'Vertex',
                'ToolTip': 'Define one or more vertices from selected features'}
FreeCADGui.addCommand('Define Vertex', DefineVertex())