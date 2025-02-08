from datetime import datetime


# Get the current date and time
now = datetime.now()
formatted_time = now.strftime("2025-01-29 11:30:00")

# Open the version.md file and write the formatted date and time
with open("version.md", "w") as file:
    file.write(formatted_time)

print(f"Version file updated with current date and time: {formatted_time}")
