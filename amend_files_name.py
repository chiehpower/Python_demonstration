import os

def batch_rename(path):
    count = 0
    total = len(os.listdir(path))
    
    for fname in os.listdir(path):
        time = total - len(str(count))
        Extension = fname.split('.')[-1]
        new_fname = str(0*(time)) + str(count) + '.' + Extension
        print(os.path.join(path, fname), ' New file name >>> ', new_fname)
        os.rename(os.path.join(path, fname), os.path.join(path, new_fname))
        count = count + 1  

path = input("Your data folder location")
# path = './dataset'
batch_rename(str(path))
