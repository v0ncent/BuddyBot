# Vincent Banks
# ---BuddyBot CommandManager---
class CommandObj:  # create command object
    def __init__(self, command_name: str, get_help: str):
        self.command_name = command_name
        self.get_help = get_help

    def get_instance(self):
        return self


def add_command(command: CommandObj, command_list: [CommandObj]):
    for cmd in command_list:
        if command.command_name == command_list[cmd].command_name:
            raise ValueError(f'Command {command.command_name} Already Present!')
        command_list.append(command)
