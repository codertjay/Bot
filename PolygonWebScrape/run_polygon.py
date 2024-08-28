from polygon import Polygon

try:
    bot = Polygon(teardown=True)
    bot.get_details_on_links()
    bot.dump_data()
    print("Exiting")

except Exception as a:
    print(a)
