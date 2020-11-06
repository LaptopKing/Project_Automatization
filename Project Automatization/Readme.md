# Tips and help for virtual environment

To run the 'base.py' file in a virtual environment extract the 'venv.zip' file and the in the command line and in the right folder called './Project_Automatization/Project Automatization' run 'source venv/bin/activate'. 

(The '.' before '/Project_Automatization' is symbolising the folder where you saved/cloned the git repository!)

## Easier run for the script

To set up this, it can be a little more complicated than the above one, but it will be easier to use later on for sure! 

Follow these steps:
- In the linux terminal enter:
        ```html
        nano ~/.bashrc
        ```
>       After you ran this code you should see a text editor in your terminal! Now scroll all the way down and paste the code belove!
- The following step goes as this:
        ```html
        # Custom aliases
        alias make_project='cd ~; ./Programming\ Projects/Project_Automatization/Project\ Automatization/Run.sh; cd -'
        ```
>       Note that the above commands are only for to make it more easy to use, after you completed these steps you will only need to type 'make_project' and the whole program will start automaticly and will guide you further to create your amazing project!