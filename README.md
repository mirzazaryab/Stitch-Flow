# ✂️ Stitch Flow

A Django-based web application to manage tailoring shop operations
including customers, measurements, orders, and payments.\
This project is built to simplify and digitalize the workflow of
tailoring shops.

------------------------------------------------------------------------

## 🚀 Features

-   Customer management (add, view, update, delete)
-   Store detailed measurement records
-   Manage orders with statuses (pending, in progress, completed,
    delivered)
-   Payment tracking for each order
-   User-friendly interface with templates
-   Admin dashboard using Django admin
-   Secure authentication and session management

------------------------------------------------------------------------

## 📂 Project Structure

    tailoring_shop/
    │── customers/        # App to manage customer info and measurements
    │── orders/           # App to handle orders
    │── payments/         # App to track payments
    │── static/           # Static files (CSS, JS, images)
    │── templates/        # HTML templates
    │── tailoring_shop/   # Project configuration files
    │── manage.py         # Django project manager
    │── db.sqlite3        # Database (SQLite)
    │── venv/             # Virtual environment (ignored in Git)

------------------------------------------------------------------------

## ⚙️ Installation Guide

### 1. Clone the Repository

``` bash
git clone https://github.com/mirzazaryab/Tailoring-Orders-Management-System.git
cd Tailoring-Orders-Management-System
```

### 2. Create Virtual Environment

``` bash
python -m venv venv
```

Activate it:

-   **Windows (PowerShell)**

    ``` powershell
    venv\Scripts\activate
    ```

-   **Linux / macOS**

    ``` bash
    source venv/bin/activate
    ```

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4. Run Migrations

``` bash
python manage.py migrate
```

### 5. Create Superuser

``` bash
python manage.py createsuperuser
```

### 6. Run the Server

``` bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

------------------------------------------------------------------------

## 🛠️ Requirements

-   Python 3.8+
-   Django 4.x
-   SQLite (default, or configure PostgreSQL/MySQL if needed)

------------------------------------------------------------------------

## 📸 Screenshots

<img width="1875" height="844" alt="image" src="https://github.com/user-attachments/assets/c3be39bb-31a2-420f-82f8-00abed520cda" />


------------------------------------------------------------------------

## 📜 License

This project is open-source and available under the [MIT
License](LICENSE).

------------------------------------------------------------------------

## 👤 Author

Developed by **Mirza Zaryab**
📧 Contact: mirzazaryab96@gmail.com
