import os
import platform

class project_folder_making:
    # Setting up project folder
    @staticmethod
    def project_path():
        path = input("\nEnter the path for your 'Programs' folder and the name of the 'Project Folder': ")
        decision = False
        while (decision != True):
            try:
                os.system("mkdir " + path)
                decision = True
            except:
                print("\nNOT correct PATH, Enter it again: ")
                path = input("\nEnter the path for your 'Programs' folder and the name of the 'Project Folder': ")
        
        return path


    # Choosing the project type and environment
    @staticmethod
    def project_type():
        p_type = input("Enter the programming language you'll use [p = python3, c# = C#, web = web development (full frontend setup), f = flutter]: ")
        if (p_type == "p"):
            project_folder_making().python()
        elif (p_type == "c#"):
            project_folder_making().c_sharp()
        elif (p_type == "web"):
            pass
            


    # Setting up the python3 virtual environment in the project folder
    @staticmethod
    def python():
        folder_name = project_folder_making().project_path()
        python_version = platform.python_version()
        python_version = float(python_version[:-2])

        if (python_version <= 3.7):
            os.system("python3 -m venv " + folder_name + "/venv")
            os.system("touch " + folder_name + "/base.py")
            os.system("chmod a+x " + folder_name + "/base.py")
            # os.system("source " + folder_name + "/venv/bin/active") # not working properly, because it is not possible
        else:
            os.system("virtualenv " + folder_name + "/venv")
            os.system("touch " + folder_name + "/base.py")
            os.system("chmod a+x " + folder_name + "/base.py")
            # os.system("source " + folder_name + "/venv/bin/active") # not working properly, because it is not possible

    # Setting up the C# project whether it's a Wpf app or a Console app 
    @staticmethod
    def c_sharp():
        folder_name = project_folder_making().project_path()
        c_sharp_type = input("Choose between console and GUI project [c = console, wpf = GUI]: ")

        if (c_sharp_type == "c"):
            os.system("rsync -avz ./C#/Console/ " + folder_name)
        elif (c_sharp_type == "wpf"):
            os.system("rsync -avz ./C#/Wpf/ " + folder_name)

    # Setting up Front-End Web Dev project a.k.a HTML, CSS, Javascript
    def web():
        folder_name = project_folder_making().project_path()
        os.system("rsync -avz ./Web_Dev/ " + folder_name)


folder = project_folder_making()

folder.project_type()
