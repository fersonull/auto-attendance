from app.models.AttendanceBot import AttendanceBot
import schedule
import dotenv
import os
import time

def run_bot(subject):
    email = os.getenv("USER_EMAIL")
    password = os.getenv("USER_PASSWORD")

    bot = AttendanceBot(email, password)

    if not bot.login():
        bot.tag("Invalied credentials", "error")
        return

    bot.start(subject=subject)

def main():
    dotenv.load_dotenv()

    print("Attendance bot loaded! Waiting for scheduled subjects...")

    # [
    #     'https://pmftci.com/college/view-subject-lessons/141458', IT4 IPT2
    #     'https://pmftci.com/college/view-subject-lessons/141459', IT5 EDP
    #     'https://pmftci.com/college/view-subject-lessons/141460', IT16 ADS
    #     'https://pmftci.com/college/view-subject-lessons/141461', IT17 NET2
    #     'https://pmftci.com/college/view-subject-lessons/141462', IT18 SIA 1
    #     'https://pmftci.com/college/view-subject-lessons/141463' IT19 WST 1
    # ]  

    scheds = [
        { "subject_id": 141463, "name": "WST1", "schedule": "02:04" },
        { "subject_id": 141458, "name": "IPT2", "schedule": "02:05" }
    ]

    for sched in scheds:
        schedule.every().day.at(sched["schedule"]).do(run_bot, subject=sched)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
