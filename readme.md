# TaskD: CLI Task Tracker App
The project requiremnts is taken from ROADMAP.SH - https://roadmap.sh/projects/task-tracker

## Description:

Taskd is command line application used to track tasks 

## Features

- Add tasks to the list
- Update status of the tasks
- Delete the tasks
- List the task with status filter
- JSON file is used as database
- argparse is used for building commandline app in python 

## Installation

```bash
pip install git+https://github.com/yashjain23/taskd.git
```
## Usage

- ### Add Tasks

```bash
$ taskd add "Do Mathematics Homework"
Successfully created the task with id - 1

$ taskd add "Pick up khushbu from Pune railway station"
Successfully created the task with id - 2
```

- ### List Tasks

```bash
$ taskd
================================================================================================================================================================
 Id                          Description                            Status            Last Status Updated At                         Created At               
================================================================================================================================================================
 1                     Do Mathematics Homework                       ToDo           2025-01-11 22:16:40.459983               2025-01-11 22:16:40.459956       
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 2            Pick up khushbu from Pune railway station              ToDo           2025-01-11 22:18:45.647477               2025-01-11 22:18:45.647443       
----------------------------------------------------------------------------------------------------------------------------------------------------------------
```
- ### Update Status
```bash
$ taskd update 2 Done
Successfully updated the status of the task 3 to Done

$ taskd
================================================================================================================================================================
 Id                          Description                            Status            Last Status Updated At                         Created At               
================================================================================================================================================================
 1                     Do Mathematics Homework                       ToDo           2025-01-11 22:16:40.459983               2025-01-11 22:16:40.459956       
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 2            Pick up khushbu from Pune railway station              Done           2025-01-11 22:23:19.005777               2025-01-11 22:18:45.647443       
----------------------------------------------------------------------------------------------------------------------------------------------------------------
```


- ### See help for more options
```bash
$ taskd -h
usage: taskd [-h] [-s {Done,ToDo,In Progress}] {add,update,delete} ...

A program used to track and manage the tasks

positional arguments:
  {add,update,delete}   Operations on task
    add                 Add task
    update              Update status of the task
    delete              delete the task

options:
  -h, --help            show this help message and exit
  -s {Done,ToDo,In Progress}, --status {Done,ToDo,In Progress}
                        Status filter
```

