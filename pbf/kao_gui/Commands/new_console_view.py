from pbf.helpers.filename_helper import GetPythonClassnameFromFilename

from pbf.Commands import command_manager
from pbf.templates import template_manager
from pbf.kao_gui.templates import TemplatesRoot

class NewConsoleView:
    """ Creates a new Console View """
    category = "new"
    command = "cns-view"
    description = "Creates a new Console View"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Create the Console View """
        viewFileName = args[0]
        viewName = GetPythonClassnameFromFilename(viewFileName)
        print "Creating Console View:", viewName, "at:", viewFileName
        self.createView(viewFileName, viewName)
        
    def createView(self, viewFileName, viewName):
        """ Create the controller file """
        template_manager.CopyTemplate(viewFileName, "console_view.py", {"%ViewName%":viewName}, TemplatesRoot)
    
    def help(self):
        """  """
        print "Usage: pbf {category} {command} [path/to/view]".format(category=self.category, command=self.command)
        print "\tWill create a Console View at the path given"
    
command_manager.RegisterCommand(NewConsoleView)