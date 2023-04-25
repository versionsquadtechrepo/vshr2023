Prerequirements : 
	Python 3.6+
	Postgres SQL & dependencies

Create virtual env
Checkout the code
Goto the folder
install dependecies by hitting the following command
	pip -m install requirements.txt
Create a new database in the Postgre - hrversion_db_20230319
Create a user and provide full privileges to the new create

Change the DB credentials in settings.txt DATABASES section
run following commands to migrate the database
	python manage.py makemigrations
	python manage.py migrate
	
	








Account creation:
	Email Id & Login
	Organisation / account details
		Name 
		Braches
		Branch Address
		Emails
		Phone numbers
		Others - TODO
	Start creating users 


