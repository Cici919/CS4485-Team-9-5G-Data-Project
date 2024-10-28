import random
from datetime import datetime, timedelta
import pandas as pd

def generate_machine_metrics(numRows):
    start_timestamp = datetime.now()

    timestamp = []
    cpu_percent = []
    mem_used_bytes = []
    mem_total = []
    disk_percent = []
    disk_total = []
    sent_bytes = []
    received_bytes = []
    radio_connected = []
    devices_registered = []
    devices_connected = []
    ue_pdn_connections_success = []
    ue_pdn_connections_released = []

    for i in range(numRows):
        timestamp.append(start_timestamp + timedelta(minutes=i*5))
        cpu_percent.append(round(random.uniform(0.6, 0.9), 2))
        mem_used_bytes.append(int(536870912 * random.uniform(0.7, 0.99)))
        mem_total.append(536870912)
        disk_percent.append(round(random.uniform(0.6, 0.9), 2))
        disk_total.append(536870912)
        sent_bytes.append(int(536870912 * random.uniform(0.1, 0.7) / 15))
        received_bytes.append(int(536870912 * random.uniform(0.1, 0.7)))
        radio_connected.append(random.randint(50, 100))
        devices_registered.append(random.randint(500, 700))
        devices_connected.append(random.randint(400, 800))
        ue_pdn_connections_success.append(random.randint(100, 300))
        ue_pdn_connections_released.append(random.randint(100, 300))
        
    df = pd.DataFrame(zip(timestamp, cpu_percent, mem_used_bytes, mem_total, disk_percent, disk_total, sent_bytes, received_bytes, radio_connected, devices_registered, devices_connected, ue_pdn_connections_success, ue_pdn_connections_released),
                    columns=["timestamp", "cpu_percent", "mem_used_bytes", "mem_total", "disk_percent", "disk_total", "sent_bytes", "received_bytes", "radio_connected", "devices_registered", "devices_connected", "ue_pdn_connections_success", "ue_pdn_connections_released"])
    
    timestamp_str = start_timestamp.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"machine_metrics_{timestamp_str}.csv"

    df.to_csv(filename, index=False)

    return filename