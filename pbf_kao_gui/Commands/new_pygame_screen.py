
from pbf.helpers.filename_helper import GetPythonClassnameFromFilename

from pbf.templates import template_manager
from pbf_kao_gui.templates import TemplatesRoot

class NewPygameScreen:
    """ Command to Create a new Pygame Screen """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new pygame screen')
    
    def run(self, arguments):
        """ Run the command """
        screenFileName = arguments.destination
        screenName = GetPythonClassnameFromFilename(screenFileName)
        print "Creating Pygame Screen:", screenName, "at:", screenFileName
        self.createScreen(screenFileName, screenName)
        
    def createScreen(self, screenFileName, screenName):
        """ Create the widget file """
        template_manager.CopyTemplate(screenFileName, "pygame_screen.py", {"%ScreenName%":screenName}, TemplatesRoot)
