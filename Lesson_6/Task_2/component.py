from dataBase import *
import platform


def checkElements(list):
    for elemenents in list:
         match elemenents: 
                case "CPU":
                    inputDataBase(Name="Full CPU name",status=str(platform.processor()))
                case "System":
                    inputDataBase(Name="System name",status=str(platform.system()))
                case "Network":
                    inputDataBase(Name="Network name",status=str(platform.node()))
                case "SysRelease":
                    inputDataBase(Name="System release",status=str(platform.node()))
                case "SysVersion":
                    inputDataBase(Name="System version",status=str(platform.version()))
                case "PythonVer":
                    inputDataBase(Name="Python Version",status=str(platform.python_version()))
                case "PythonCompiler":
                    inputDataBase(Name="Python compiler",status=str(platform.python_compiler()))