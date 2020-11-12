import os

with open(os.path.expanduser("~/.bashrc"), "r") as f:
    name = f.read()
    bash_array = name.splitlines()
    f.close()

alias = "alias make_project='var1=$(locate Sajt.sh);" + '"$var1"'

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