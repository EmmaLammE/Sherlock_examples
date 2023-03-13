# Run faster on Sherlock
This is a tutorial of how to manage and submit jobs on Sherlock, prepared for SIGMA group meeting on 03/15/2023.

## Connecting to Sherlock
### ssh
For Mac users, open up terminal, and login using the following command. Your sunit is whatever letter/number combination that you have for your Stanford email.
```
ssh [your_sunit]@sherlock.stanford.edu
```
For Windows user, sorry. Usually you can use Cygwin or WSL.

### Web browser

The Sherlock OnDemand interface allows you to conduct your research on Sherlock through a web browser. Once you login, you will see something like this

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/9de664de54b78ea9bf046dd271d6c2e9b40abf32/readme_imag/ondemand_joblist.png" width="800">

This allows you to further access, modify and run jobs on Sherlock. For example, you can check the status of your submitted jobs (explained below) by clicking ```jobs -> active jobs```, and you will see something like this

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/9de664de54b78ea9bf046dd271d6c2e9b40abf32/readme_imag/ondemand_joblist.png" width="800">

More info can be found here: [https://www.sherlock.stanford.edu/docs/user-guide/ondemand/](https://www.sherlock.stanford.edu/docs/user-guide/ondemand/)

## .bashrc file

.bashrc is a Bash shell script that Bash runs whenever it is started interactively. It initializes an interactive shell session. You can put any command in that file that you could type at the command prompt.

You put commands here to set up the shell for use in your particular environment, or to customize things to your preferences. A common thing to put in .bashrc are aliases that you want to always be available.

For example, if your program requires loading several modules, or requires specifying some paths, you can put those commands in the .bashrc file. In this way, you don't have to keep repeating the same commands everytime you login. An example .bashrc is shown below. In this file, we load the python modules and export a path variable for ISPC.

```
ml python
export PATH=$PATH:${HOME}/Downloads/ispc-v1.18.0-linux/bin
```

## Sherlock file system
When you log onto Sherlock, you are automatically put into your home directory ```/home/users/[your_sunit]``` with a login node. (meaning that it is not meant for computation!). Home directory's storage is very low (15 GB), you may want to go to other directories for compuation. A summary of different directories is shown below.

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/9e2582c7fcc89b4f160dd768ab2e6974603396bb/readme_imag/sher_dir_summ.png" width="500">

**Sherlock is for computation, not storage!**




## Clone your repo

In this tutorial, we are using the Sherlock_example repo. Copy paste the following command into your bash
```
git clone https://github.com/EmmaLammE/Sherlock_examples.git
```


