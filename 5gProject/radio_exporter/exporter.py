from flask import Flask, Response
import os
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    metrics_data = ""
    csv_directory = '/app/generated_data/'  # Adjusted for Docker container path

    # Check if directory exists
    if not os.path.exists(csv_directory):
        return Response("No data directory found", status=404)

    for filename in os.listdir(csv_directory):
        if filename.endswith('.csv'):
            with open(os.path.join(csv_directory, filename), 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert the timestamp string to a Unix timestamp in milliseconds
                    timestamp = int(datetime.fromisoformat(row['timestamp']).timestamp() * 1000)
                    for key, value in row.items():
                        if key != 'timestamp':  # Skip the timestamp column
                            # Ensure the value is numeric and handle any potential issues
                            try:
                                float_value = float(value)  # Convert to float for consistency
                                metrics_data += f"{key}{{}} {float_value} {timestamp}\n"
                            except ValueError:
                                continue  # Skip non-numeric values

    if not metrics_data:
        return Response("No metrics data available", status=204)  # No content

    return Response(metrics_data, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)  # Listen on port 8081
