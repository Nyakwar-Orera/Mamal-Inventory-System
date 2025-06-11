# Asset Management System - Technical Documentation

**Presented to:** HOD Supervisor
**Prepared by:** \[Your Name]
**Date:** \[Submission Date]

---

## 1. Project Overview

### 1.1 Introduction

The **Asset Management System (AMS)** is a **Flask-based web application** created to efficiently manage IT and office assets such as desktops, printers, servers, and stationery supplies within an organization or academic institution.

### 1.2 Key Features

* **Dashboard** – Summarizes key data, low-stock notifications, and maintenance reminders.
* **Asset Management** – Allows adding, updating, deleting, and filtering of physical assets.
* **Stationery Tracking** – Monitors paper inventory and alerts on low stock.
* **Check-In/Check-Out** – Records asset allocation to staff/students.
* **Maintenance Logs** – Tracks service and repair histories with cost details.
* **Reports** – Generates downloadable Excel and PDF reports.
* **QR Integration** – Quick updates through QR code scanning.
* **User Authentication** – Supports multiple roles (Admin, Staff, Guest).

### 1.3 Technology Stack

| Category       | Technologies                                 |
| -------------- | -------------------------------------------- |
| Backend        | Python, Flask, Flask-SQLAlchemy, Flask-Login |
| Frontend       | HTML5, CSS3, Bootstrap 5, Chart.js           |
| Database       | SQLite (Dev), PostgreSQL (Prod)              |
| Reporting & QR | Pandas, ReportLab, qrcode                    |
| Deployment     | Docker, Heroku or AWS (optional)             |

---

## 2. System Architecture

### 2.1 High-Level Design

The application follows a simple MVC pattern:

* **Frontend** → User Interface (Bootstrap + JS)
* **Flask Backend** → Routing, Logic, Authentication
* **Database** → Stores persistent asset data

### 2.2 Database Schema

Key Tables:

* `Asset`
* `Stationery`
* `Checkout`
* `Maintenance`
* `User`

---

## 3. Installation & Execution Guide

### 3.1 Prerequisites

* Python 3.8+
* Pip
* Git (optional)

### 3.2 Setup Instructions

**Step 1: Clone the Project**

```bash
git clone https://github.com/your-repo/asset-management-system.git
cd asset-management-system
```

**Step 2: Create and Activate Virtual Environment**

```bash
python -m venv venv
# Activate
source venv/bin/activate    # macOS/Linux
.\venv\Scripts\activate       # Windows
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

Open [http://localhost:5000](http://localhost:5000) in a web browser.

---

## 4. User Guide

### 4.1 Roles and Permissions

| Role  | Permissions                                    |
| ----- | ---------------------------------------------- |
| Admin | Full access (manage users, assets, stationery) |
| Staff | Can manage assets and log checkouts            |
| Guest | View-only access                               |

### 4.2 Workflows

**Add Asset**

* Navigate to `Assets > Add Asset`
* Input details
* QR code is generated automatically

**Checkout an Asset**

* Scan QR or go to `Checkout > Active`
* Select user and due date
* Status updates to `In-use`

**Low Stock Alert**

* When paper < 100 sheets, auto email alert is sent

**Generate Reports**

* Navigate to `Reports`
* Choose Excel or PDF format

---

## 5. Technical Insights

### 5.1 QR Code Support

* Built using `qrcode` library
* Base64 images stored and rendered in templates

### 5.2 Background Tasks

* `APScheduler` runs daily tasks like email notifications

### 5.3 Reports

* Excel: `pandas`, `openpyxl`
* PDF: `reportlab`

---

## 6. Deployment

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
docker build -t asset-management .
docker run -p 5000:5000 asset-management
```

---

## 7. Presentation Tips

### 7.1 Demo Points

* Show dashboard summary
* Scan a QR to view/check asset
* Simulate a low stock and email alert
* Generate and download a PDF report

### 7.2 Sample Questions

**Q:** Can this scale?
**A:** Yes, supports PostgreSQL and Docker for production.

**Q:** Is it secure?
**A:** Yes, uses Flask-Login, hashed passwords, and role-based access.

**Q:** Can it work offline?
**A:** Yes, with SQLite or local server hosting.

---

## 8. Conclusion and Future Work

* **Current**: Web app with asset tracking, user roles, QR, reports
* **Planned**:

  * Mobile QR scanner app
  * Barcode compatibility
  * REST API integration

---

## 9. References

* Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
* Bootstrap: [https://getbootstrap.com/](https://getbootstrap.com/)
* GitHub Repo: \[Your Repo Link Here]

---

**Tip:** Add 10-15 sample entries before demo. Prepare answers and backup screenshots. Good luck!
