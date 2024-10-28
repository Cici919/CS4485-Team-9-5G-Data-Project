import os
import time
import subprocess
import logging
from datetime import datetime, timezone

# Setup logging
logging.basicConfig(level=logging.INFO)

# Define the path to the generator scripts
script_directory = './generator_scripts/'

# List of generator scripts to run
scripts = [
    'gen_downlink_metrics.py',
    'gen_uplink_metrics.py'
    # Add more scripts as needed
]

def run_generator_scripts():
    while True:
        for script in scripts:
            # Construct the full path to the script
            script_path = os.path.join(script_directory, script)
            logging.info(f"Starting script: {script} at {datetime.now(timezone.utc)} UTC")
            try:
                # Run the script
                subprocess.run(['python', script_path], check=True)
                logging.info(f"Completed script: {script} at {datetime.now(timezone.utc)} UTC")
            except subprocess.CalledProcessError as e:
                logging.error(f"Error running {script}: {e}")
        
        # Sleep for 5 minutes
        time.sleep(300)

if __name__ == "__main__":
    run_generator_scripts()
