# -*- coding: utf-8 -*-

__title__ = "Feature1"
__author__ = "Christian Bergmann"
__license__ = "LGPL 2.1"
__doc__ = "An example for a workbench feature"

import PythonWorkbenchTemplate
import os
import FreeCADGui
import FreeCAD
from FreeCAD import Vector
import Part

    
class Feature1Worker:
    def __init__(self, 
                 fp,    # an instance of Part::FeaturePython
                 base = None,
                 green = False):
        fp.addProperty("App::PropertyLink", "Base",  "Feature1",  "This object will be modified by this feature").Base = base
        fp.addProperty("App::PropertyBool", "Green", "Feature1",  "Colorize the feature green").Green = green
        
        fp.Proxy = self
    
    def execute(self, fp):
        '''Do something when doing a recomputation, this method is mandatory'''
        redrawFeature1(fp)
        
    def onChanged(self, fp, prop):
        '''Do something when a property has changed'''
        if prop == "Base":
            redrawFeature1(fp)
            
        if prop == "Green":
            changeFeature1Color(fp)


class Feature1ViewProvider:
    def __init__(self, vobj):
        '''Set this object to the proxy object of the actual view provider'''
        vobj.Proxy = self
        self.Object = vobj.Object
            
    def getIcon(self):
        '''Return the icon which will appear in the tree view. This method is optional and if not defined a default icon is shown.'''
        return (os.path.join(PythonWorkbenchTemplate.get_module_path(), "Resources", "icons", "feature1.svg"))

    def attach(self, vobj):
        '''Setup the scene sub-graph of the view provider, this method is mandatory'''
        self.Object = vobj.Object
        self.onChanged(vobj, "Base")
 
    def updateData(self, fp, prop):
        '''If a property of the handled feature has changed we have the chance to handle this here'''
        pass
    
    def claimChildren(self):
        '''Return a list of objects that will be modified by this feature'''
        return [self.Object.Base]
        
    def onDelete(self, feature, subelements):
        '''Here we can do something when the feature will be deleted'''
        return True
    
    def onChanged(self, fp, prop):
        '''Here we can do something when a single property got changed'''
        pass
        
    def __getstate__(self):
        '''When saving the document this object gets stored using Python's json module.\
                Since we have some un-serializable parts here -- the Coin stuff -- we must define this method\
                to return a tuple of all serializable objects or None.'''
        return None
 
    def __setstate__(self,state):
        '''When restoring the serialized object from document we have the chance to set some internals here.\
                Since no data were serialized nothing needs to be done here.'''
        return None
        

def redrawFeature1(fp):
    # check plausibility of all parameters
    if not fp.Base:
        return
    
    # fp.Shape contains the newly created object
    fp.Shape = fp.Base.Shape.copy()
    changeFeature1Color(fp)
    
       
def changeFeature1Color(fp):       
    if fp.Green:
        fp.ViewObject.ShapeColor = (0.00, 1.00, 0.00)
    else:
        fp.ViewObject.ShapeColor = (1.00, 0.00, 0.00) 
    
        
class Feature1():
    '''This class will be loaded when the workbench is activated in FreeCAD. You must restart FreeCAD to apply changes in this class'''  
      
    def Activated(self):
        '''Will be called when the feature is executed.'''
        # Generate commands in the FreeCAD python console to create Feature1
        FreeCADGui.doCommand("import PythonWorkbenchTemplate")
        
        selection = FreeCADGui.Selection.getSelectionEx()
        if len(selection) > 0:
            FreeCADGui.doCommand("base = FreeCAD.ActiveDocument.getObject('%s')"%(selection[0].ObjectName))
            FreeCADGui.doCommand("PythonWorkbenchTemplate.makeFeature1(base)")
        else:            
            FreeCADGui.doCommand("PythonWorkbenchTemplate.makeFeature1()")
                  

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        if FreeCAD.ActiveDocument:
            return(True)
        else:
            return(False)
        
    def GetResources(self):
        '''Return the icon which will appear in the tree view. This method is optional and if not defined a default icon is shown.'''
        return {'Pixmap'  : os.path.join(PythonWorkbenchTemplate.get_module_path(), "Resources", "icons", "feature1.svg"),
                'Accel' : "", # a default shortcut (optional)
                'MenuText': "Feature1",
                'ToolTip' : "A template for a workbench feature" }

FreeCADGui.addCommand('Feature1', Feature1())
