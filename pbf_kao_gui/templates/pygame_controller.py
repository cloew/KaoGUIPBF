%ViewImport%
from kao_gui.pygame.pygame_controller import PygameController

class %ControllerName%(PygameController):
    """ Controller for a *** """
    
    def __init__(self):
        """ Initialize the *** Controller """
        screen = %ViewName%()
        PygameController.__init__(self, screen)