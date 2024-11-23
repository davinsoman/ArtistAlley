"""This is possible because of the __init__.py file in the website folder
that file turns the website folder into a python package that can be imported"""

from website import create_app 

app = create_app()

"""This is the entry point for the application, if we run this file directly it will run the web server"""
if __name__ == '__main__':
    app.run(debug=True)