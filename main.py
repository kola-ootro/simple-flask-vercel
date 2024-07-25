from flask import Flask
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    logger.info("Accessed root route")
    return "Hello, Vercel!"

@app.route('/test')
def test():
    logger.info("Accessed test route")
    return "Test route is working"

@app.route('/debug')
def debug():
    logger.info("Accessed debug route")
    debug_info = {
        "Python Version": sys.version,
        "Flask Version": Flask.__version__,
        "Environment": app.config['ENV']
    }
    return str(debug_info)

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {str(e)}", exc_info=True)
    return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)