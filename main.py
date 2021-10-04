""" Main script: run the project """
import logging
import uvicorn
from app.main import app

if __name__ == '__main__':
    logging.info("Starting project")
    uvicorn.run(app, host='0.0.0.0', port=8000)
