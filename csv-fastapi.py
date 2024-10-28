from prometheus_client import generate_latest, Gauge
import time
import os
from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse
import random
import uvicorn
from faker import Faker
import csv
import sys
from datetime import datetime, timedelta

from generationscripts.gen_downlink_5g_metrics import *
from generationscripts.gen_downlink_metrics import *
from generationscripts.gen_link_ip_rate_5g_metrics import *
from generationscripts.gen_machine_metrics import *
from generationscripts.gen_ue_queries_metrics import *
from generationscripts.gen_uplink_5g_metrics import *
from generationscripts.gen_uplink_metrics import *

app = FastAPI()
fake = Faker()

filename = ""
numRows = 300 #1 row per second, 300 rows = 5 minutes
#global rowsIndex
rowsIndex = 300

dlindex = 0
dl5gindex = 0
lir5gindex = 0
mmindex = 0
uqindex = 0
ulindex = 0
ul5gindex = 0

downlink_5g_gauges = {
    #'timestamp': Gauge('timestamp', 'time'),
    'downlink_sent_bytes_5g': Gauge('downlink_sent_bytes_5g', 'Downlink bytes sent in 5G'),
    'downlink_received_bytes_5g': Gauge('downlink_received_bytes_5g', 'Downlink bytes received in 5G'),
    'downlink_sent_packets_5g': Gauge('downlink_sent_packets_5g', 'Downlink packets sent in 5G'),
    'downlink_received_packets_5g': Gauge('downlink_received_packets_5g', 'Downlink packets received in 5G'),
    'downlink_sent_packets_dropped_5g': Gauge('downlink_sent_packets_dropped_5g', 'Downlink packets sent but dropped in 5G'),
    'downlink_received_packets_dropped_5g': Gauge('downlink_received_packets_dropped_5g', 'Downlink packets received but dropped in 5G')
}

downlink_gauges = {
    #'timestamp': Gauge('timestamp', 'time'),
    'downlink_sent_bytes': Gauge('downlink_sent_bytes', 'Downlink bytes sent'),
    'downlink_received_bytes': Gauge('downlink_received_bytes', 'Downlink bytes received'),
    'downlink_sent_packets': Gauge('downlink_sent_packets', 'Downlink packets sent'),
    'downlink_received_packets': Gauge('downlink_received_packets', 'Downlink packets received'),
    'downlink_sent_packets_dropped': Gauge('downlink_sent_packets_dropped', 'Downlink packets sent but dropped'),
    'downlink_received_packets_dropped': Gauge('downlink_received_packets_dropped', 'Downlink packets received but dropped')
}

link_ip_rate_5g_gauges = {
    #'timestamp': Gauge('timestamp', 'time'),
    'uplink_success_rate_5g': Gauge('uplink_success_rate_5g', 'Uplink success rate in 5G'),
    'uplink_drop_rate_5g': Gauge('uplink_drop_rate_5g', 'Uplink drop rate in 5G'),
    'downlink_success_rate_5g': Gauge('downlink_success_rate_5g', 'Downlink success rate in 5G'),
    'downlink_drop_rate_5g': Gauge('downlink_drop_rate_5g', 'Downlink drop rate in 5G'),
    'allocate_ip_success_5g': Gauge('allocate_ip_success_5g', 'Successful IP allocations in 5G'),
    'release_ip_success_5g': Gauge('release_ip_success_5g', 'Successful IP releases in 5G'),
    'allocated_ip_count_5g': Gauge('allocated_ip_count_5g', 'Count of allocated IPs in 5G')
}

machine_metric_gauges = {
    #'timestamp' : Gauge('timestamp', 'time'),
    'cpu_percent': Gauge('cpu_percent', 'CPU percentage'),
    'mem_used_bytes': Gauge('mem_used_bytes', 'Memory used in bytes'),
    'mem_total': Gauge('mem_total', 'Total memory'),
    'disk_percent': Gauge('disk_percent', 'Disk percentage'),
    'disk_total': Gauge('disk_total', 'Total disk space'),
    'sent_bytes' : Gauge("sent_bytes", "Bytes sent"),
    'received_bytes' : Gauge("received_bytes", "Bytes received"),
    'radio_connected' : Gauge("radio_connected", "Radio connections status"),
    'devices_registered' : Gauge("devices_registered", "Number of registered devices"),
    'devices_connected' : Gauge("devices_connected", "Number of connected devices"),
    'ue_pdn_connections_success' : Gauge("ue_pdn_connections_success", "Successful UE PDN connections"),
    'ue_pdn_connections_released' : Gauge("ue_pdn_connections_released", "Released UE PDN connections")
}

