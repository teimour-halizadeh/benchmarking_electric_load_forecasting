

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



model_name = 'Crossformer'




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
            '--label_len', str(48),  
            '--pred_len', str(pred_len),
            '--e_layers', str(2), 
            '--d_layers', str(1),  
            '--factor', str(3),  
            '--enc_in', str(DATA_SET[1]),
            '--dec_in', str(DATA_SET[1]),
            '--c_out', str(DATA_SET[1]),
            '--d_model', str(256),
            '--d_ff', str(512),
            '--top_k', str(5),  
            '--des', 'Exp',
            '--batch_size', str(16),
            '--itr', str(NUM_EXPERIMENT)
        ]

        # create a specific log_file for the experiment
        log_file = os.path.join(LOG_DIR,   f"{model_name}_I_{DATA_SET[0].split('.')[0]}_{seq_len}_{pred_len}.log")
        with open(log_file, 'w') as f:
            subprocess.run(cmd, stdout=f)

