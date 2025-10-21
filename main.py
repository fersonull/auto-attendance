from app.models.AttendanceBot import AttendanceBot

def main():
    print("Starting Attendance Bot...")

    email = "youremail@sample.bot"
    password = "yourpassword"

    bot = AttendanceBot(email, password)

    if not bot.login():
        bot.tag("Invalid credentials", "error")
        return
    
    bot.start();

if __name__ == "__main__":
    main()
