# Linux Server Configuration

~~IP Address: 35.183.61.38~~

SSH Port: 2200

~~URL: ```http://ec2-35-183-61-38.ca-central-1.compute.amazonaws.com/```~~

I have graduated from the program, so the webite can no longer be found at the above addresses.

## Required software

- Python
- Apache
- PostgreSQL
- SQLAlchemy
- Flask
- Git

## Configuring the Uncomplicated Firewall

Block incoming connections on every port using ```sudo ufw default deny incoming```

Allow outgoing connections on every port using ```sudo ufw default allow outgoing```

Allow incoming connection for SSH on port 2200 using ```sudo ufw allow 2200/tcp```

Allow incoming connection for SSH on port 22 using ```sudo ufw allow 22```

Allow incoming connection for HTTP on port 80 using ```sudo ufw allow www```

Allow incoming connection for NTP on port 123 using ```sudo ufw allow ntp```

Enable the firewall using ```sudo ufw enable```

In ```/etc/ssh/sshd_config``` change the line that says ```Port 22``` to ```Port 2200```

Block connection to port 22 using ```ufw deny 22```

Restart the SSH service using ```sudo service ssh restart```

From here, you can only SSH to the instance remotely.

## Update packages

```sudo apt-get update```

```sudo apt-get upgrade```

If system restart is required after updating, type the command ```reboot```

## Create the grader user and set up SSH

```sudo useradd grader```

Add grader to sudo admin group using ```sudo usermod -aG sudo grader```

In ```/etc/sudoers``` under the line ```root ALL=(ALL:ALL) ALL``` add the line ```grader ALL=(ALL) NOPASSWD:ALL```

```
sudo mkdir /home/grader/.ssh
sudo chown grader:grader /home/grader/.ssh
sudo chmod 700 /home/grader/.ssh
sudo cp /root/.ssh/authorized_keys /home/grader/.ssh/
sudo chown grader:grader /home/grader/.ssh/authorized_keys
sudo chmod 644 /home/grader/.ssh/authorized_keys
```

In ```/etc/ssh/sshd_config``` change the line ```PermitRootLogin``` to ```PermitRootLogin no```

## Install Apache to serve a Python mod_wsgi application

```sudo apt-get install apache2```

```sudo apt-get install libapache2-mod-wsgi```

## Set up PostgreSQL

```sudo apt-get install postgresql postgresql-contrib```

Create a ```catalog``` user using ```sudo -u postgres createuser -P catalog```

Create a database called ```catalog``` using ```sudo -u postgres createdb -O catalog catalog```

## Install SQLAlchemy, Flask, and Git

```
sudo apt-get install python-psycopg2 python-flask
sudo apt-get install python-sqlalchemy python-pip
sudo pip install oauth2client
sudo pip install requests
sudo apt-get install git
```

## Clone the Item Catalog repo

```
cd /var/www/
sudo mkdir fullstack-nanodegree-vm
sudo chown www-data:www-data fullstack-nanodegree-vm/
sudo -u www-data git clone https://github.com/dmat1986/fullstack-nanodegree-vm.git fullstack-nanodegree-vm
```

Type in ```sudo nano .htaccess``` and add ```RedirectMatch 404 /\.git```

## Set up Item Catalog app for deployment

Inside ```/var/www/fullstack-nanodegree-vm/vagrant/catalog``` create a folder called ```catalog``` and move all the files in there.

Rename project.py to __init__.py using ```sudo mv project.py __init__.py```

Inside ```__init__.py```, ```database_setup.py```, and ```lotsofitems.py``` change the line ```engine = create_engine('sqlite:///electronics.db')``` to ```engine = create_engine('postgresql://catalog:your_password@localhost/catalog')```

Update client_secrets.json from Google OAuth by replacing it with its full path, and changing the javascript origins section to ```"javascript_origins":["http://35.183.61.38", "http://ec2-35-183-61-38.ca-central-1.compute.amazonaws.com/"]```. You also need to add these addresses to the Google Developers Console.

Create the database using ```python database_setup.py``` and ```python lotsofitems.py```

Create catalog.wsgi with the following inside of it:

```
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/fullstack-nanodegree-vm/vagrant/catalog/")

from catalog import app as application

application.secret_key = 'YOUR_SECRET_KEY'
```

Configure Apache2 by using ```sudo nano /etc/apache2/sites-available/catalog.conf```

```
<VirtualHost *:80>
	ServerName http://35.183.61.38
	ServerAdmin admin@35.183.61.38
	WSGIDaemonProcess catalog user=www-data group=www-data threads=5
	WSGIProcessGroup catalog
	WSGIApplicationGroup %{GLOBAL}
	WSGIScriptAlias / /var/www/fullstack-nanodegree-vm/vagrant/catalog/catalog.wsgi
	<Directory /var/www/fullstack-nanodegree-vm/vagrant/catalog/catalog/>
		Require all granted
	</Directory>
	Alias /static /var/www/fullstack-nanodegree-vm/vagrant/catalog/catalog/static
	<Directory /var/www/fullstack-nanodegree-vm/vagrant/catalog/catalog/static/>
		Require all granted
	</Directory>
	ErrorLog ${APACHE_LOG_DIR}/error.log
	LogLevel warn
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Disable the default virtual host using ```sudo a2dissite 000-default.conf```

Enable the virtual host created previously using ```sudo a2ensite catalog.conf```

Restart Apache2 using ```sudo service apache2 restart```

Run the app using ```python __init__.py```

## Third Party Resources

https://www.postgresql.org/docs/

https://help.ubuntu.com/community/PostgreSQL

https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-14-04-lts


