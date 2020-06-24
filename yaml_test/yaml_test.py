import yaml
import pickle 

with open("config.yaml", "r") as stream:
    data = yaml.load(stream, Loader=yaml.FullLoader)

### Test 1
IOUThreshold = data['Parameter']['Threshold']
print(IOUThreshold)

### Test 2
output_plt = data['Normal_ap_case']['output_plt']
print(output_plt)

### Test 3
showAP = data['Normal_ap_case']['showAP']
def test_showAP(showAP=False):
    if showAP:
        print("showAP: ",showAP)
    else:
        print("showAP is False ")
test_showAP(showAP=showAP)

assert IOUThreshold <= 1, "The value is bigger than 1."


fp = open('Config_Results.txt','w')
fp.write("Here is the yaml information:\n\n")
fp.close()

with open(r'Config_Results.txt', 'a') as file:
    documents = yaml.dump(data, file)
# for k,v in data.items():
#     	fp.write(str(k)+' '+str(v)+'\n')

# with open('Config_Results.txt', 'w') as file:
#      file.write(pickle.dumps(str(data)))

