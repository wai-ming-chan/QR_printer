# How to Convert a Python Script into an Executable (.exe) File Using PyInstaller

This guide explains how to convert your Python script into a standalone `.exe` file using PyInstaller.

## Steps to Create an Executable File

1. **Install PyInstaller**: You need to install `PyInstaller` to create an executable from your Python script. Run the following command in your terminal or command prompt:

    ```
    pip install pyinstaller
    ```

2. **Convert Python Script to an Executable**: 
    - cd to the directory where your Python script is located:
    ```
    cd path/to/your/script
    ```
    - Run PyInstaller to create the `.exe`:
    ```
    pyinstaller --onefile your_script.py
    ```
3. **Locate the Executable**: After running PyInstaller, you will see the following folders created:
    - `dist`: This folder contains your `.exe` file.
    - `build`: Temporary files created during the build process.
    - `your_script.spec`: The configuration file for PyInstaller.

    Inside the `dist/` folder, you will find the generated `.exe` file.

4. **Additional Options**:
    Here are some useful options you can use with PyInstaller:
    - **Add an Icon**: You can specify an icon for your `.exe` file using the `--icon` option:
    ```
    pyinstaller --onefile --icon=your_icon.ico your_script.py
    ```
    - **Hide the Console Window:** If you don’t want the console window to appear, use the `--windowed` option:
    ```
    pyinstaller --onefile --windowed your_script.py
    ```
    - **Add Extra Files:** If your script uses additional files (like images), you can include them using `--add-data`:
    ```
    pyinstaller --onefile --add-data "image.png;." your_script.py
    ```

5. **Run the Executable**: Once PyInstaller completes, your `.exe` file will be located in the `dist/` folder. You can now run or distribute this file, and it will work on any Windows machine without needing Python installed. 