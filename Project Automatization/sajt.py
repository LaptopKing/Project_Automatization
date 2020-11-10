import os
import platform
import pip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

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

        return p_type


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


class GitHub_and_Setup():
    # Check for pip packages and install them
    @staticmethod
    def pip():
        path = os.popen("locate sajt.py").readline()
        path = path[:-8]
        print("\nEnter your password to update your system and install the required packages:")
        os.system("sudo apt update")
        os.system("sudo apt install python3-pip")
        os.system("pip3 install selenium")
        os.system("clear")
    
    # Open google and create new repository in GitHub
    @staticmethod
    def web():
        p_type = project_folder_making().project_type()
        driver_path = os.popen("find Project\ Automatization").readline()
        variables = GitHub_and_Setup().git_hub()
        username_slash_email = input("\nEnter your username or email address: ")
        password = input("Enter your password: ")
        driver = webdriver.Opera(executable_path=driver_path)
        driver.get("https://github.com/login")
        driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(username_slash_email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]').click()

        sleep(0.5)

        driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
        driver.find_element_by_xpath('//*[@id="repository_name"]').send_keys(variables[3])
        
        if (variables[4] == ""):
            pass
        else:
            driver.find_element_by_xpath('//*[@id="repository_description"]').send_keys(variables[4])
        
        if (variables[0] == False):
            driver.find_element_by_xpath('//*[@id="repository_visibility_private"]').click()

        element = driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

        sleep(1)

        driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').send_keys(Keys.ENTER)

        sleep(5)

        element = driver.find_element_by_xpath('//*[@id="empty-setup-new-repo-echo"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        os.system(element)

        sleep(5)



        if (variables[1] == True):
            f = open ("./README.md", "w")
            f.write("# " + variables[3])
            f.write("\n")
            f.write(variables[4])
            f.flush()
            f.close()
        
        # if (variables[2] == True):
            
        
        
        sleep(5)


    # Github repository set up.
    @staticmethod
    def git_hub():
        GitHub_and_Setup().pip()
        pub_priv = True
        readme = False
        gitignore = False
        repos_name = input("Enter your repository name: ")
        description = input("Add a description (optional)\n: ")
        if (input("Select repository type [pub = Public, priv = Private]: ") == "priv"):
            pub_priv = False
        else:
            pub_priv = True
            pass

        if (input("Add README file by typing 'add': ") == "add"):
            readme = True
        else:
            readme = False
            pass

        if (input("Add .gitignore file by typing 'add': ") == "add"):
            gitignore = True
        else:
            gitignore = False
            pass
        
        return pub_priv, readme, gitignore, repos_name, description


folder = project_folder_making()

# folder.project_type()

git = GitHub_and_Setup()

# git.web()

asd = os.popen('locate operadriver').readlines()
word = ""

for f in asd:
    for i in range(f):
        
    print(f)
