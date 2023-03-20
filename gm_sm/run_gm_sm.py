from gm_sm import GmSM

try:
    bot = GmSM(teardown=True)
    bot.land_first_page()
    bot.get_emails_on_subs()
    bot.convert_to_xl()
    print("Exiting")

except Exception as a:
    print(a)
