from rich.console import Console
import platform
import cpuinfo
import os
import time

console = Console()

def selectionComponent(informList):  #the function of selecting the desired components
    infoList(informList)
    console.print("[i]Just write the value you want to select. [bold red]Only one at a time[/]")
    inputLetter = console.input("[bold red]Enter[/] [i]your[/] value: ")
   
    try:
        if inputLetter == "y":
            return informList
        elif informList[inputLetter] == True:
            informList.update({inputLetter: False})
        elif informList[inputLetter] == False:
            informList.update({inputLetter:True})
    except KeyError:
        console.print("Oopps...:monkey: [bold red]You entered an invalid value[/] \n [bold green]Try again![/]")
    selectionComponent(informList)

def status(inputValue):  #Writes the selection status
    if inputValue == True:
        status = ("[yes]")
    elif inputValue == False:
        status =("[no]")
    return status

def infoList(informList):  #information output
    console.rule("[bold red]InformList")
    print ("\n a) CPU Name;", status(informList["a"]),"\n",
    "b) CPU architecture;", status(informList["b"]),"\n",
    "c) System name;", status(informList["c"]),"\n",
    "d) Network name;", status(informList["d"]),"\n",
    "e) System release;", status(informList["e"]),"\n",
    "f) System version;", status(informList["f"]),"\n",
    "g) Type of machine;", status(informList["g"]),"\n",
    "h) Python version;", status(informList["h"]),"\n",
    "i) Python build;", status(informList["i"]),"\n",
    "j) Python compiler;", status(informList["j"]),"\n",
    )
    console.print(" y) [bold green]Proceed")
    console.rule("[bold red]InformList")

def dictionaryNew():
    informList = {
        "a": False, #CPU Name
        "b": False, #CPU architecture
        "c": False, #System name
        "d": False, #Network name
        "e": False, #System release
        "f": False, #System version
        "g": False, #Type of machine
        "h": False, #Python ver
        "i": False, #Python buid
        "j": False, #Python compiler
    }
    return informList

def deleteFile():
    if os.path.exists(r"c:\Users\777\NG_2022_Alexandr_Malina\Lesson_4\InfoAboutPC.txt"):
        os.remove(r"c:\Users\777\NG_2022_Alexandr_Malina\Lesson_4\InfoAboutPC.txt")

def createFile():
    datafile = open(r"c:\Users\777\NG_2022_Alexandr_Malina\Lesson_4\InfoAboutPC.txt", "w")
    return datafile

def writeToFile(informList):
    with console.status("Now everything will...I guess", spinner="monkey"):
        deleteFile()
        datafile = createFile()
        my_cpuinfo = cpuinfo.get_cpu_info()
        for x in informList.items():
            x = str(x)
            match x: 
                case "('a', True)":
                    datafile.write(f"Full CPU Name: {my_cpuinfo['brand_raw']}" + "\n")
                case "('b', True)":
                    datafile.write(f"CPU architecture: {my_cpuinfo['arch']}" + "\n")
                case "('c', True)":
                    datafile.write(f"System name: {platform.system()}" + "\n")
                case "('d', True)":
                    datafile.write(f"Network name: {platform.node()}" + "\n")
                case "('e', True)":
                    datafile.write(f"System release: {platform.node()}" + "\n")
                case "('f', True)":
                    datafile.write(f"System version: {platform.version()}" + "\n")
                case "('g', True)":
                    datafile.write(f"System version: {platform.machine()}" + "\n")
                case "('h', True)":
                    datafile.write(f"Python version: {platform.python_version()}" + "\n")
                case "('i', True)":
                    datafile.write(f"Python buid(num and date): {platform.python_build()}" + "\n")
                case "('j', True)":
                    datafile.write(f"Python compiler: {platform.python_compiler()}" + "\n")
        datafile.close()

def main():
    informList = dictionaryNew()
    selectionComponent(informList)
    writeToFile(informList)

    console.rule("[bold red]Result")
    console.print("[bold green]Great, [i]it's working![/][/] File ready and you can see [i]it![/]")
    choice = console.input("You wanna try [bold red]again[/]? :smiley: (y-yeah, n-no): ")

    if choice == "y":
        main()
    else:
        with console.status("Have a good day...", spinner="monkey"):
            time.sleep(5)   

main()
