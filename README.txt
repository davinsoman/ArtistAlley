Steps to creating the requirements file for sharing (Do not follow these instructions first):

1. Create a virtual environment: Create a virtual environment in your project directory. This isolates your project's dependencies from the global Python environment.

    python -m venv venv

2. Activate the virtual environment: Activate the virtual environment. The command varies depending on your operating system:

    Windows: venv\Scripts\activate

    macOS/Linux: source venv/bin/activate

3. Install dependencies: Install Flask and any other dependencies you need for your project.

    pip install Flask Flask-SQLAlchemy Flask-Login Flask-Uploads

4. Freeze dependencies: Create a requirements.txt file that lists all the dependencies for your project.

    pip freeze > requirements.txt

5. Share the requirements.txt file: Include the requirements.txt file in your project repository. This file will allow others to install the necessary dependencies easily.

Steps for installing dependencies needed to run the application (Follow this one by inputting these commands in the vs terminal):

6. Install dependencies from requirements.txt: When someone else clones your repository, they can create and activate a virtual environment, then install all the dependencies using the requirements.txt file.

    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    pip install -r requirements.txt

After doing backend work, if you needed to install a new dependency simply follow step 4 to update the requirements.txt

If you get an error when inputting venv\Scripts\activate, you need to open windows powershell(as admin) and input the following:
    
    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

Then confirm the change by typing Y if prompted and pressing Enter