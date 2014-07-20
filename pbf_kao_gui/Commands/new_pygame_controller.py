from pbf.Commands import command_manager

from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf_python.helpers.python_helper import GetPythonImportString

from pbf.templates import template_manager
from pbf_kao_gui.templates import TemplatesRoot

class NewPygameController:
    """ Command to Create a new Pygame Controller """
    category = "new"
    command = "pygame-ctrl"
    description = "Creates a new Pygame Controller"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new pygame controller')
    
    def run(self, arguments):
        """ Run the command """
        controllerFileName = arguments.destination
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