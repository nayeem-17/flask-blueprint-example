## Structure a Large Flask Application
```
├── flask_app
│   ├── app
│   │   ├── database.py
│   │   ├── __init__.py
│   │   ├── main
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── models
│   │   │   └── posts.py
│   │   └── posts
│   │       ├── __init__.py
│   │       └── routes.py
│   ├── app.db
│   └── config.py
└── README.md
```

## Description
This is a simple structure for a large Flask application. The structure is as follows:
- `app` is the main package that contains the application factory and other configurations.
- `main` is a blueprint that contains the main routes of the application.
- `posts` is a blueprint that contains the routes for posts.
- `models` is a package that contains the database models.
- `database.py` contains the database instance.
- `config.py` contains the configurations for the application.

## The structure of a blueprint
```
├── blueprint
│   ├── __init__.py
│   └── routes.py
```
here,
- `__init__.py` contains the blueprint instance. For example:
    ```python
    from flask import Blueprint

    bp = Blueprint('blueprint_name', __name__)

    from flask_app.blueprint_name import routes
    ```
- `routes.py` contains the routes for the blueprint. For example:
    ```python
    from flask import render_template
    from flask_app.blueprint_name import bp

    @bp.route('/test')
    def test():
        return render_template('test.html')
    ```

## Installation
1. Clone the repository
2. Install the requirements
```bash
pip install -r requirements.txt
```

## Usage
To run the application, execute the following command:
```bash
flask run
```

To run using `flask run` provide the `FLASK_APP` and `FLASK_ENV` environment variables:
```bash
export FLASK_APP=flask_app.app
export FLASK_ENV=development
flask run
```

or use `.env` file:
```bash
FLASK_APP=flask_app.app
FLASK_ENV=development
```