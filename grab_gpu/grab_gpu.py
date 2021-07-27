import GPUtil
def get_available_device(max_memory=0.8):
    '''
    select available device based on the memory utilization status of the device
    :param max_memory: the maximum memory utilization ratio that is considered available
    :return: GPU id that is available, -1 means no GPU is available/uses CPU, if GPUtil package is not installed, will
    return 0 
    '''
    GPUs = GPUtil.getGPUs() 
    freeMemory = 0
    available=-1
    for GPU in GPUs:
        print(GPU.memoryUtil)
        if GPU.memoryUtil > max_memory:
            continue
        if GPU.memoryFree >= freeMemory:
            freeMemory = GPU.memoryFree
            available = GPU.id
    return available 
print(get_available_device(0.5))