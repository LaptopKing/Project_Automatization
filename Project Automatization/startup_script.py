import os

with open(os.path.expanduser("~/.bashrc"), "r") as f:
    name = f.read()
    bash_array = name.splitlines()
    f.close()

alias = "alias make_project='var1=$(locate Sajt.sh);" + '"$var1"'

bash_new = open(os.path.expanduser("~/.bashrc"), "a+")

new_string = "\n# Custom aliases" + "\n" + alias
is_or_not = False
for lines in bash_array:
    if (lines == "# Custom aliases" or lines == alias):
        is_or_not = False
    else:
        is_or_not = True

if (is_or_not == True):
    bash_new.write(new_string)

bash_new.flush()
bash_new.close()
os.system("clear")