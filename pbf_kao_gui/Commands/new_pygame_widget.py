from pbf.helpers.filename_helper import GetPythonClassnameFromFilename

from pbf.templates import template_manager
from pbf_kao_gui.templates import TemplatesRoot

class NewPygameWidget:
    """ Command to construct a new Pygame Widget """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination of the new widget')
    
    def run(self, arguments):
        """ Create the Pygame Widget """
        widgetFileName = arguments.destination
        widgetName = GetPythonClassnameFromFilename(widgetFileName)
        print "Creating Pygame Widget:", widgetName, "at:", widgetFileName
        self.createWidget(widgetFileName, widgetName)
        
    def createWidget(self, widgetFileName, widgetName):
        """ Create the widget file """
        template_manager.CopyTemplate(widgetFileName, "pygame_widget.py", {"%WidgetName%":widgetName}, TemplatesRoot)
