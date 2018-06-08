# Item Catalog

An application that provides a list of items within a variety of categories as well as a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

This project requires:

- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads)
- SQLAlchemy toolkit for Python

## Run the virtual machine!

```cd``` into the vagrant directory then type **vagrant up** to launch your virtual machine.

## Running the Item Catalog App
Once it is up and running, type **vagrant ssh** to log in. Type **exit** on the shell prompt to log out.  To turn the virtual machine off, type **vagrant halt**. You'll need to run **vagrant up** again before you can log into it.

```cd``` into the vagrant directory.

Now type **python database_setup.py** to initialize the database.

Type **python lotsofitems.py** to populate the database with categories and items.

Type **python project.py** to run the Flask web server. In your browser visit **http://localhost:5000** to view the item catalog app.  You should be able to view, add, edit, and delete items and categories.