ue_queries_gauges = {
    #'timestamp': Gauge('timestamp', 'time'),
    'ue_sent_bytes': Gauge('ue_sent_bytes', 'ue bytes sent'),
    'ue_received_bytes': Gauge('ue_received_bytes', 'ue bytes received'),
    'ue_sent_packets': Gauge('ue_sent_packets', 'ue packets sent'),
    'ue_received_packets': Gauge('ue_received_packets', 'ue packets received'),
    'ue_sent_packets_dropped': Gauge('ue_sent_packets_dropped', 'ue packets sent but dropped'),
    'ue_received_packets_dropped': Gauge('ue_received_packets_dropped', 'ue packets received but dropped')
}

uplink_5g_gauges = {
    #'timestamp': Gauge('timestamp', 'time'),
    'uplink_sent_bytes_5g': Gauge('uplink_sent_bytes_5g', 'Uplink bytes sent in 5G'),
    'uplink_received_bytes_5g': Gauge('uplink_received_bytes_5g', 'Uplink bytes received in 5G'),
    'uplink_sent_packets_5g': Gauge('uplink_sent_packets_5g', 'Uplink packets sent in 5G'),
    'uplink_received_packets_5g': Gauge('uplink_received_packets_5g', 'Uplink packets received in 5G'),
    'uplink_sent_packets_dropped_5g': Gauge('uplink_sent_packets_dropped_5g', 'Uplink packets sent but dropped in 5G'),
    'uplink_received_packets_dropped_5g': Gauge('uplink_received_packets_dropped_5g', 'Uplink packets received but dropped in 5G')
}

uplink_gauges = {
    #'timestamp' : Gauge('timestamp', 'time'),
    'uplink_sent_bytes' : Gauge('uplink_sent_bytes', 'uplink_sent_bytes'),
    'uplink_received_bytes' : Gauge('uplink_received_bytes', 'uplink_received_bytes'),
    'uplink_sent_packets' : Gauge('uplink_sent_packets', 'uplink_sent_packets'),
    'uplink_received_packets' : Gauge('uplink_received_packets', 'uplink_received_packets'),
    'uplink_sent_packets_dropped' : Gauge('uplink_sent_packets_dropped', 'uplink_sent_packets_dropped'),
    'uplink_received_packets_dropped' : Gauge('uplink_received_packets_dropped', 'uplink_received_packets_dropped')
}

metrics_files = {
    'downlink_5g': (generate_downlink_5g_metrics(numRows), downlink_5g_gauges),
    'downlink': (generate_downlink(numRows), downlink_gauges),
    'link_ip_rate_5g': (generate_link_ip_rate_5g(numRows), link_ip_rate_5g_gauges),
    'machine_metrics': (generate_machine_metrics(numRows), machine_metric_gauges),
    'ue_queries': (generate_ue_queries(numRows), ue_queries_gauges),
    'uplink_5g': (generate_uplink_5g(numRows), uplink_5g_gauges),
    'uplink': (generate_uplink_data(numRows), uplink_gauges),
}

def load_metrics_from_csv(filename, gauges, index):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"CSV file '{filename}' not found.")

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if index < len(rows):
            current_row = rows[index]
            for key, gauge in gauges.items():
                #print(gauge)
                gauge.set(float(current_row[key]))
            index += 1
            return index
        else:
            index = 0
            return index

@app.get("/metrics")
async def metrics():
    global fnDownlink5g, fnDownlink, fnLinkIpRate5g, fnMachineMetrics, fnUEQueries, fnUplink5g, fnUplink
    global rowsIndex, dlindex, dl5gindex, lir5gindex, mmindex, uqindex, ul5gindex, ulindex
    if rowsIndex == numRows:
        fnDownlink5g = generate_downlink_5g_metrics(numRows)
        fnDownlink = generate_downlink(numRows)
        fnLinkIpRate5g = generate_link_ip_rate_5g(numRows)
        fnMachineMetrics = generate_machine_metrics(numRows)
        fnUEQueries = generate_ue_queries(numRows)
        fnUplink5g = generate_uplink_5g(numRows)
        fnUplink = generate_uplink_data(numRows)
        rowsIndex = 0
    dlindex = load_metrics_from_csv(fnDownlink5g, downlink_5g_gauges, dlindex)
    dl5gindex = load_metrics_from_csv(fnDownlink, downlink_gauges, dl5gindex)
    lir5gindex = load_metrics_from_csv(fnLinkIpRate5g, link_ip_rate_5g_gauges, lir5gindex)
    mmindex = load_metrics_from_csv(fnMachineMetrics, machine_metric_gauges, mmindex)
    uqindex = load_metrics_from_csv(fnUEQueries, ue_queries_gauges, uqindex)
    ulindex = load_metrics_from_csv(fnUplink5g, uplink_5g_gauges, ulindex)
    ul5gindex = load_metrics_from_csv(fnUplink, uplink_gauges, ul5gindex)
    rowsIndex += 1
    return Response(content=generate_latest(), media_type="text/plain")

@app.get("/")
async def index():
    return "Prometheus Test Target is running, /metrics to see the metrics"

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
