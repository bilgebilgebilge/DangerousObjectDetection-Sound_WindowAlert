# Dangerous Object Detection with Sound and Window Alert

In Short:
Running this project is easy! Just run the "run.bat" file once, and it will handle everything. The necessary dependencies will be installed, and the project will be ready for use. You won’t need to manually install anything after the initial setup. Enjoy using the object detection alerts without worrying about dependencies!

This project uses the YOLOv8 model to detect dangerous objects in a video stream and provides both audio and visual alerts.  All necessary dependencies and configurations are integrated into the provided files, making it easy for you to run the project with minimal setup.

## 🔍 Features
- ⚡ **YOLOv8** based object detection
- 🔊 Real-time audio alerts (e.g., for knife, scissors, gun)
- 🪟 Pop-up window alerts via Tkinter
- 🇹🇷 Supports Turkish object labels


# Dangerous Object Detection with Sound Alert

This project detects dangerous objects in real-time using a camera feed, providing visual and audio alerts. It can be easily used through an EXE file for beginners or via BAT file and Python script for advanced users.

## Getting Started

There are two main ways to run the project according to your technical expertise:

### 1. **For Beginners (EXE File)**

If you are a beginner and want to use the application quickly without worrying about installation or dependencies, you can just run the **EXE file**. Contact me if you need it. DangerousObjectDetection.exe will be shared with you.

#### Steps in this case:
1. Run `DangerousObjectDetection.exe` from the Versions section.
2. Double-click to run the application.
3. The program will automatically start detecting dangerous objects using your camera and you will hear a sound alert for detected dangerous objects (The speed of the program opening may vary depending on the performance of your computer).

**Note**: The EXE file contains all the necessary dependencies and can be run without the need to install Python or any additional libraries. Just run the EXE and the program will work out of the box.

If the window does not close, you can stop it in the task manager.
---

### 2. **For Intermediate and Advanced Users (Using BAT File or Python Script)**

If you are more familiar with development or want to run the project from the command line or your IDE, you can use the **BAT file** or run the **Python script directly**.

#### Running the Project Using the `run.bat` File (for Intermediate Users)

The `run.bat` file is an automated script that sets up the environment and runs the project. It's a convenient method for users who are comfortable with running batch files.

#### Steps:
1. Make sure you have **Python 3.x** installed on your machine. You can download Python from the official website [here](https://www.python.org/).
2. Download the project files and extract them to your preferred directory.
3. Double-click on the `run.bat` file to execute it. This script will:
   - Create a virtual environment for the project.
   - Install all necessary dependencies from the `requirements.txt` file.
   - Automatically run the `main.py` script to start the object detection.

After the program finishes, the virtual environment will be deactivated automatically.

---

#### Running the Project Directly Using `main.py` (for Advanced Users)

For users who prefer to work with Python directly and want full control over the code, you can run the project by manually installing the dependencies and executing the Python script.

#### Steps:
1. **Install Python**: Ensure Python 3.x is installed on your system.
2. **Set Up a Virtual Environment**: 
   - Open a terminal (Command Prompt, PowerShell, or any terminal emulator).
   - Navigate to the project folder.
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**: `venv\Scripts\activate`
     - **Mac/Linux**: `source venv/bin/activate`
3. **Install Dependencies**:
   - Run the following command to install the required packages:
     ```bash
     pip install -r requirements.txt
     ```
4. **Run the Project**:
   - Once all dependencies are installed, run the main script:
     ```bash
     python main.py
     ```

This method gives you more control over the project and allows you to modify the code as needed. If you prefer to use **VS Code** or another IDE, simply open the project folder and run the `main.py` script after setting up the virtual environment.

---

## Notes:
- **Dependencies**: If you're running the BAT or Python script, make sure to install the required libraries (listed in `requirements.txt`). The EXE file contains these dependencies already bundled.
- **First-Time Setup**: When running the BAT or Python script for the first time, it will install the necessary libraries. You only need to install them once. After that, you can run the project without reinstalling the packages.
- **Tkinter**: The project requires `tkinter` for the GUI part. If you are using Python directly, ensure that `tkinter` is installed. It comes pre-installed with most Python versions. If you encounter issues, check the Python version compatibility and install it manually.

---

## Conclusion

- **Beginner**: Simply run the **EXE file** for a hassle-free experience.
- **Intermediate/Advanced**: Use the **BAT file** or run the project directly via **Python** for more flexibility and control.

Feel free to modify and enhance the code to better fit your needs!


## Required Libraries
The following libraries are required to run this project:
- opencv-python
- ultralytics
- gtts
- pygame
- tkinter (included in most Python installations)



