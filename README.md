# Building project locally

Create virtual environment

    >virtualenv venv

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source venv/bin/activate

OR

Open virtual environment (Windows OS)

    >venv/Scripts/activate

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

Run unit test

    >pytest 
