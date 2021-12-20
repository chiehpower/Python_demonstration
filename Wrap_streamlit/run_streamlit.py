import subprocess
import streamlit

# subprocess.call(['streamlit', 'run', 'main.py'])

from multiprocessing import Process
def launchstreamlit():
    path = os.path.join(os.getcwd(),'./main.py --server.maxUploadSize=1028')
    start_streamlit = 'streamlit run ' + path
    subprocess.run(start_streamlit,shell=True)

stP = Process(target=launchstreamlit)
stP.start()
# launchstreamlit()