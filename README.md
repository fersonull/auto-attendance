Here’s a clean, minimal **README.md** for your **Auto Attendance Bot** 👇

---

````markdown
# 🧠 Auto Attendance Bot (PMFTCI LMS)

An automated attendance bot made specifically for **PMFTCI’s LMS**.  
It automatically logs in and marks attendance for your subjects based on a defined schedule.

---

## ⚙️ Setup Guide

### 1️⃣ Clone the repository
```bash
git clone https://github.com/fersonull/auto-attendance.git
cd auto-attendance
````

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables

Copy the example file and edit it:

```bash
cp .env.example .env
```

Then open `.env` and replace the values with your own credentials:

```
USER_EMAIL=your_lms_email
USER_PASSWORD=your_lms_password
WEBHOOK_URL=your_discord_webhook_url
```

### 5️⃣ Run the bot

```bash
python main.py
```

---

## 📅 Scheduling

The bot automatically runs according to the schedule defined in the code:

```python
scheds = [
    { "subject_id": 141463, "name": "WST 1", "schedule": "08:00" },
    { "subject_id": 141458, "name": "IPT 2", "schedule": "09:30" },
]
```

Each schedule runs daily at the specified time.

---

## 🧩 Features

* Auto login to PMFTCI LMS
* Marks attendance automatically
* Customizable daily schedule
* Discord webhook notifications
* Simple and lightweight setup

---

## ⚠️ Disclaimer

This tool is for **educational and personal automation use only**.
Use responsibly — do not misuse it for cheating or violating LMS terms.

---