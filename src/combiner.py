import os
import pandas as pd
import time
import logging
from utils.logger import setup_logger

def combine_excel_files(input_folder, output_file):
    logger = setup_logger()
    logger.info("Starting the Excel file combination process.")
    
    # List all .xlsx files in the input directory
    excel_files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]
    logger.info(f"Found {len(excel_files)} Excel files to combine.")

    combined_data = pd.DataFrame()

    for file in excel_files:
        file_path = os.path.join(input_folder, file)
        logger.info(f"Reading file: {file_path}")
        
        # Read the Excel file
        data = pd.read_excel(file_path)
        
        # Combine data while maintaining headers
        combined_data = pd.concat([combined_data, data], ignore_index=True)
        logger.info(f"Combined data from {file_path}. Current total rows: {len(combined_data)}")

    # Save the combined data to a new Excel file
    combined_data.to_excel(output_file, index=False)
    logger.info(f"Combined Excel file saved to: {output_file}")

    # Summary of the operation
    total_lines = len(combined_data)
    file_size = os.path.getsize(output_file)
    logger.info(f"Operation completed. Total lines: {total_lines}, File size: {file_size} bytes.")

if __name__ == "__main__":
    start_time = time.time()
    
    input_folder = 'input'
    output_file = 'output/combined.xlsx'
    
    combine_excel_files(input_folder, output_file)
    
    end_time = time.time()
    operation_time = end_time - start_time
    print(f"Operation completed in {operation_time:.2f} seconds. Press Enter to exit.")
    input()