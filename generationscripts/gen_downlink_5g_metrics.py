import random
from datetime import datetime, timedelta
import pandas as pd

def generate_downlink_5g_metrics(numRows):
    start_timestamp = datetime.now()

    timestamp = []
    downlink_sent_bytes_5g = []
    downlink_received_bytes_5g = []
    downlink_sent_packets_5g = []
    downlink_received_packets_5g = []
    downlink_sent_packets_dropped_5g = []
    downlink_received_packets_dropped_5g = []

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
        downlink_sent_bytes_5g.append(int(random.uniform(0.1, 0.4) * (1073741824 / random.randint(23,25)) / 10))
        downlink_received_bytes_5g.append(int(random.uniform(0.1, 0.4) * 1073741824 / 10))
        downlink_sent_packets_5g.append(int(downlink_sent_bytes_5g[i] / 1000))
        downlink_received_packets_5g.append(int(downlink_received_bytes_5g[i] / 1000))
        downlink_sent_packets_dropped_5g.append(int(random.uniform(0, 0.01) * downlink_sent_packets_5g[i]))
        downlink_received_packets_dropped_5g.append(int(random.uniform(0, 0.01) * downlink_received_packets_5g[i]))

    df = pd.DataFrame(zip(timestamp, downlink_sent_bytes_5g, downlink_received_bytes_5g, downlink_sent_packets_5g, downlink_received_packets_5g, downlink_sent_packets_dropped_5g, downlink_received_packets_dropped_5g),
                    columns=["timestamp", "downlink_sent_bytes_5g", "downlink_received_bytes_5g", "downlink_sent_packets_5g", "downlink_received_packets_5g", "downlink_sent_packets_dropped_5g", "downlink_received_packets_dropped_5g"])
    
    timestamp_str = start_timestamp.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"downlink_5g_{timestamp_str}.csv"

    df.to_csv(filename, index=False)

    return filename