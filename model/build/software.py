import shell
import os
import sys
sys.path.append("...")  # set all imports to root imports


def installSoftware(software):
    """
    Install arbitrary software based on a software object
    """
    packagelist = ""
    for package in software.packages:
        packagelist += package + " "
    return [software.installer + " " + packagelist]
