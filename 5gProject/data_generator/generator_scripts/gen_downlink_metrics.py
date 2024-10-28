import random
from datetime import datetime, timedelta
import pandas as pd
import os

# Specify the output directory
output_dir = './generated_data/'

# Set the starting timestamp to the current UTC time
start_timestamp = datetime.utcnow()
numRows = 288

timestamp = []
downlink_sent_bytes = []
downlink_received_bytes = []
downlink_sent_packets = []
downlink_received_packets = []
downlink_sent_packets_dropped = []
downlink_received_packets_dropped = []

for i in range(numRows):
    # Generate timestamps in UTC
    timestamp.append(start_timestamp + timedelta(minutes=i * 5))
    downlink_sent_bytes.append(int(random.uniform(0.1, 0.4) * (1073741824 / random.randint(23, 25))))
    downlink_received_bytes.append(int(random.uniform(0.1, 0.4) * 1073741824))
    downlink_sent_packets.append(int(downlink_sent_bytes[i] / 1000))
    downlink_received_packets.append(int(downlink_received_bytes[i] / 1000))
    downlink_sent_packets_dropped.append(int(random.uniform(0, 0.01) * downlink_sent_packets[i]))
    downlink_received_packets_dropped.append(int(random.uniform(0, 0.01) * downlink_received_packets[i]))

df = pd.DataFrame(zip(timestamp, downlink_sent_bytes, downlink_received_bytes, downlink_sent_packets, downlink_received_packets, downlink_sent_packets_dropped, downlink_received_packets_dropped),
                  columns=["timestamp", "downlink_sent_bytes", "downlink_received_bytes", "downlink_sent_packets", "downlink_received_packets", "downlink_sent_packets_dropped", "downlink_received_packets_dropped"])

# Save to the generated_data directory
try:
    df.to_csv(os.path.join(output_dir, "downlink_metrics.csv"), index=False)
except Exception as e:
    print(f"Error saving CSV: {e}")
