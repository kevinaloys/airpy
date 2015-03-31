import click
from airpy.install import airinstall
from airpy.list import print_list
from airpy.start import airstart
from airpy.remove import airremove
from airpy.autopilot import airautopilot

"""
   
"""
def main():

    @click.group()
    def airpy():
        """AirPy : Documentation Installer for the Pythonic Soul"""
        pass

    """

    """
    @airpy.command(help='Install offline doc of a Python module.')
    @click.argument('name')
    def install(name):
        airinstall(name)

    """

    """
    @airpy.command(help='Start a doc in a browser.')
    @click.argument('name')
    def start(name):
        airstart(name)

    """

    """
    @airpy.command(help='Remove an installed doc.')
    @click.argument('name', nargs = -1)
    def remove(name):
        airremove(name)


    """

    """
    @airpy.command(help='List installed docs.')
    def list():
        print_list()

    """

    """
    @airpy.command(help='Auto install docs.')
    def autopilot():
        airautopilot()


    """

    """
    @airpy.command(help='Show information about installed doc.')
    @click.argument('name')
    def show():
        airshow(name)


    airpy()

if __name__ == '__main__':
    main()
