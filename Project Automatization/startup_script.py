bash = open (".bashrc", "r")
bash_array = []
i = 0
for lines in bash.readlines():
    bash_array[i] = lines
    i += 1

bash.close()

line2 = "alias make_project='var1=$(locate Sajt.sh); cd" + "$var1" + "; ./Sajt.sh; cd -'"
bash_array[(len(bash_array) + 1)] += "# Custom aliases"
bash_array[(len(bash_array) + 2)] += line2
bash_new = open("~/.bashrc", "w")
bash_new.writelines(bash_array)
bash_new.flush()
bash_new.close()
os.system("clear")