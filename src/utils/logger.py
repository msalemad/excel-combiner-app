import logging
import os

def setup_logger(log_file='app.log'):
    """Sets up the logger for the application."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def log_info(message):
    """Logs an informational message."""
    logging.info(message)

def log_warning(message):
    """Logs a warning message."""
    logging.warning(message)

def log_error(message):
    """Logs an error message."""
    logging.error(message)

def log_summary(total_files, total_lines, file_size, operation_time):
    """Logs a summary of the operation."""
    log_info(f"Operation Summary:")
    log_info(f"Total Files Processed: {total_files}")
    log_info(f"Total Lines in Combined File: {total_lines}")
    log_info(f"Output File Size: {file_size} bytes")
    log_info(f"Operation Time: {operation_time} seconds")