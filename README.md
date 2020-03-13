
# certus-challenge


## Description
Pentestfinding is controller that calls other modules such as migrationcsv. We want candidates to add features highlighted in section below titled ‘Task’. The data stored in the DB is referred as findings and all findings are already migrated to SQLite DB but one can also port findings using audit_questions.py.

 

 

## Task

* From API, edit following fields - findings, descriptions, solutions. All new edits must be stored within SQLite DB

* From API add functionality to build new findings along with mandatory descriptions and solutions text fields. When adding 
the field to the DB ensure there are no duplicates and encode any special characters.

* Provide a list view of all findings (field) within DB to the end user that they can select. 
Once selected end user should have an option to download selected findings (only) along with their descriptions and solutions to PDF and HTML.
  


### Requirements

* [wkhtml](https://wkhtmltopdf.org/downloads.html)
* Python version 3.6 or 3.7



### Installation
1. Install [wkhtml](https://wkhtmltopdf.org/downloads.html)

2. clone this repository 
          
3. create a virtual environment with python 3.x for the project
    * Click [here](https://docs.python.org/3/library/venv.html) to learn how to 
    create virtual environment for python project

4. Run the following command to install the packages in the requirements.

    ```bash
    pip install -r requirements.txt
    ``` 
     or in case you are not using virtual environment and have multiple python versions installed.
    ```bash
    pip3 install -r requirements.txt
    
    ```
5. Make Migrations
    ```bash
    python manage.py makemigrations
    
    python manage.py migrate
    
    ```

6. Create Super user (It is required for admin permission to create/update Findings API)
     ```bash
    python manage.py createsuperuser
    ```

7. Run Django server
    ```bash
    python manage.py runserver 8000
    ```

8. Log in to [admin](http://127.0.0.1:8000/admin/) with the username and password created in 6. 


### Usage
* Findings API [documentation](http://127.0.0.1:8000/findings/api/v1/redoc/)
* Findings API [swagger](http://127.0.0.1:8000/findings/api/v1/docs/)
* List findings [here](http://127.0.0.1:8000/appsec/findings/)