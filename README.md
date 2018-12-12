# Senior Design Django Project
In order to run our application, please take the following steps:

	1. Install Docker and Django
	2. Run the following commands 
		docker build -t seniordesign docker
		docker run -it -p 8000:8000 -v "$PWD:/home/SeniorDesign" seniordesign bash
		set -a; . /home/SeniorDesign/.env; set +a
		python3 ./manage.py runserver 0.0.0.0:8000
	3. Navigate to localhost:8000
