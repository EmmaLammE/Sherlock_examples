# Run faster on Sherlock
This is a tutorial of how to manage and submit jobs on Sherlock, prepared for SIGMA group meeting on 03/15/2023.

## Connecting to Sherlock
### ssh
For Mac users, open up terminal, and login using the following command. Your sunit is whatever letter/number combination that you have for your Stanford email.
```
ssh [your_sunit]@sherlock.stanford.edu
```
For Windows users, sorry. Usually you can use Cygwin or WSL.

### Web browser

The Sherlock OnDemand interface allows you to conduct your research on Sherlock through a web browser. Once you login, you will see something like this

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/9996ae793113912b9f0ab0b37bda3a6b8ff7691b/readme_imag/ondemand_login.png" width="800">

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

## Sherlock system
### File system
When you log onto Sherlock, you are automatically put into your home directory ```/home/users/[your_sunit]``` with a login node. (meaning that it is not meant for computation!). Home directory's storage is very low (15 GB), you may want to go to other directories for compuation. A summary of different directories is shown below.

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/9e2582c7fcc89b4f160dd768ab2e6974603396bb/readme_imag/sher_dir_summ.png" width="500">

**Sherlock is for computation, not storage!**

### User limits
A summary of user limits is shown below.

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/7f3f2ba5875ee30db4d72ad38e56a5f79086693c/readme_imag/sher_user_limits.png" width="600">

* MaxTRESPU: max number of CPUs/GPUs one user can use
* MaxTRESPA: max number of CPUs/GPUs one group can use
* MaxSubmitPU: max number of jobs one user can submit
* MaxSubmitPA: max number of jobs one group can submit
* MaxWall: max time one job can run

More info of file system and user limits can be found here: [https://www.sherlock.stanford.edu/docs/storage/#features-and-purpose](https://www.sherlock.stanford.edu/docs/storage/#features-and-purpose)

### Partitions
Partition is set of compute nodes on Sherlock will you run on. A summary of partitions is shown below.

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/0f4ae4ff7699e6d1175dd8c25b6d79ccea548350/readme_imag/sher_partition.png" width="1200">

## Example to modify and submit a job on Sherlock
### Login to Sherlock
```
ssh [your_sunit_id]@sherlock.stanford.edu
```

### Clone the repo onto Sherlock
In your own research, you want to clone your program onto Sherlock. In this tutorial, we are using the Sherlock_example repo. Copy paste the following command into your bash
```
git clone https://github.com/EmmaLammE/Sherlock_examples.git
```
### Choose a code editor
After you have the codes ready on Sherlock, you want to read the codes comfortably and modify them efficiently, especially when you need to debug a bit on Sherlock. Image this work flow: 

Have the codes ready on Sherlock -> Run the codes -> You find a bug or need to change a parameter -> Modify your codes -> Run it again. 

Here at step 4, there are 3 routes to go: 

**a.** you can change your codes directly on Sherlock; **b.** you change your codes locally on your personal computer, then git push to remote, then git pull on Sherlock; **c.** you can mount the Sherlock folder onto your personal computer. 

Depending on what route you choose, there are various way to choose codes editor. Here, I only briefly summarize the ones that I used before.

* vim: good for remote editting. Fast, efficient text editing. Need to memorize some commands;
* VSCode: beginner friendly. It can connect to remote server directly. (But recently cannot connect to Sherlock for unknow reasons);
* Sublime text: just a text editor, similar to VSCode, but with less build in extensions. Also it cannot connect to remote server;
* sshfs + codes editor: easy to use once setup. No need to clone any codes on personal computer. No need to worry about version control. But it requires changing system security settings to enable system extensions.

### Run on a computation node
If you want to run something directly in the console, first you need to request a computational node by running the following command. (Remember that if you just do ssh [your_sunit_id]@sherlock.stanford.edu, it only takes you to a login node). This will lead you to an interactive session and resources, which is useful for debugging.
```
srun -c 2 --mem=32GB --pty --partition=serc --time=01:00:00 bash
```

The above command requires a 1 hour interative session with 2 CPUs, 32 GB memories on serc partition. 

The you can run the codes directly in the console. For example, 
```
python large_add.py
```

### Run by sbatch
Another way to run a program is to schedule batch jobs. Then script is submitted to and executed by the scheduler (Slurm). Remember to carefully request the computing power. If you request more computing powers than you need , e.g. request 100 CPUs when you actually only need 10, the waiting time is long. For example, for the same addition program in python, you may have a sbatch file looking something like this.
```
#!/bin/bash
#SBATCH --job-name=test
#SBATCH --time=00:10:00
#SBATCH --mem=10GB
#SBATCH -p serc
#SBATCH -c 2
#SBATCH -o out_%j.out
#SBATCH -e err_%j.err

# below you run/call your code, load modules, python, Matlab, R, etc.
# and do any other scripting you want
# lines that begin with #SBATCH are directives (requests) to the scheduler-SLURM module load python/3.6.1
python large_add.py
```

In the sbatch file, you tell the scheduler what resources your job needs and how long it should run. It should be a close estimate. For example, in the above, we estimate our program is going to need 10 GB memory and it takes about 10 minutes to complete. We further place it on serc partition and request 2 CPUs to run the program. In addition, we save the err and output as separate files using the ```-o``` and ```-e```.

After you submit, you can check the status of your job by the following command
```
squeue -u [your_sunit_id]
```
