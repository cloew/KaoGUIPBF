from pbf.Commands import command_manager

from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf_python.helpers.python_helper import GetPythonImportString

from pbf.templates import template_manager
from pbf_kao_gui.templates import TemplatesRoot

class NewConsoleController:
    """ Creates a new Console Controller """
    category = "new"
    command = "cns-ctrl"
    description = "Creates a new Console Controller"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ ADD LOGIC TO RUN THE PACKAGE HERE """
        controllerFileName = args[0]
        controllerName = GetPythonClassnameFromFilename(controllerFileName)
        print "Creating Console Controller:", controllerName, "at:", controllerFileName
        self.createController(controllerFileName, controllerName)
        
    def createController(self, controllerFileName, controllerName, ):
        """ Create the controller file """
        viewName = controllerName.replace("Controller", "Screen")
        viewFileName = controllerFileName.replace("controller", "screen")
        keywords = {"%ControllerName%":controllerName,
                    "%ViewName%":viewName,
                    "%ViewImport%":GetPythonImportString(viewFileName, [viewName])}
        template_manager.CopyTemplate(controllerFileName, "console_controller.py", keywords, TemplatesRoot)
    
    def help(self):
        """  """
        print "Usage: pbf {category} {command} [path/to/controller]".format(category=self.category, command=self.command)
        print "\tWill create a Console Controller at the path given"
    
command_manager.RegisterCommand(NewConsoleController)