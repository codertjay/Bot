from themelock.themelock import Themelock

try:
    bot = Themelock(teardown=True)
    bot.land_first_page()
    bot.template_list()
    print("Exiting")

except Exception as a:
    print(a)
