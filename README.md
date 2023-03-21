# eventProject
project for my employer


# launch
Before launch type commands `python3 manage.py makemigrations` and `python3 manage.py migrate`
Use the `make requirements` command or `pip3 install -r requirements.txt` before running.
There are two ways to launch an application:
Makefile(`make`) and docker(`docker-compose up`).
Use command `make run_tests` or `python3 manage.py test .` to run tests
To get test report type `make tests_report` or series of commands `coverage run --source='.' ./manage.py test .` and `coverage report`
