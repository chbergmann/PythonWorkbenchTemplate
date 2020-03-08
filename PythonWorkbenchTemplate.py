import os
import FreeCAD
from importlib import reload

def get_module_path():
    """ Returns the current module path.
    Determines where this file is running from, so works regardless of whether
    the module is installed in the app's module directory or the user's app data folder.
    (The second overrides the first.)
    """
    return os.path.dirname(__file__)


def makeFeature1(base = None, green = False):
    '''Python command to create a Feature1'''
    import Feature1      
    reload(Feature1)     # causes FreeCAD to reload Feature1.py every time a new Feature1 is created.       
    fp = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Feature1")
    Feature1.Feature1Worker(fp, base, green)
    Feature1.Feature1ViewProvider(fp.ViewObject)
    FreeCAD.ActiveDocument.recompute()
    return fp
    
