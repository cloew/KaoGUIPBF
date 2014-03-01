from pbf.Commands import command_manager

from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf.python.helpers.python_helper import GetPythonImportString

from pbf.templates import template_manager
from pbf.kao_gui.templates import TemplatesRoot

class NewPygameController:
    """ Command to Create a new Pygame Controller """
    category = "new"
    command = "pygame-ctrl"
    description = "Creates a new Pygame Controller"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        controllerFileName = args[0]
        controllerName = GetPythonClassnameFromFilename(controllerFileName)
        print "Creating Pygame Controller:", controllerName, "at:", controllerFileName
        self.createController(controllerFileName, controllerName)
        
    def createController(self, controllerFileName, controllerName):
        """ Create the controller file """
        viewName = controllerName.replace("Controller", "Screen")
        viewFileName = controllerFileName.replace("controller", "screen")
        keywords = {"%ControllerName%":controllerName,
                    "%ViewName%":viewName,
                    "%ViewImport%":GetPythonImportString(viewFileName, [viewName])}
        template_manager.CopyTemplate(controllerFileName, "pygame_controller.py", keywords, TemplatesRoot)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/controller]".format(category=self.category, command=self.command)
        print "\tWill create a Pygame Controller at the path given"
    
command_manager.RegisterCommand(NewPygameController)