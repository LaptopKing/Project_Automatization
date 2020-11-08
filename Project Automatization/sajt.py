import os
import platform
import pip
from selenium import webdriver

driver = webdriver.Opera(executable_path="operadriver")
driver.get("www.google.com")

installed_packages = pip.get_installed_distributions()
flat_installed_packages = [package.project_name for package in installed_packages]

class project_folder_making:

    # Setting up project folder
    @staticmethod
    def project_path():
        path = input("\nEnter the path for your 'Programs' folder and the name of the 'Project Folder'\
            \n[Full path needed and a new folder name where all your files are going]\
            \n[For example: /home/username/path/to/go/new_folder_name]\n: ")
        
        os.mkdir(path)

        return path

    # Opening up the terminal, file manager and VS Code with the given path
    @staticmethod
    def opening_system(folder_name):
        os.system("gnome-terminal --working-directory=" + folder_name)
        os.system("gnome-open " + folder_name)
        os.system("code " + folder_name)


    # Choosing the project type and environment
    @staticmethod
    def project_type():
        p_type = input("\nEnter the programming language you'll use!\n[p = python3, c# = C#, web = web development (full frontend setup), f = flutter]: ")
        if (p_type == "p"):
            project_folder_making().python()
        elif (p_type == "c#"):
            project_folder_making().c_sharp()
        elif (p_type == "web"):
            project_folder_making().web()
        elif (p_type == "f"):
            project_folder_making().flutter()

    # Github repository set up.
    @staticmethod
    def git_hub():


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
            project_folder_making().opening_system(folder_name)

        else:
            os.system("virtualenv " + folder_name + "/venv")
            os.system("touch " + folder_name + "/base.py")
            os.system("chmod a+x " + folder_name + "/base.py")
            project_folder_making().opening_system(folder_name)

    # Setting up the C# project whether it's a Wpf app or a Console app 
    @staticmethod
    def c_sharp():
        folder_name = project_folder_making().project_path()
        c_sharp_type = input("Choose between console and GUI project [c = console, wpf = GUI]: ")

        if (c_sharp_type == "c"):
            try:
                os.chdir(folder_name)
                os.system("dotnet new console")
                project_folder_making().opening_system(folder_name)
            except:
                print("\nBefore using flutter, you should set it up by the guide given in the 'README.md' in the base folder of 'Project_Automatization'")

        elif (c_sharp_type == "wpf"):
            try:
                os.chdir(folder_name)
                os.system("dotnet new wpf")
                project_folder_making().opening_system(folder_name)
            except:
                print("\nBefore using flutter, you should set it up by the guide given in the 'README.md' in the base folder of 'Project_Automatization'")

    # Setting up Front-End Web Dev project a.k.a HTML, CSS, Javascript
    @staticmethod
    def web():
        folder_name = project_folder_making().project_path()
        os.system("rsync -avz ./Web_Dev/ " + folder_name)
        project_folder_making().opening_system(folder_name)

    # Setting up Flutter (Android) project
    @staticmethod
    def flutter():
        try:
            folder_name = project_folder_making().project_path()
            os.system("flutter create " + folder_name)
            project_folder_making().opening_system(folder_name)
        except:
            print("\nBefore using flutter, you should set it up by the guide given in the 'README.md' in the base folder of 'Project_Automatization'")


folder = project_folder_making()

folder.project_type()
