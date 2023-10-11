## HBNB Console
![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

### Intro

We were tasked with creating our own first full web application, an AirBnB clone.
This being just the first part of a much bigger project, where we worked on the
backend with the help of the cmd module we were able to get a console application
up and started.

### Description

The **HBNB Console** is a command-line interpreter for managing instances of various classes. It allows you to create, show, destroy, update, and list instances of classes like BaseModel, User, State, City, Amenity, Place, and Review.

### How to Start

To start the HBNB Console, follow these steps:

1. Clone the repository to your local machine:
   ```git clone https://github.com/cpmoore0317/holbertonschool-AirBnB_clone.git```

2. Change to the project directory:
    ```cd holbertonschool-AirBnB_clone```

3. Run the console:
    ```./console.py```

### How to Use

The HBNB Console supports the following commands:

* create: Create a new instance of a class. Usage: create <class name>.
* show: Show details of an instance. Usage: show <class name> <instance id>.
* destroy: Delete an instance. Usage: destroy <class name> <instance id>.
* all: List all instances or instances of a specific class. Usage: all or all <class name>.
* update: Update an instance's attributes. Usage: update <class name> <instance id> <attribute name> "<new value>".

To exit the console, use the quit or EOF command.

### Examples

Here is an example usage of the console:

```
holbie$ ./console.py

(hbnb) create NewModel
49faff9a-6318-451f-87b6-910505c55907

(hbnb) all NewModel
["[NewModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2023, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2023, 10, 2, 3, 10, 25, 903300)}"]

(hbnh) destroy NewModel 49faff9a-6318-451f-87b6-910505c55907

(hbnb) show NewModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **

(hbnb)
```

### Authors

Matthew Krozel
Parker Moore
