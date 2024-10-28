import random
from datetime import datetime, timedelta
import pandas as pd

def generate_link_ip_rate_5g(numRows):
    start_timestamp = datetime.now()

    timestamp = []
    uplink_success_rate_5g = []
    uplink_drop_rate_5g = []
    downlink_success_rate_5g = []
    downlink_drop_rate_5g = []
    allocate_ip_success_5g = []
    release_ip_success_5g = []
    allocated_ip_count_5g = []
    counter = 0

    for i in range(numRows):
        timestamp.append(start_timestamp + timedelta(minutes=i*5))
        uplink_success_rate_5g.append(round(random.uniform(0.8, 1), 2))
        uplink_drop_rate_5g.append(1 - uplink_success_rate_5g[i])
        downlink_success_rate_5g.append(round(random.uniform(0.8, 1), 2))
        downlink_drop_rate_5g.append(1 - downlink_success_rate_5g[i])
        allocate_ip_success_5g.append(int(random.randint(100,300)))
        release_ip_success_5g.append(int(random.randint(100,300)))
        counter += allocate_ip_success_5g[i]
        allocated_ip_count_5g.append(counter)

    df = pd.DataFrame(zip(timestamp, uplink_success_rate_5g, uplink_drop_rate_5g, downlink_success_rate_5g, downlink_drop_rate_5g, allocate_ip_success_5g, release_ip_success_5g, allocated_ip_count_5g),
                    columns=["timestamp", "uplink_success_rate_5g", "uplink_drop_rate_5g", "downlink_success_rate_5g", "downlink_drop_rate_5g", "allocate_ip_success_5g", "release_ip_success_5g", "allocated_ip_count_5g"])
    
    timestamp_str = start_timestamp.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"link_ip_rate_5g_{timestamp_str}.csv"

    df.to_csv(filename, index=False)

    return filename