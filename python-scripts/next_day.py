from datetime import datetime, timedelta

# Parse the input string to a datetime object (assuming current year -- 2025)
current_year = datetime.now().year
input_date = datetime.strptime(f"{inputData['end_date']}/{current_year}", "%a %m/%d/%Y")

# Calculate the next day's 8:00 AM time
next_day_fire_time = input_date + timedelta(days=1)
next_day_fire_time = next_day_fire_time.replace(hour=8, minute=0, second=0, microsecond=0)

# Convert to a string for JSON serialization
next_day_fire_time_str = next_day_fire_time.isoformat()

# Output the result
output = [{'email_date': next_day_fire_time_str}]
