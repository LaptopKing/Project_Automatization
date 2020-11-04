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
            pass

    # Setting up the python3 virtual environment in the project folder
    @staticmethod
    def python():
        folder_name = project_folder_making().project_path()
        python_version = platform.python_version()
        python_version = float(python_version[:-2])

        if (python_version <= 3.7):
            os.system("python3 -m venv " + folder_name + "/venv")
            # os.system("source " + folder_name + "/venv/bin/active") # not working properly, because it is not possible
        else:
            os.system("virtualenv " + folder_name + "/venv")
            # os.system("source " + folder_name + "/venv/bin/active") # not working properly, because it is not possible

folder = project_folder_making()

folder.project_type()