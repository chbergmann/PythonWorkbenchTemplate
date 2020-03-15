# -*- coding: utf-8 -*-

__title__ = "FreeCAD Python Workbench Template - Init file"
__author__ = "Christian Bergmann"
__url__ = ["http://www.freecadweb.org"]
__doc__ = "A template for a new workbench"
__version__ = "0.0.1"


class PythonWorkbenchTemplate (Workbench):
    def __init__(self):
        import os
        import PythonWorkbenchTemplate
        self.__class__.MenuText = "PythonWorkbenchTemplate"
        self.__class__.ToolTip = "A template for a new workbench"
        self.__class__.Icon = os.path.join(PythonWorkbenchTemplate.get_module_path(), "freecad.svg")

    def Initialize(self):
        "This function is executed when FreeCAD starts"
        # import here all the needed files that create your FreeCAD commands
        from Feature1 import Feature1
        
        self.list = ["Feature1"] # A list of command names created in the line above
        self.appendToolbar("PythonWorkbenchTemplate", self.list) # creates a new toolbar with your commands
        self.appendMenu("PythonWorkbenchTemplate", self.list) # creates a new menu

    def Activated(self):
        "This function is executed when the workbench is activated"
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def ContextMenu(self, recipient):
        "This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu(self.__class__.MenuText, self.list) # add commands to the context menu

    def GetClassName(self): 
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"
    
       
Gui.addWorkbench(PythonWorkbenchTemplate())
