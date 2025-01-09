import pandas as pd
import time
from ExampleDiagnosisSystem import ExampleDiagnosisSystem # Change this line to use your own diagnosis system
import sys
import os

TIMEOUT = 0.1

# Create diagnosis system
ds = ExampleDiagnosisSystem() # Change this line to use your own diagnosis system

# Load test data
if len(sys.argv) != 2:
    print("Usage: python run_diagnoser.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
test_data = pd.read_csv(input_file, sep=';')

# Log diagnosis output
output_file = os.path.join('results', 'output_' + os.path.basename(input_file))
filehandler = open(output_file, 'w')

# Write header
header = 'sample_time;computation_time;fault_detection;' + ';'.join([f'fault_isolation_{i}' for i in range(ds.n_faults)]) + ';cyber_detection;' + ';'.join([f'cyber_isolation_{i}' for i in range(ds.n_loops)]) + '\n'
filehandler.write(header)

for time_idx in range(len(test_data)):
    t = time.time()

    # Feed sample to diagnosis system and return diagnosis output
    sample = test_data.iloc[time_idx, :].to_frame().transpose()
    fault_detection, fault_isolation, cyber_detection, cyber_isolation = ds.diagnose_sample(sample)
    
    elapsed = time.time() - t
    
    # Log diagnosis output
    filehandler.write('%f;%f;%d;%s;%d;%s\n' % (
        test_data['t'][time_idx], 
        elapsed, 
        fault_detection, 
        ';'.join(map(str, fault_isolation)), 
        cyber_detection, 
        ';'.join(map(str, cyber_isolation))
    ))

    if elapsed > TIMEOUT and time_idx > 5:
        print(f"Timeout at time index {time_idx} ({test_data['time'][time_idx]})")
        break

    # Print progress
    if time_idx % 1000 == 0:
        print('.', end="", flush=True)
    
# Close logger
filehandler.close()