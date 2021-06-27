# test-scraping

This project is developed with python using the selenium library

## Preparing the environment

Create the environment: `python -m venv env`

Activate environment: `env\Scripts\activate`

Install requirements: `pip install -r requirements.txt`

## Run proyect

Run: `python main.py`

Depending on the speed of your internet connection, you can use the --iw argument, increasing this value, the browser will wait to load the page without throwing an exception. Example: 

Run: `python main.py --iw=20`

## Output data

After running the proyect, data.json should be in the folder of this project

data.json contain all information that has been obtained