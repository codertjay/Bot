from booking import Booking

try:
    bot = Booking(teardown=True)
    bot.land_first_page()
    bot.change_currency(currency='GBP')
    bot.select_place_to_go('New York')
    bot.select_dates(
        check_in_date="2022-05-18",
        check_out_date="2022-05-19")
    bot.select_adults(count=10)
    bot.click_search()
    bot.apply_filtration()
    bot.refresh()  # work around get data properly
    bot.report_results()
    print("Exiting")

except Exception as a:
    print(a)
