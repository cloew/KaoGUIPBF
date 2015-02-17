from pbf.helpers.filename_helper import GetPythonClassnameFromFilename

from pbf.templates import template_manager
from pbf_kao_gui.templates import TemplatesRoot

class NewConsoleView:
    """ Creates a new Console View """
    
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
        template_manager.CopyTemplate(viewFileName, "console_view.py", {"%ViewName%":viewName}, TemplatesRoot)
