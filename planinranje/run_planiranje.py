from planiranje import Planiranje

try:
    bot = Planiranje(teardown=True)
    # bot.land_first_page()
    # bot.get_details()
    bot.convert_to_xl()
    print("Exiting")

except Exception as a:
    print(a)
