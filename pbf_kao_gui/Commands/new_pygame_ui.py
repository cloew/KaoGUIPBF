from pbf.helpers.filename_helper import RemoveFileExtension, GetPythonClassnameFromFilename

from new_pygame_controller import NewPygameController
from new_pygame_screen import NewPygameScreen

class NewPygameUI:
    """ Creates a new Pygame Controller & Screen """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new pygame controller & view')
    
    def run(self, arguments):
        """ Run the command """
        filename = RemoveFileExtension(arguments.destination)
        uiName = GetPythonClassnameFromFilename(filename)
        print "Creating Pygame Controller & View:", uiName
        
        pygameScreenCommand = NewPygameScreen()
        pygameControllerCommand = NewPygameController()
        
        pygameScreenCommand.createScreen(filename+"_screen.py", uiName+"Screen")
        pygameControllerCommand.createController(filename+"_controller.py", uiName+"Controller")
