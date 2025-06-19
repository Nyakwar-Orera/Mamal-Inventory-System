Here’s your **cleaned and updated `README.md`** file that merges both versions — keeping the **detailed documentation** and **project name** from both sides:

---

````markdown
# Mamal Inventory System - Technical Documentation

**Presented to:** HOD Supervisor  
**Prepared by:** Nyakwar Orera  
**Date:** [Submission Date]  

---

## 1. Project Overview

### 1.1 Introduction

The **Mamal Inventory System** is a **Flask-based web application** developed to efficiently manage IT and office assets such as desktops, printers, servers, and stationery supplies in an organizational or institutional setting.

### 1.2 Key Features

- **Dashboard** – Summarizes key data, low-stock notifications, and maintenance reminders.  
- **Asset Management** – Add, update, delete, and filter physical assets.  
- **Stationery Tracking** – Monitors stationery inventory and alerts on low stock.  
- **Check-In/Check-Out** – Records asset allocations to staff/students.  
- **Maintenance Logs** – Track service history and associated costs.  
- **Reports** – Downloadable Excel and PDF reports.  
- **QR Integration** – Quick actions via QR code scanning.  
- **User Authentication** – Role-based access (Admin, Staff, Guest).

### 1.3 Technology Stack

| Category       | Technologies                                 |
| -------------- | -------------------------------------------- |
| Backend        | Python, Flask, Flask-SQLAlchemy, Flask-Login |
| Frontend       | HTML5, CSS3, Bootstrap 5, Chart.js           |
| Database       | SQLite (Dev), PostgreSQL (Prod)              |
| Reporting/QR   | Pandas, ReportLab, qrcode                    |
| Deployment     | Docker, Heroku or AWS (optional)             |

---

## 2. System Architecture

### 2.1 High-Level Design

The application follows a simple MVC pattern:

- **Frontend** → Bootstrap + JS  
- **Flask Backend** → Routing, Logic, Authentication  
- **Database** → Persistent asset data

### 2.2 Database Schema

Key Tables:

- `Asset`  
- `Stationery`  
- `Checkout`  
- `Maintenance`  
- `User`  

---

## 3. Installation & Execution Guide

### 3.1 Prerequisites

- Python 3.8+  
- Pip  
- Git (optional)  

### 3.2 Setup Instructions

**Step 1: Clone the Project**

```bash
git clone https://github.com/Nyakwar-Orera/Mamal-Inventory-System.git
cd Mamal-Inventory-System
````

**Step 2: Create and Activate Virtual Environment**

```bash
python -m venv venv
# Activate
source venv/bin/activate    # macOS/Linux
.\venv\Scripts\activate     # Windows
```

**Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
pip install email_validator
```

**Step 4: Configure Environment**

Create a `.env` file:

```env
FLASK_ENV=development
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///assets.db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-email-password
ADMIN_EMAIL=admin@example.com
```

**Step 5: Initialize Database**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

**Step 6: Launch the App**

```bash
flask run --host=127.0.0.1 --port=5000
```

Then open: [http://localhost:5000](http://localhost:5000)

---

## 4. User Guide

### 4.1 Roles and Permissions

| Role  | Permissions                             |
| ----- | --------------------------------------- |
| Admin | Full access (users, assets, stationery) |
| Staff | Manage assets, checkouts                |
| Guest | View-only access                        |

### 4.2 Common Workflows

* **Add Asset**: `Assets > Add Asset`, fill form, QR is auto-generated.
* **Checkout Asset**: `Checkout > Active`, assign to user with due date.
* **Low Stock Alerts**: Email triggered when stationery (e.g., paper) < 100.
* **Generate Report**: Go to `Reports`, select Excel or PDF.

---

## 5. Technical Insights

### 5.1 QR Code Support

* Generated using `qrcode` library
* Rendered via base64 images in HTML

### 5.2 Background Tasks

* Daily tasks via `APScheduler` (e.g., email alerts)

### 5.3 Report Generation

* **Excel**: `pandas`, `openpyxl`
* **PDF**: `reportlab`

---

## 6. Deployment Options

### Option 1: Heroku

```bash
heroku create your-app-name
git push heroku main
heroku run flask db upgrade
```

### Option 2: Docker

**Dockerfile:**

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
```

Run:

```bash
docker build -t mamal-inventory .
docker run -p 5000:5000 mamal-inventory
```

---

## 7. Demo & Presentation Tips

### 7.1 Key Demo Actions

* Use dashboard to show data overview
* Scan QR code to check an asset
* Simulate low stationery alert
* Download and show a PDF report

### 7.2 Possible Questions

* **Can this scale?** Yes — supports PostgreSQL and Dockerized environments.
* **Is it secure?** Yes — uses Flask-Login, password hashing, and role control.
* **Can it run offline?** Yes — using SQLite and local hosting.

---

## 8. Conclusion and Future Enhancements

### Current System:

* Role-based asset and inventory management
* QR & report generation
* Background alert tasks

### Future Improvements:

* Mobile app with QR scanner
* Barcode reader integration
* REST API support for third-party tools

---

## 9. References

* Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
* Bootstrap: [https://getbootstrap.com/](https://getbootstrap.com/)
* GitHub Repo: [https://github.com/Nyakwar-Orera/Mamal-Inventory-System](https://github.com/Nyakwar-Orera/Mamal-Inventory-System)

---

**Tip:** Seed your database with 10–15 records for smoother demos. Prepare for questions. Backup screenshots just in case. Good luck!

```

---

Let me know if you want this in a downloadable `.md` file or pushed to your GitHub repo.
```
