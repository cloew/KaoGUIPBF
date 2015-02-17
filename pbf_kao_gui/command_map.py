from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig("new console-controller", "pbf_kao_gui.Commands.new_console_controller.NewConsoleController", description="Creates a new Console Controller"),
            CommandConfig("new console-ui", "pbf_kao_gui.Commands.new_console_ui.NewConsoleUi", description="Crates a new Console UI controller and view"),
            CommandConfig("new console-view", "pbf_kao_gui.Commands.new_console_view.NewConsoleView", description="Creates a new Console View"),
            CommandConfig("new pygame-controller", "pbf_kao_gui.Commands.new_pygame_controller.NewPygameController", description="Creates a new Pygame Controller"),
            CommandConfig("new pygame-screen", "pbf_kao_gui.Commands.new_pygame_screen.NewPygameScreen", description="Creates a new Pygame Screen"),
            CommandConfig("new pygame-ui", "pbf_kao_gui.Commands.new_pygame_ui.NewPygameUi", description="Crates a new Pygame UI controller and screen"),
            CommandConfig("new pygame-widget", "pbf_kao_gui.Commands.new_pygame_widget.NewPygameWidget", description="Creates a new Pygame Widget")]

RegisterCommands(commands)