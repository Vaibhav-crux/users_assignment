from flask import request, g
from datetime import datetime
from app.config.logging_config import logger

def logging_middleware():
    def before_request():
        logger.info(f"Request: {request.method} {request.url}")
        g.start_time = datetime.now()

    def after_request(response):
        duration = (datetime.now() - g.start_time).total_seconds()
        logger.info(f"Response: {response.status} - Duration: {duration:.2f}s")
        return response

    return before_request, after_request