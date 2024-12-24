# Excel Combiner Application

## Overview
The Excel Combiner Application is a Python-based tool designed to combine multiple Excel (.xlsx) files into a single Excel file. The application maintains the headers from the first row of each input file and starts the data from the second row. It is structured for easy enhancements and provides detailed logging of operations.

## Project Structure
```
excel-combiner-app
├── input
│   └── (place your .xlsx files here)
├── output
│   └── (combined .xlsx file will be saved here)
├── src
│   ├── combiner.py
│   └── utils
│       └── logger.py
├── requirements.txt
└── README.md
```

## Directories
- **input/**: Place your Excel (.xlsx) files that need to be combined in this directory.
- **output/**: The combined Excel (.xlsx) file will be saved in this directory after the operation is completed.

## Files
- **src/combiner.py**: The main script that handles the logic for reading input Excel files, combining their data, and saving the output. It also manages logging and provides a summary of the operation upon completion.
- **src/utils/logger.py**: Contains utility functions for logging operations in verbose mode, aiding in debugging and tracking the application's status.
- **requirements.txt**: Lists the dependencies required for the project, such as `pandas` and `openpyxl`, necessary for handling Excel files.

## Installation
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Place the Excel files you want to combine in the `input/` directory.
2. Run the application by executing the following command:
   ```
   python src/combiner.py
   ```
3. After execution, check the `output/` directory for the combined Excel file.

## Logging
The application provides detailed verbose logging of operations, which can be useful for debugging and understanding the flow of the program.

## Summary
Upon completion of the operation, the application will provide a summary that includes:
- Total lines combined
- File size of the output file
- Operation time
- Program status

## Future Enhancements
This project is structured to allow for future enhancements, such as:
- Adding support for more file formats
- Implementing a GUI for easier user interaction
- Enhancing logging features for better tracking

## License
This project is open-source and available for modification and distribution under the terms of the MIT License.