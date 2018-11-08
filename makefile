# Need to export as ENV var
export TEMPLATE_DIR = templates

DJANGO_DIR = seniordesign
PYTHONFILES = $(shell ls $(DJANGO_DIR)/*.py)

# build the static website describing the project:
website: 
	-git commit -a 
	git pull origin master
	git push origin master

# the rest of these targets may need to be tweaked for this project:
container:
	docker build -t seniordesign docker


dblocal:
	python3 manage.py makemigrations
	python3 manage.py migrate
