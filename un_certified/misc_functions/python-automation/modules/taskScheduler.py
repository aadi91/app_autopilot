# Schedule Library imported
import schedule
import time

# Functions setup
def sudo_placement():
    print("Get ready for Sudo Placement at automation task")


def good_luck():
    print("Good Luck for Test")


def work():
    print("Study and work hard")


def bedtime():
    print("It is bed time go rest")


def automationTask():
    print("Shaurya says automation task")


# Task scheduling
# After every 10mins automation task() is called.
schedule.every(10).minutes.do(automationTask)

# After every hour automation task() is called.
schedule.every().hour.do(automationTask)

# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("00:00").do(bedtime)

# After every 5 to 10mins in between run work()
schedule.every(5).to(10).minutes.do(work)

# Every monday good_luck() is called
schedule.every().monday.do(good_luck)

# Every tuesday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("18:00").do(sudo_placement)

# Loop so that the scheduling task
# keeps on running all time.
while True:

    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
