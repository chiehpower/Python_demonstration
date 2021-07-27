"""
The method is not using the python library. 
I wanna use the subprocess to take the value from terminal because python library cannot grab my gpu information 
because gpu is using MIG technique. 
"""
import subprocess

def get_available_device(max_memory=0.8):
    '''
    select available device based on the memory utilization status of the device
    :param max_memory: the maximum memory utilization ratio that is considered available
    :return: GPU id that is available, -1 means no GPU
    '''
    Total = subprocess.check_output("nvidia-smi -q | grep \"Total\"", shell=True)
    Total_gpu = int([a for a in str(Total).split(' ') if a != ''][3])

    Used = subprocess.check_output("nvidia-smi -q | grep \"Used\"", shell=True)
    Used_gpu = int([a for a in str(Used).split(' ') if a != ''][3])

    available=-1

    memoryUtil = float(Used_gpu / Total_gpu)
    if memoryUtil > max_memory:
        return available
    else:
        return memoryUtil

print(get_available_device(0.8))