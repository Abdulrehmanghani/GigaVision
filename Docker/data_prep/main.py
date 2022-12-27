
import os
from subprocess import Popen, PIPE

import logging
Log_Format = "%(levelname)s %(asctime)s - %(message)s"

def setup_logger(filename):
    logging.basicConfig(filename = filename,
                    filemode = "a+",
                    format = Log_Format,
                    level = logging.INFO)

    logger = logging.getLogger()
    return logger
    
def run_process_2(cmd, prefix=None, suffix=None, cwd = None,use_pipe=False, use_shell = False):
    if cwd == None:
        cwd = os.getcwd()
    print("Running process with command: {}".format(cmd),flush=True)
    cmd_pcs = cmd.split()

    p = Popen(cmd_pcs, cwd = cwd, 
            stdout = PIPE if use_pipe else None,
            stderr = PIPE if use_pipe else None,
            shell = use_shell)

    return p
    
all_process={}
p_id=0
logger = setup_logger("log.txt")

logger.info("Starting data prepration")
p = run_process_2("python create_tracking_csv.py")

all_process["P{}".format(p_id)] = [p, True]
p.wait()        
logger.info('Tracking data csv created successfully')

p_id = p_id +1
p = run_process_2("python csv_to_json.py")

all_process["P{}".format(p_id)] = [p, True]
p.wait()        
logger.info('Tracking data json created successfully')

p_id = p_id +1
p = run_process_2("python split_annotation_json.py")

all_process["P{}".format(p_id)] = [p, True]
p.wait()        
logger.info('Tracking data split successfully')

p_id = p_id +1
p = run_process_2("python visualize_json.py")

all_process["P{}".format(p_id)] = [p, True]
p.wait()        
logger.info('Tracking data visualize successfully')