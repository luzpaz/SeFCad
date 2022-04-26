import FreeCAD, FreeCADGui, config, apilib
from PySide import QtCore
from PySide import QtGui
class SaveFeatures:
    def Activated(self):

    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/SaveFeatures.png")
        return {'Pixmap': icon_str,'MenuText': 'Short text', 'ToolTip': 'More detailed text'}
FreeCADGui.addCommand('Save Features', SaveFeatures())