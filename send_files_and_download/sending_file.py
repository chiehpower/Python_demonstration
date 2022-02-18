import requests
import os

class WrapAndDownFiles(object):
    def __init__(self, server_ip):
        self.server_ip = server_ip

    def send(self, your_filename):

        url = 'http://'+ self.server_ip + ':5000/'

        zip_files = your_filename
        zip_files = str(zip_files)
        
        assert os.path.isfile(zip_files) == True, 'Check the zip file path.'

        files  = {'file': open(zip_files, 'rb')}

        # Because now we don't have second kind of tools, we set a default by the embedmask tool.
        config = {
            'arch' : 'x86_64',
            'filename' : 'test',
            'sofile': zip_files
        }
        result = requests.post(url, files=files, data=config, verify =False)
        
        file_name = 'file-{}.tar.gz'.format(config['filename'])
        print("file_name", file_name)
        with open(file_name, 'wb') as f:
            f.write(result.content)

wad = WrapAndDownFiles('0.0.0.0')
your_filename = 'test.txt'
wad.send(your_filename)