from pywinauto.application import Application

# Start the application
app = Application().start("brave")

# Interact with the application
app.YourWindowName.YourControlName.click()
app.YourWindowName.YourControlName.type_keys("Your text")
