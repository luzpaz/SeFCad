import FreeCAD
class MyWorkbench(Workbench):
    MenuText = "SeFCad workbench"
    ToolTip = "A workbench to create modals, defining constraints and saving the model as a Surface Evolver (.fe) file."
    

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import SelectAllVerticesScript, DefineVertexScript, DefineEdgeScript, DefineEdgeLoopScript, \
            DefineUnconnectedEdgesScript,  DefineFacetScript, DefinedFeaturesScript, \
            DeleteFeatureScript, DefineConstraintScript,DeleteConstraintScript, fa2feScript, SaveFeaturesScript, \
            LoadFeaturesScript \
                    # import here all the needed files that create your FreeCAD commands
        self.list = ["Select All Vertices", "Define Vertex", "Define Edge", "Define Edge Loop",
                     "Define Unconnected Edges", "Define Facet","Defined Features", "Delete Feature",
                     "Define Constraint","Delete Constraint", "fa2fe", "Save Features", "Load Features"]
                    # A list of command names created in the line above
        self.appendToolbar("My Commands", self.list)  # creates a new toolbar with your commands
        self.appendMenu("My New Menu", self.list)  # creates a new menu
    def Activated(self):
        import config
        config.designFileName = FreeCAD.ActiveDocument.Name
        return

    def Deactivated(self):
        """This function is executed when the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands", self.list)  # add commands to the context menu

    def GetClassName(self):
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"


FreeCAD.Gui.addWorkbench(MyWorkbench())