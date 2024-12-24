import os
import pandas as pd
import time
import logging
from tqdm import tqdm
from colorama import Fore, Style, init
from utils.logger import setup_logger

init(autoreset=True)

def combine_excel_files(input_folder, output_file):
    logger = setup_logger()
    logger.info(Fore.GREEN + "Iniciando el proceso de combinación de archivos Excel.")
    
    # Verificar directorios de entrada y salida
    if not os.path.exists(input_folder):
        logger.error(Fore.RED + f"La carpeta de entrada '{input_folder}' no existe.")
        return
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
        logger.info(Fore.GREEN + f"Directorio de salida creado '{os.path.dirname(output_file)}'.")

    # Listar todos los archivos .xlsx en el directorio de entrada
    excel_files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]
    logger.info(Fore.GREEN + f"Se encontraron {len(excel_files)} archivos Excel para combinar.")

    combined_data = pd.DataFrame()

    # Barra de progreso
    for file in tqdm(excel_files, desc="Combinando archivos", unit="archivo"):
        file_path = os.path.join(input_folder, file)
        logger.info(Fore.GREEN + f"Leyendo archivo: {file_path}")
        
        # Leer el archivo Excel
        data = pd.read_excel(file_path)
        
        # Combinar datos manteniendo los encabezados
        combined_data = pd.concat([combined_data, data.iloc[1:]], ignore_index=True)
        logger.info(Fore.GREEN + f"Datos combinados de {file_path}. Total de filas actuales: {len(combined_data)}")

    # Guardar los datos combinados en un nuevo archivo Excel
    combined_data.to_excel(output_file, index=False, header=True)
    logger.info(Fore.GREEN + f"Archivo Excel combinado guardado en: {output_file}")

    # Resumen de la operación
    total_lines = len(combined_data)
    file_size = os.path.getsize(output_file)
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(Fore.GREEN + f"Operación completada. Total de líneas: {total_lines}, Tamaño del archivo: {file_size} bytes, Tiempo de operación: {elapsed_time:.2f} segundos.")

if __name__ == "__main__":
    start_time = time.time()
    
    input_folder = 'input'
    output_file = 'output/combined.xlsx'
    
    combine_excel_files(input_folder, output_file)
    
    # Mantener el prompt abierto
    input("Presiona Enter para salir...")