# Finance Tracker

A Python-based Finance Tracker application.

## Setup Instructions

Follow these steps to set up and run the project locally.

### 1. Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd finance-tracker
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn app:app --reload
```

Open the application in your browser:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs


## Technologies Used

- Python
- FastAPI

## Notes

- Ensure Python is installed and added to PATH.
- Activate the virtual environment before installing dependencies or running the application.
- If you add new dependencies, update `requirements.txt` 