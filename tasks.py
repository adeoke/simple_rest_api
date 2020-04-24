from invoke import task
import os, sys


# in this task the name argument will list the information about the arg
@task(help={'name': "Name of the person to say hi to."})
def hi(c, name):
    """
    Say hi to someone.
    """
    print("Hi {}!".format(name))

@task
def pre_print_dir(_c):
    print('write this before listing dir\n')


@task(pre_print_dir)
def print_dir(c):
    """
    print the working directory
    """
    c.run("pwd")


@task
def print_current_working_directory(_c):
    print(os.getcwd())


@task
def print_load_path(_c):
    print(sys.path)


@task
def run_unit_test(c):
    c.run('python -m unittest tests/unit/*.py')