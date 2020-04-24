# Follow me for this simple journey into creating a rest api using django and django rest.

# What you will need:
A version of python, I'm using 3.6.5, which isn't all that new, but its what I have installed and I'll 
change it in due time if I need to.


Vagrant - See here for installation instructions for your platform:
https://www.vagrantup.com/

VirtualBox - See here for installation instructions for that here:
https://www.virtualbox.org/

Of course Git: 
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git.

I shall be using Invoke to automate the boring stuff. See here for details:
http://docs.pyinvoke.org/en/stable/index.html

Also, for package management I'm using pipenv. See installation instructions here:
https://pipenv-fork.readthedocs.io/en/latest/

# What are the prerequisites for?
Well, we need Python to interpret the code that we are writing, I'm not
supporting legacy applications so I'm using a quite modern Python version.
 
For a clean environment, independent of all the applications, etc that I have 
on my physical machine I've decided to use Vagrant to sandbox my environment.

Vagrant is really just an API for a hypervisor, the type 2 hypervisor of choice I'm using 
is VirtualBox, why, well its free. You can use others if you want (hyperv, parallels, etc). 

Just for reference, Vagrant, VirtualBox, Pipenv and Invoke can all be ignored, if you want.
I use them just as it's my preferred way of working.
 
# Using pipenv in vagrant

Firstly, setup initialise the vagrant environment from the current directory:

`vagrant up`
 
Will download the base Ubuntu image and then install the packages within the 
shell section on top of that image.

to verify that the image has all the required dependencies type:

`vagrant ssh`

This will log you into the the image, at which point you can verify the 
installed applications etc. For example, you can try the following:

`python --version` 

the output should be similar to the following:

`# => Python 3.6.9`

To check pipenv type:

`pipenv --version`

you should see output similar to the following:

`# => pipenv, version 2018.11.26`

If you see this then you can assume that you are setup correctly.
 
Any further setup instructions will be included here as this project unfolds.


