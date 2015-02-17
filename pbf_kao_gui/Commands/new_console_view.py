from pbf.helpers.filename_helper import GetPythonClassnameFromFilename

from pbf.templates.template_loader import TemplateLoader
from pbf_kao_gui.templates import TemplatesRoot

class NewConsoleView:
    """ Creates a new Console View """
    TEMPLATE_LOADER = TemplateLoader("console_view.py", TemplatesRoot)
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new console view')
    
    def run(self, arguments):
        """ Create the Console View """
        viewFileName = arguments.destination
        viewName = GetPythonClassnameFromFilename(viewFileName)
        print "Creating Console View:", viewName, "at:", viewFileName
        self.createView(viewFileName, viewName)
        
    def createView(self, viewFileName, viewName):
        """ Create the controller file """
        self.TEMPLATE_LOADER.copy(viewFileName, keywords={"%ViewName%":viewName})
