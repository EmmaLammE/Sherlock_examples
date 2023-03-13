# Run faster on Sherlock
This is a tutorial of how to manage and submit jobs on Sherlock, prepared for SIGMA group meeting on 03/15/2023.

## Connecting to Sherlock
### ssh
For Mac user, open up terminal, and login using the following command. Your sunit is whatever letter/number combination that you have for your Stanford email.
```
ssh [your_sunit]@sherlock.stanford.edu
```
For Windows user, sorry. Usually you can use Cygwin or WSL.


## .bashrc file

.bashrc is a Bash shell script that Bash runs whenever it is started interactively. It initializes an interactive shell session. You can put any command in that file that you could type at the command prompt.

You put commands here to set up the shell for use in your particular environment, or to customize things to your preferences. A common thing to put in .bashrc are aliases that you want to always be available.

For example, if your program requires loading several modules, or requires specifying some paths, you can put those commands in the .bashrc file. In this way, you don't have to keep repeating the same commands everytime you login. An example .bashrc is shown below. In this file, we load the python modules and export a path variable for ISPC.
```
ml python
export PATH=$PATH:${HOME}/Downloads/ispc-v1.18.0-linux/bin
```

