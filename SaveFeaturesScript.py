import FreeCAD, FreeCADGui, config, apilib, pickle
from PySide import QtCore
from PySide import QtGui
class SaveFeatures:
    def Activated(self):
        folder = QtGui.QFileDialog.getExistingDirectory()
        if folder:
            reply = QtGui.QInputDialog.getText(None, "SE arrays save", "Enter SE arrays file name:")
            if reply[1]:
                # user clicked OK
                replyText = reply[0]
                allArrays = [config.verticesArray, config.edgesArray, config.facetsArray]
                with open(folder + "/" + reply[0] + ".txt", "wb") as f:
                    pickle.dump(allArrays, f)
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText("Save cancelled")
                msgBox.exec_()

        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Save cancelled")
            msgBox.exec_()

    def GetResources(self):
        icon_str = str(FreeCAD.getHomePath() + "Mod/SeFCad/icons/SaveFeatures.png")
        return {'Pixmap': icon_str,'MenuText': 'Save Features',
                'ToolTip': 'Save current feature buffers as a pickle file'}
FreeCADGui.addCommand('Save Features', SaveFeatures())