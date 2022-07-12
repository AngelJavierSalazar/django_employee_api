# django_employee_api <br /> <br />

A function to format and ingest fixture data can be accessed at <br />
https://github.com/AngelJavierSalazar/django-json-fixture-converter <br />

Partial CRUD api views and serializer - for creating new employee and view all employees <br />
Templates to work with views for each CRUD - TBC <br />
Filters and analytics - TBC <br /><br />

INSTALLATION<br /><br />

1. Create a virtual environemnt and pip install dependencies in the requirements.txt file<br />
2. Run makemigrations and migrate commands and create admin superuser using the standard Django commands, e.g., python manage.py <command>.<br />
3. Load the fixture data using the command: "python manage.py loaddata fixturedata.json" in your terminal.<br />
4. Start the server and point your browser to the URL shown as per instructions in the terminal.<br />
5. Endpoints for entering data to create new employee and also view all employee records are /api/create and /api/employees respectively. <br /><br />
