from app.models.AttendanceBot import AttendanceBot
import dotenv
import os

def main():
    dotenv.load_dotenv()

    print("Starting Attendance Bot...")

    email = os.getenv("USER_EMAIL")
    password = os.getenv("USER_PASSWORD")

    bot = AttendanceBot(email, password)

    if not bot.login():
        bot.tag("Invalid credentials", "error")
        return
    
    bot.start();

if __name__ == "__main__":
    main()
