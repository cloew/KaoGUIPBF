from pbf.helpers.filename_helper import GetPythonClassnameFromFilename

from pbf.templates.template_loader import TemplateLoader
from pbf_kao_gui.templates import TemplatesRoot

class NewPygameScreen:
    """ Command to Create a new Pygame Screen """
    TEMPLATE_LOADER = TemplateLoader("pygame_screen.py", TemplatesRoot)
    
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
        self.TEMPLATE_LOADER.copy(screenFileName, keywords={"%ScreenName%":screenName})
