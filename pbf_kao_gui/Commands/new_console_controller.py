
from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf_python.helpers.python_helper import GetPythonImportString

from pbf.templates import template_manager
from pbf_kao_gui.templates import TemplatesRoot

class NewConsoleController:
    """ Creates a new Console Controller """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new console view')
    
    def run(self, arguments):
        """ ADD LOGIC TO RUN THE PACKAGE HERE """
        controllerFileName = arguments.destination
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
