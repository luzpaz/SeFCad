import FreeCAD, FreeCADGui, config, apilib, pickle
from PySide import QtCore
from PySide import QtGui
class LoadFeatures:
    def Activated(self):
        FreeCADGui.doCommand('pickleFileName = gui_getSEArrayFile()')
        with open(pickleFileName, "rb") as fp:
            b = pickle.load(fp)
        config.verticesArray = b[0]
        config.edgesArray = b[1]
        config.facetsArray = b[2]
    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/LoadFeatures.png")
        return {'Pixmap': icon_str,'MenuText': 'Load Features',
                'ToolTip': 'Load previously saved feature buffers'}
FreeCADGui.addCommand('Load Features', LoadFeatures())