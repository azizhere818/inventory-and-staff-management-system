# Inventory Management System

A menu-driven inventory and staff management system built using **Python** and **MySQL**.

The application allows users to manage inventory items and staff records through a command-line interface while storing all data in a MySQL database.

---

## Features

### Items Management

- Add new items
- Delete items
- Search items using PID
- Display all items
- Sort items by PTYPE
- Sort items by PCOST
- Sort items by PQTY
- Update PCOST
- Update PQTY

### Staff Management

- Add new staff records
- Delete staff records
- Search staff using ID
- Display all staff
- Sort staff by NAME
- Sort staff by DEPT
- Sort staff by SALARY
- Update PHONE
- Update SALARY
- Update DEPT

---

## Database

Database Name:

```text
supermarket
```

### Table: items

| Column | Type |
|---------|------|
| PID | INT |
| PNAME | VARCHAR(50) |
| PTYPE | VARCHAR(50) |
| PCOST | FLOAT |
| PQTY | INT |

### Table: staff

| Column | Type |
|---------|------|
| ID | INT |
| NAME | VARCHAR(50) |
| DEPT | VARCHAR(50) |
| PHONE | INT |
| SALARY | FLOAT |
| EMAIL | CHAR(70) |
| DOJ | DATE |

---

## Technologies Used

- Python
- MySQL
- mysql-connector-python
- tabulate

---

## Project Structure

```
inventory-management-system/
│
├── inventory.py
├── supermarket.sql
├── README.md
└── Screenshots/
```

---

## Setup

1. Install MySQL.
2. Create the database:

```sql
CREATE DATABASE supermarket;
```

3. Create the required tables (`items` and `staff`).

4. Install the required Python packages:

```bash
pip install mysql-connector-python tabulate
```

5. Open the Python file and replace the database connection placeholders with your own credentials:

```python
host = "YOUR_HOST"
user = "YOUR_DATABASE_USER"
password = "YOUR_DATABASE_PASSWORD"
database = "supermarket"
```

6. Run the application.

---

## How It Works

The application connects to the **supermarket** MySQL database and provides a menu-driven interface for managing inventory items and staff records.

Users can perform Create, Read, Update, Delete (CRUD) operations directly from the terminal, with all data stored in MySQL.

---

## My Role

- Designed the MySQL database schema.
- Built the Python application.
- Wrote SQL queries for CRUD operations.
- Connected Python with MySQL using `mysql-connector-python`.
- Used AI as a development assistant for learning, debugging, and improving the implementation.

---

## Security Note

The public version of this project does not include real database credentials or sensitive information.

Before running the project, configure your own MySQL connection details.

---

## Future Improvements

- Graphical User Interface (GUI)
- Login authentication
- Inventory reports
- Barcode support
- Low-stock alerts
- Export reports to Excel/PDF
- Dashboard and analytics

---

## License

This project was created for learning and portfolio purposes.
