from app.models.AttendanceBot import AttendanceBot
import dotenv
import os

def main():
    dotenv.load_dotenv()

    print("Starting Attendance Bot...")

    # [
    #     'https://pmftci.com/college/view-subject-lessons/141458', IT4 IPT2
    #     'https://pmftci.com/college/view-subject-lessons/141459', IT5 EDP
    #     'https://pmftci.com/college/view-subject-lessons/141460', IT16 ADS
    #     'https://pmftci.com/college/view-subject-lessons/141461', IT17 NET2
    #     'https://pmftci.com/college/view-subject-lessons/141462', IT18 SIA 1
    #     'https://pmftci.com/college/view-subject-lessons/141463' IT19 WST 1
    # ]

    email = os.getenv("USER_EMAIL")
    password = os.getenv("USER_PASSWORD")

    bot = AttendanceBot(email, password)

    if not bot.login():
        bot.tag("Invalid credentials", "error")
        return
    
    bot.start(141459)

if __name__ == "__main__":
    main()
