import os

# Updating pip, the system and downloading necessary packages
def pip():
    print("\nEnter your password to update your system and install the required packages:")
    os.system("sudo apt update")
    os.system("sudo apt install python3 -y")
    os.system("sudo apt install python3.7 -y")
    os.system("sudo apt install python3-pip -y")
    os.system("sudo apt install python3-venv -y")
    os.system("sudo apt install virtualenv -y")
    os.system("pip3 install selenium")
    os.system("clear")

with open(os.path.expanduser("~/.bashrc"), "r") as f:
    name = f.read()
    bash_array = name.splitlines()
    f.close()

alias = "alias make_project='var1=$(locate Sajt.sh);" + ' "$var1"' + "'" 

bash_new = open(os.path.expanduser("~/.bashrc"), "a+")

new_string = "\n# Custom aliases" + "\n" + alias
for lines in bash_array:
    if (lines == "# Custom aliases" or lines == alias):
        pass
    else:
        bash_new.write(new_string)
        break

bash_new.flush()
bash_new.close()
os.system("clear")