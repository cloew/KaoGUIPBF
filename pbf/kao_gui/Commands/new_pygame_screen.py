from pbf.Commands import command_manager

from pbf.helpers.filename_helper import GetPythonClassnameFromFilename

from pbf.templates import template_manager
from pbf.kao_gui.templates import TemplatesRoot

class NewPygameScreen:
    """ Command to Create a new Pygame Screen """
    category = "new"
    command = "pygame-screen"
    description = "Creates a new Pygame Screen"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        screenFileName = args[0]
        screenName = GetPythonClassnameFromFilename(screenFileName)
        print "Creating Pygame Screen:", screenName, "at:", screenFileName
        self.createScreen(screenFileName, screenName)
        
    def createScreen(self, screenFileName, screenName):
        """ Create the widget file """
        template_manager.CopyTemplate(screenFileName, "pygame_screen.py", {"%ScreenName%":screenName}, TemplatesRoot)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command}} [path/to/widget]".format(category=self.category, command=self.command)
        print "\tWill create a Pygame Screen at the path given"
    
command_manager.RegisterCommand(NewPygameScreen)