from pbf.helpers.filename_helper import GetPythonClassnameFromFilename

from pbf.Commands import command_manager
from pbf.templates import template_manager
from pbf.kao_gui.templates import TemplatesRoot

class NewPygameWidget:
    """ Command to construct a new Pygame Widget """
    category = "new"
    command = "pygame-widget"
    category = "new"
    description = "Creates a new Pygame Widget"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Create the Pygame Widget """
        widgetFileName = args[0]
        widgetName = GetPythonClassnameFromFilename(widgetFileName)
        print "Creating Pygame Widget:", widgetName, "at:", widgetFileName
        self.createWidget(widgetFileName, widgetName)
        
    def createWidget(self, widgetFileName, widgetName):
        """ Create the widget file """
        template_manager.CopyTemplate(widgetFileName, "pygame_widget.py", {"%WidgetName%":widgetName}, TemplatesRoot)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/widget]".format(category=self.category, command=self.command)
        print "\tWill create a Pygame Widget at the path given"
    
command_manager.RegisterCommand(NewPygameWidget)