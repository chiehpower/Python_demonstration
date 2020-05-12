import yaml

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