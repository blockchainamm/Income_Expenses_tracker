import os
from deta import Deta #pip install deta
from dotenv import load_dotenv # pip install python-dotenv. This takes environment variables from .env

# Load API key from the environment variables
load_dotenv()
DETA_KEY = os.getenv("DETA_KEY")

# Initialize with a database API key
deta = Deta(DETA_KEY)

# Connect to the database
db = deta.Base("monthlyexpenses")

def insert_period(period, incomes, expenses, groceries, car, utilities, comment):
    """Returns the report on successful creation, otherwise raises an error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment, \
                  "groceries": groceries, "car": car, "utilities": utilities})

def fetch_all_periods():
    """Returns a dictionary of all periods"""
    res = db.fetch()
    return res.items

def get_period(period):
    """If period not founds, the function will return none"""
    return db.get(period)