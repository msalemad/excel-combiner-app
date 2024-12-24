# Excel Combiner App

![version](https://img.shields.io/badge/version-1.0.0-blue)
![python](https://img.shields.io/badge/python-3.8%2B-green)
![license](https://img.shields.io/badge/license-MIT-yellow)

---

## Resumen

La Aplicación Combinadora de Excel es una herramienta basada en Python diseñada para combinar múltiples archivos Excel (.xlsx) en un solo archivo Excel. La aplicación mantiene los encabezados de la primera fila de cada archivo de entrada y empieza los datos desde la segunda fila. Está estructurada para facilitar mejoras y proporciona un registro detallado de las operaciones.

## Estructura del Proyecto

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
│
├── combiner.exe
├── requirements.txt
└── README.md
```

## 📁 Directorios

- **📂 input/**: Coloca tus archivos Excel (.xlsx) que necesitan ser combinados en este directorio.
- **📂 output/**: El archivo Excel (.xlsx) combinado se guardará en este directorio después de que la operación se complete.

---

## 📄 Archivos

- **`src/combiner.py`**: El script principal que maneja la lógica para leer los archivos Excel de entrada, combinar sus datos y guardar el resultado. También gestiona el registro y proporciona un resumen de la operación al finalizar.
- **`src/utils/logger.py`**: Contiene funciones utilitarias para el registro de operaciones en modo detallado, ayudando en la depuración y seguimiento del estado de la aplicación.
- **`requirements.txt`**: Enumera las dependencias requeridas para el proyecto, como `pandas` y `openpyxl`, necesarias para manejar archivos Excel.

---

## 🛠️ Instalación

1. Clona el repositorio o descarga los archivos del proyecto.
2. Navega al directorio del proyecto.
3. Instala las dependencias requeridas usando pip:
   ```sh
   pip install -r requirements.txt
   ```

---

## 🚀 Uso

1. Coloca los archivos Excel que deseas combinar en el directorio `input/`.
2. Ejecuta la aplicación ejecutando el siguiente comando:

   ```sh
   python src/combiner.py
   ```

   O ejecuta el archivo ejecutable:
   ```sh
   ./combiner.exe
   ```
3. Después de la ejecución, revisa el directorio `output/` para el archivo Excel combinado.

---

## 📝 Registro

La aplicación proporciona un registro detallado y verboso de las operaciones, lo que puede ser útil para la depuración y comprensión del flujo del programa.

---

## 📊 Resumen

Al completar la operación, la aplicación proporcionará un resumen que incluye:

- Total de líneas combinadas
- Tamaño del archivo de salida
- Tiempo de operación
- Estado del programa

---

## 🌟 Mejoras Futuras

Este proyecto está estructurado para permitir futuras mejoras, tales como:

- Agregar soporte para más formatos de archivo
- Implementar una interfaz gráfica para una interacción más sencilla del usuario
- Mejorar las características de registro para un mejor seguimiento
- Optimizar el rendimiento para manejar archivos más grandes
- Añadir soporte para la combinación de hojas específicas dentro de los archivos Excel
- Implementar pruebas automatizadas para asegurar la calidad del código

---

## 📜 Licencia

Este proyecto es de código abierto y está disponible para modificación y distribución bajo los términos de la Licencia MIT.
