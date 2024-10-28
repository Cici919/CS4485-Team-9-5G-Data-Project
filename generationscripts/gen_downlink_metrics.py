import random
from datetime import datetime, timedelta
import pandas as pd

def generate_downlink(numRows):
    start_timestamp = datetime.now()

    timestamp = []
    downlink_sent_bytes = []
    downlink_received_bytes = []
    downlink_sent_packets = []
    downlink_received_packets = []
    downlink_sent_packets_dropped = []
    downlink_received_packets_dropped = []

    for i in range(numRows):
        '''
        timestamp                   (datetime, starting datetime + (i * 5min))
        sent_bytes                  (integer, received_bytes / 23-25)
        received_bytes              (integer, 0.1-0.4 gb)
        sent_packets                (integer, sent_bytes/1000)
        received_packets            (integer, received_bytes/1000)
        sent_packets_dropped        (integer, sent_packets * 0-1%)
        received_packets_dropped    (integer, received_packets * 0-1%)
        '''
        timestamp.append(start_timestamp + timedelta(minutes=i*5))
        downlink_sent_bytes.append(int(random.uniform(0.1, 0.4) * (1073741824 / random.randint(23,25))))
        downlink_received_bytes.append(int(random.uniform(0.1, 0.4) * 1073741824))
        downlink_sent_packets.append(int(downlink_sent_bytes[i] / 1000))
        downlink_received_packets.append(int(downlink_received_bytes[i] / 1000))
        downlink_sent_packets_dropped.append(int(random.uniform(0, 0.01) * downlink_sent_packets[i]))
        downlink_received_packets_dropped.append(int(random.uniform(0, 0.01) * downlink_received_packets[i]))

    df = pd.DataFrame(zip(timestamp, downlink_sent_bytes, downlink_received_bytes, downlink_sent_packets, downlink_received_packets, downlink_sent_packets_dropped, downlink_received_packets_dropped),
                    columns=["timestamp", "downlink_sent_bytes", "downlink_received_bytes", "downlink_sent_packets", "downlink_received_packets", "downlink_sent_packets_dropped", "downlink_received_packets_dropped"])

    timestamp_str = start_timestamp.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"downlink_{timestamp_str}.csv"

    df.to_csv(filename, index=False)

    return filename