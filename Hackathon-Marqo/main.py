from multiprocessing import process
from Processor.simple_script_processor import process_simple_scripts
from Processor.vehicle_processor import process_vehicle_queries
import marqo

print("Application initialising.")

# Initialise Client
mq = marqo.Client(url="http://localhost:8882")

# Run processors
# process_simple_scripts(mq)
process_vehicle_queries(mq)

print("Application closing.")

