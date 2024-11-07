

"""
This script repeats for num of experiments  the experiments that we have in the 
TSLIB with the same parameters. 
 """



import os 
import subprocess

# Meta parameters for models
from constants import DATA_SET, PRED_LENS, SEQ_LENS, NUM_EXPERIMENT
from constants import LOG_DIR







# Define the log file path
os.makedirs(LOG_DIR, exist_ok=True)



model_name = 'DLinear'




 # loop over the combination
for seq_len in SEQ_LENS:
    for pred_len in PRED_LENS:
        cmd = [
            'python', './run.py',
            '--task_name', 'long_term_forecast',
            '--is_training', '1',
            '--root_path', './dataset/',
            '--data_path', DATA_SET[0],
            '--model_id', f"{DATA_SET[0].split('.')[0].replace('_', '')}_{seq_len}_{pred_len}",
            '--model', model_name,
            '--data', 'custom',
            '--features', 'M',
            '--seq_len', str(seq_len),
            '--label_len', str(48),  # Assuming this stays constant
            '--pred_len', str(pred_len),
            '--e_layers', str(2),  # Added e_layers parameter
            '--d_layers', str(1),  # Added d_layers parameter
            '--factor', str(3),  # Assuming the factor stays constant
            '--enc_in', str(DATA_SET[1]),
            '--dec_in', str(DATA_SET[1]),
            '--c_out', str(DATA_SET[1]),  # You used c_out as 321 before
            '--des', 'Exp',
            '--itr', str(NUM_EXPERIMENT)
        ]

        # create a specific log_file for the experiment
        log_file = os.path.join(LOG_DIR,   f"{model_name}_I_{DATA_SET[0].split('.')[0]}_{seq_len}_{pred_len}.log")
        with open(log_file, 'w') as f:
            subprocess.run(cmd, stdout=f)

