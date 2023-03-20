from gimsap.gimsap import Gimsap

bot = Gimsap(teardown=True)
bot.land_first_page()
# bot.get_collections()
bot.get_collection_products()
bot.get_collection_product_description()
print("Exiting")
# try:
#     bot = Gimsap(teardown=True)
#     bot.land_first_page()
#     # bot.get_collections()
#     bot.get_collection_products()
#     bot.get_collection_product_description()
#     print("Exiting")
#
# except Exception as a:
#     print(a)
