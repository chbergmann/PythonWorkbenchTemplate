# Python Workbench Template
   
A template for creating a new FreeCAD workbench in Python.  
FreeCAD offers great opportunities to create scripted objects. This should be a starting point to create your own workbench.
  
## Installation

### Automatic Installation
**Note: This is the recommended way to install this workbench.**  
The Python Workbench Template will be available soon through the builtin FreeCAD [Addon Manager](https://github.com/FreeCAD/FreeCAD-addons#1-builtin-addon-manager).
Once installed all that is needed is to restart FreeCAD and the workbench will be available in the [workbench dropdown list](https://freecadweb.org/wiki/Std_Workbench) menu.

### Manual Installation

```bash
cd ~/FreeCAD/Mod/ 
git clone https://github.com/chbergmann/PythonWorkbenchTemplate.git
```
When you restart FreeCAD, "Python Workbench Template" workbench should now show up in the [workbench dropdown list](https://freecadweb.org/wiki/Std_Workbench).
  
## Getting started with a new FreeCAD workbench
- Create a new git repository and copy the contents of this project to your new project
- Rename PythonWorkbenchTemplate.py to YourWorkbenchsName.py. Search all files for PythonWorkbenchTemplate and replace with the name of your workbench
- Rename Feature1.py with YourNewFeature.py 
- Edit InitGui.py. Delete Feature1 and add your new feature instead. Edit the \__title\__, \__author\__, \__url\__ and \__version\__ tags.
- Write your new feature and test it well.
- Write a documentation in README.md. Explain the purpose of your workbench. Explain your features. Screenshots are great.
- Draw a .svg icon for the workbench and for each feature. You can export FreeCAD designs to .svg.
- Announce your workbench in the [FreeCAD forum](https://forum.freecadweb.org/index.php). Add the link of your new thread in README.md
- Add your workbench to the [Addon manager](https://github.com/FreeCAD/FreeCAD-addons)

## Tools
### ![Feature1Icon](./Resources/icons/feature1.svg) Feature1
Colorizes a selected object red or green. For demonstration how to write a workbench feature.

#### Parameters
- Base: The object to colorize
- Green: if True, the linked object will be colored green, otherwise red.


## Discussion
Please offer feedback or connect with the developer via the [dedicated FreeCAD forum thread](LINK).

## License
GNU Lesser General Public License v3.0
