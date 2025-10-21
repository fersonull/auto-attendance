# Auto Attendance Bot (Selenium)

This project is a Python automation bot that logs into a website and performs actions automatically using Selenium. It is designed with Object-Oriented Programming (OOP) structure for maintainability and scalability.

---

## ✅ Features

* Automated login using Selenium WebDriver
* Clean Python OOP architecture
* Includes element wait handling
* Support for console logging
* Ready for future automation (e.g. attendance check)

---

## 🚀 Tech Stack

| Tool               | Purpose                   |
| ------------------ | ------------------------- |
| Python 3.10+       | Main programming language |
| Selenium           | Web automation            |
| WebDriver (Chrome) | Controls the browser      |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/auto-attendance.git
cd auto-attendance
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download ChromeDriver

Download a ChromeDriver version compatible with your Chrome browser:
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

Place it inside the project folder or add it to PATH.

---

## 📁 Project Structure

```
auto-attendance/
│
├── app/
│   ├── models/
│   │   └── AttendanceBot.py
│   ├── utils/
│   │   └── __init__.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ Usage

Configure your credentials and run the bot:

```python
from app.models.AttendanceBot import AttendanceBot

bot = AttendanceBot("your-email@example.com", "your-password")
bot.login()
```

Run it:

```bash
python main.py
```

---

## 🛡️ Notes

* Only use this script for **ethical and legal purposes**.
* Do **not** use this on systems without permission.
* Some websites detect bot behavior—use responsibly.

---

## 🛠️ Future Improvements

* Auto attendance execution
* Headless mode support
* User configuration via `.env`
* Logging system improvements using `rich`

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss.

---

## 📜 License

This project is open-source. You may modify and use it under terms defined by the owner.

---

### ✉️ Contact

For help or suggestions, feel free to reach out.
