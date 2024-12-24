import logging
from colorama import Fore, Style

def setup_logger(log_file='app.log'):
    """Configura el logger para la aplicación."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('excel_combiner')

def log_info(message):
    """Registra un mensaje informativo."""
    logging.info(Fore.GREEN + message)

def log_warning(message):
    """Registra un mensaje de advertencia."""
    logging.warning(Fore.YELLOW + message)

def log_error(message):
    """Registra un mensaje de error."""
    logging.error(Fore.RED + message)

def log_summary(total_files, total_lines, file_size, operation_time):
    """Registra un resumen de la operación."""
    log_info("Resumen de la operación:")
    log_info(f"Total de archivos procesados: {total_files}")
    log_info(f"Total de líneas en el archivo combinado: {total_lines}")
    log_info(f"Tamaño del archivo de salida: {file_size} bytes")
    log_info(f"Tiempo de operación: {operation_time} segundos")