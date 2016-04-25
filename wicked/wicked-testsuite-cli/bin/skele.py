"""
skele

Usage:
  skele hello
  skele -h | -help
  skele -version

Options:
  -h -help                         Show this screen.
  -version                         Show version.

Examples:
  skele hello


"""


from inspect import getmembers, isclass

from docopt import docopt

#import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import commands
    options = docopt(__doc__, version="0.0.0.1")

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for k, v in options.iteritems():
        if hasattr(commands, k):
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()