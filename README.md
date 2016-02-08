# python-multiprocess-worker-library
A generic library for childprocess workers


## Installation
All that is required is the Worker.py file.


## Usage
Add the Worker.py file to your source directory and import the module. 
One method initializes the worker(s) and the Job Queue, assigns the passed attributes to the worker and returns the Job Queue for usage. 

JobQueue = StartWorkers(Number_of_workers, AttributeClass)

After calling the function above, one can begin using the workers by putting jobs on the JobQueue. 


## Description
This library spawns "workers" with specific "attributes" that perform the instructions passed to them on the Job Queue. 

#### Worker
Workers are child processes of the main process that spawns it. 

#### Attributes
Attributes are the functions that the child processes are capable of running. They are usually assigned to the workers during the initialization process. Attributes to be assigned to a worker must be passed as a class of non static methods. Each method is required to have self as a parameter. After the attribute are given, they can be referenced by name in the "Job".

#### Jobs
Jobs are the instructions placed into the queue that the Workers carry out. A job is a dictionary containing the "target" and the "arguments". 
The target refers to the Attribute(function) name that should be called. 
The arguments refer to the parameters that must be passed to the function. "Arguments" should preferably be a dictionary of parameter names paired with their respective values. One should ensure that Attributes are designed with the arguments structure used (whether list, dictionary, tuple, etc).

A Job takes the following form:  {"target": "Attribute_Name", "arguments":{"key":"value"}}
Note that arguments can be anything as long as the Attribute expects the format used. 

