import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GitHub_and_Setup():
    # Updating pip, the system and downloading necessary packages
    @staticmethod
    def pip():
        print("\nEnter your password to update your system and install the required packages:")
        os.system("sudo apt update")
        os.system("sudo apt install python3 -y")
        os.system("sudo apt install python3.7 -y")
        os.system("sudo apt install python3-pip -y")
        os.system("pip3 install selenium")
        os.system("clear")


    # Open google and create new repository in GitHub
    @staticmethod
    def web():
        operadriver_path = os.popen('locate /Project_Automatization/Project\ Automatization/operadriver').read()
        operadriver_path = operadriver_path[:-1]
        os.system("chmod 777 " + '"' +  operadriver_path + '"')
        variables = GitHub_and_Setup().git_hub()
        username_slash_email = input("\nEnter your username or email address: ")
        password = input("Enter your password: ")
        driver = webdriver.Opera(executable_path=operadriver_path)
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

        sleep(0.5)

        element = driver.find_element_by_xpath('//*[@id="empty-setup-new-repo-echo"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

        commands_to_run = element.text
        commands_to_run = commands_to_run.splitlines()
        
        # There is 7 lines with the 0 starting index
        
        if (variables[1] == True):
            os.system(commands_to_run[0])
        else:
            pass
        
        os.system("pwd")

        sleep(5)
        
        # if (variables[2] == True):
            


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

git = GitHub_and_Setup()

git.web()