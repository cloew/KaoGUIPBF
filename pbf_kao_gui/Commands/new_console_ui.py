from pbf.helpers.filename_helper import RemoveFileExtension, GetPythonClassnameFromFilename

from new_console_controller import NewConsoleController
from new_console_view import NewConsoleView


class NewConsoleUI:
    """ Creates a new Console Controller & View """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new console controller & view')
    
    def run(self, arguments):
        """ ADD LOGIC TO RUN THE PACKAGE HERE """
        filename = RemoveFileExtension(arguments.destination)
        uiName = GetPythonClassnameFromFilename(filename)
        print "Creating Console Controller & View:", uiName
        
        consoleViewCommand = NewConsoleView()
        consoleControllerCommand = NewConsoleController()
        
        consoleViewCommand.createView(filename+"_screen.py", uiName+"Screen")
        consoleControllerCommand.createController(filename+"_controller.py", uiName+"Controller")
