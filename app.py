import sys
from flask import Flask
from housing.logger import logging
from housing.exception import exceptionHousing


app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = exceptionHousing(e, sys)
        logging.info(housing.errorMessage)
        
    logging.info("We are testing the logging module")
    return'''Sai Harsh's machine learning project has started!!'''

if __name__=='__main__':
    app.run(debug=True) 