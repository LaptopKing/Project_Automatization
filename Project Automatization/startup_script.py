import os
print("Hello World")

with open(os.path.expanduser("~/.bashrc"), "r") as f:
    name = f.read()
    bash_array = name.splitlines()

print(bash_array)
print(len(bash_array))
"""
g = 0
minus_length = len(bash_array) - 2

alias = "alias make_project='var1=$(locate Sajt.sh); cd" + "$var1" + "; ./Sajt.sh; cd -'"
for g in range(len(bash_array)):
    if (bash_array[g] != "# Custom aliases" and g >= minus_length):
        bash_array.append("\n# Custom aliases")
    elif (bash_array[g] != alias and g >= minus_length):
        bash_array.append("\n" + alias)

    print(bash_array[g])

new_string = ""
for lines in bash_array:
    new_string = lines

bash_new = open(os.path.expanduser("~/.bashrc"), "w")
bash_new.write(new_string)
bash_new.flush()
bash_new.close()
os.system("clear")
"""