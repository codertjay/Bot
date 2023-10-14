import pandas as pd
from datetime import datetime
import os

# Load the CSV data
csv_file = "10_13_setlist.csv"
data = pd.read_csv(csv_file)

# Define the genres
genres = ["pop", "Indie", "Rock", "EDM", "Acoustic", "HipHop", "RnB", "Country", "Global"]

# Get today's date
today_date = datetime.now().strftime("%Y%m%d")

# Create the output folder
output_folder = "/home/codertjay/PycharmProjects/Bot/FrontageBot"

# Loop through genres
for genre in genres:
    # Filter the data for the current genre
    filtered_data = data[(data["genre1"] == genre) | (data["genre2"] == genre) | (data["genre3"] == genre)]

    if not filtered_data.empty:
        # Define the CSV file name
        csv_output_file = f"{today_date}_writeupdata_{genre}.csv"

        # Save the filtered data to a new CSV file
        filtered_data.to_csv(os.path.join(output_folder, csv_output_file), index=False)

        # Define the TXT file name
        txt_output_file = f"{today_date}_{genre}_writeup.txt"

        # Open the TXT file for writing
        with open(os.path.join(output_folder, txt_output_file), "w") as txt_file:
            for index, row in filtered_data.iterrows():
                txt_content = f'{row.get("title")} "Listen:" {row.get("song_link")} {row.get("day of week")}, {row.get("month day")} at {row.get("time")} "({row.get("price")})" {row.get("venue")} "Buy Tix:" {row.get("tix_link")}\n\n'
                txt_file.write(txt_content)

print("Script completed successfully!")
