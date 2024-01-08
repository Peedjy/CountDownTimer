from flask import Flask, render_template
from datetime import datetime, timedelta
import time

app = Flask(__name__)

def calculate_time_difference(target_date):
    target_datetime = datetime.strptime(target_date, "%Y-%m-%d %H:%M:%S")
    current_datetime = datetime.now()
    time_difference = target_datetime - current_datetime
    return time_difference

def format_time_difference(time_difference):
    days, seconds = time_difference.days, time_difference.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds

@app.route('/')
def countdown():
    target_date = "2024-01-31 23:59:59"  # Remplacez ceci par la date souhaitée au format "YYYY-MM-DD HH:MM:SS"
    time_difference = calculate_time_difference(target_date)
    days, hours, minutes, seconds = format_time_difference(time_difference)

    return render_template('countdown.html', days=days, hours=hours, minutes=minutes, seconds=seconds)

if __name__ == '__main__':
    app.run(debug=True)
