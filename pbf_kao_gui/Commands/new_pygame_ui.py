from pbf.Commands import command_manager
from pbf.helpers.filename_helper import RemoveFileExtension, GetPythonClassnameFromFilename

from new_pygame_controller import NewPygameController
from new_pygame_screen import NewPygameScreen

class NewPygameUI:
    """ Creates a new Pygame Controller & Screen """
    category = "new"
    command = "pygame-ui"
    description = "Crates a new Pygame UI controller and screen"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        filename = RemoveFileExtension(args[0])
        uiName = GetPythonClassnameFromFilename(filename)
        print "Creating Pygame Controller & View:", uiName
        
        pygameScreenCommand = NewPygameScreen()
        pygameControllerCommand = NewPygameController()
        
        pygameScreenCommand.createScreen(filename+"_screen.py", uiName+"Screen")
        pygameControllerCommand.createController(filename+"_controller.py", uiName+"Controller")
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/ui]".format(category=self.category, command=self.command)
        print "\tWill create a Pygame Controller & Screen at the path given"
    
command_manager.RegisterCommand(NewPygameUI)