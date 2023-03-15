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
* sshfs + codes editor: easy to use once setup. No need to clone any codes on personal computer. But it requires changing system security settings to enable system extensions.

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
Another way to run a program is to schedule batch jobs. Then script is submitted to and executed by the scheduler (Slurm). For example, for the same addition program in python, you may have a sbatch file looking something like this.
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
python some_program.py
```

In the sbatch file, you tell the scheduler what resources your job needs and how long it should run. It should be a close estimate. For example, in the above, we estimate our program is going to need 10 GB memory and it takes about 10 minutes to complete. We further place it on serc partition and request 2 CPUs to run the program. In addition, we save the err and output as separate files using the ```-o``` and ```-e```.

After you submit, you can check the status of your job by the following command.
```
squeue -u [your_sunit_id]
```

Your current jobs and their status will show as follows.

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/e2dfc04f0961b5a65d0e02a8c8ec1d6aff1ac4ea/readme_imag/sher_squeue.png" width="600">

The status R means run, PD means pending.

Remember to carefully request the computing power. If you request more computing powers than you need, e.g. request 100 CPUs when you actually only need 10, not only the waiting time is long you also takes up resources that other people could utilize.

## Small example parallel programs
We demonstrate 2 simple cases that we can utilize the parallel computing on Sherlock. First case is parallelizing a for loop, second case is to parallelizing a matrix-vector multiplication.

### Understanding dependencies
The very first thing to parallelize an existing program is to identify the inherent dependencies in your program. For example, imagine you have a sudo codes looks like the one below
```
a = 3
b = 4
c = a + b
d = 2*a + b
```
Line 3 and line 4 are independent of each other, thus these two lines can be computed simutaneuously, i.e. parallelizable. However, if the sudo codes looks like this
```
a = 3
b = 4
c = a + b
d = 2*c + b
```
Line 4 now depends on the results of line 3, thus cannot be executed until line 3 is finshed, i.e. this program is not parallelizable.

### Parallelize a for loop
For loops are probably the most common structures in all application fields regardless of the choice of languages. It is beneficial if some parts of the for loops can be parallelized. In this example, we are parallelizing the computation ```y = a*x + b```, where ```x, y``` are vectors and ```a, b``` are given constants. In most program languages, you will write something like
```
for i = 1:N
    y[i] = a*x[i] + b
```
Since computation of each element is completely independent of another, we can divided the for loop into several parts, and assign each part to a processor to do the computation. An example codes of is shown below.
```
pool = ThreadPool(2)
func = partial(some_function_call, a, b)
y = pool.map(func, x)
pool.close()
pool.join()
```
Here, we set the pool size to 2, meaning that we have 2 threads of execution. Then each worker thread gets tasks synchronously, meaning that the caller will block until the issued task or tasks have been completed. The thread pool provides a parallel version of the built-in map() function for issuing tasks. After all the threads finish their jobs, we close the pool and join all threads together. Use the following command to run the code
```
python3 par_for_loop.py
```
<!-- **Note:** The package concurrent requires python 3.8 or above. Be sure to check your python version if concurrent is reported not found. -->
The outputs with the size of the vector to be 1e7 is shown below.

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/0ff2344e3485b11a7209d3ca7f83218b4e61c43c/readme_imag/par_py_axpb.png" width="300">

As we can see, creating more threads does not increase the speed of computation. Is this because some codes we wrote were wrong? Let's try using the same parallel algorithm, but instead of computing ```y=ax+b```, we open a series of website given a set of urls. Try run 
```
python3 par_open_urls.py
```
An example output is 

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/0ff2344e3485b11a7209d3ca7f83218b4e61c43c/readme_imag/par_py_urls.png" width="400">

In case, we do see a speed up with the increasing the number of threads used. Let's find out why this is the case.

In the ```y[i]=a*x[i]+b``` example, for computation of each element in the vector, we have the following executions to do: 1 load, 1 multiplication, 1 addition, and 1 store. The computation time needed for each of the execution is different. Depending on the system you run the program on, the exact time to operate instructions will be different. But as you can imagine, 1 load usually takes a lot longer than 1 addition. For example, if 1 load takes 2 clocks, 1 store takes 2 clocks, and 1 floating point operation takes 1 clock. The arithematic intensity of ```y[i]=a*x[i]+b``` is 2/(2+4) = 1/3. This means that only 33% of the time the codes are doing useful work instead of just waiting to read/write values from memory/cache. Thus, this program is more bandwidth limited, instead of computation limited.

### Parallelize matrix multiplication
In this example, we calculate a matrix-matrix multiplication ```AB=X```. We use this to illustrate another important part in parallelizing a program - indexing. We all know that matrix multiplication requires accessing each row of A and each column of B, as shown below.

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/0ff2344e3485b11a7209d3ca7f83218b4e61c43c/readme_imag/gemm_sketch.png" width="400">

One part that always get overlooked is how we access each element in A and B. For example, in C++ the index of a matrix is oriented horizontally, as shown below on the left. For row accessing, this is fast, because we are requiring a continuous indices. But for column access, this requires a jump access with a step size of N. The jump access is slow as in the elements are stored in memory continuously. Therefore, apart from regular parallelizing schemes, we can also change the index of the second matrix B, such that the loading process is more efficient, as shown below on the right.

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/0ff2344e3485b11a7209d3ca7f83218b4e61c43c/readme_imag/par_mat_mult_sketch_B_rearrange.png" width="600">

A comparison of the performance for continuous access is shown below and jump access. The time used for non-rearranged matrix B

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/0ff2344e3485b11a7209d3ca7f83218b4e61c43c/readme_imag/gemm_B.png" width="500">

and the time used for rearranged matrix B

<img src="https://github.com/EmmaLammE/Sherlock_examples/blob/0ff2344e3485b11a7209d3ca7f83218b4e61c43c/readme_imag/gemm_B_rearrange.png" width="500">

**Note:** In order to run the this program, you need to install ISPC on your Sherlock. This the following commands to install
```
wget https://github.com/ispc/ispc/releases/download/v1.18.0/ispc-v1.18.0-linux.tar.gz
tar -xvf ispc-v1.18.0-linux.tar.gz
export PATH=$PATH:${HOME}/Downloads/ispc-v1.18.0-linux/bin
```

