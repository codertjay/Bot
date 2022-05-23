from themelock import Themelock

try:
    bot = Themelock(teardown=True)
    bot.land_first_page()
    print("Exiting")

except Exception as a:
    print(a)
