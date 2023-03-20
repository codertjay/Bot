from visto import Visto

try:
    bot = Visto(teardown=True)
    # bot.land_first_page()
    # bot.get_open_all_category_links()
    bot.get_details()
    bot.convert_to_xl()
    print("Exiting")

except Exception as a:
    print(a)
