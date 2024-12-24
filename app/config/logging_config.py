import logging

def setup_logging():
    """Setup the logging configuration for the application."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()  # Outputs logs to the console
            # You can add more handlers like FileHandler to log to a file.
        ]
    )

    # Create loggers for different modules
    logger = logging.getLogger('app')
    return logger
