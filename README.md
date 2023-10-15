# SIH
# NyayConnect.

Welcome to NyayConnect! This web app is designed to connect legal service providers with clients in India.

## Prerequisites

Before you can run the project, ensure that you have the following software installed on your computer:

- [Python](https://www.python.org/) (3.6 or higher)
- [Virtualenv](https://pypi.org/project/virtualenv/) (for creating a virtual environment)

## Getting Started

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/SIH-Rockers/SIH.git
cd SIH
```

### 2. Create a Virtual Environment

It's recommended to create a virtual environment to isolate project dependencies:

```bash
virtualenv venv
```

Activate the virtual environment

##### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS and Linux

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the project dependencies using `pip` and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Database Setup

To set up the database for this project, follow these steps:

1. Create and apply the database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### 5. Create a Superuser

To create a superuser account, which will allow you to access the Django admin panel, follow these steps:

1. Run the following command:

   ```bash
   python manage.py createsuperuser
   ```


