print('Import Libraries...')
import onnxruntime as rt
import numpy as np

def write_the_config(inputlist, outlist, folder_name):

    f2 = open('config.pbtxt', 'w')
    f2.write('name : \"{}\" \n'.format(folder_name))
    f2.write('platform: \"tensorrt_plan\" \n')
    f2.write('max_batch_size: 1 \n \n')
    ## Input part.
    f2.write('input [ \n')
    f2.write('  { \n')
    f2.write('    name: \"{}\" \n'.format(list(inputlist.keys())[0]))
    f2.write('    data_type: TYPE_FP32 \n')
    f2.write('    dims: {} \n'.format(list(inputlist.values())[0]))
    f2.write('  } \n')
    f2.write('] \n \n')

    ## Output part.
    f2.write('output [ \n')
    total = len(outlist)
    for i in range(total):
        f2.write('{\n')

        f2.write('    name: \"{}\" \n'.format(list(outlist.keys())[i]))
        f2.write('    data_type: TYPE_FP32 \n')
        f2.write('    dims: {} \n'.format(list(outlist.values())[i]))

        if i != (total-1):
            f2.write('  },\n')
        else:
            f2.write('  }\n')


    f2.write('] \n \n')
    f2.write('instance_group [ \n')
    f2.write('  { \n')
    f2.write('    count: 2 \n')
    f2.write('    kind: KIND_GPU \n')
    f2.write('  } \n')
    f2.write('] \n')
    f2.close()

    
if __name__ == "__main__":

    folder_name = '' # model name
    model_path = '' # your model path

    print('Define session onnxruntime...')
    sess = rt.InferenceSession(model_path)
    print(sess.get_providers())

    print('Define session input name...')
    input1 = sess.get_inputs()[0].name
    outputlist = sess.get_outputs()

    input1_shape = list(sess.get_inputs()[0].shape)
    a = input1_shape[0]
    b = input1_shape[1]
    c = input1_shape[2]
    d = input1_shape[3]
    
    img_preprocess = (np.random.rand(a,b,c,d)*255).astype(np.float32)
    print("img_preprocess", img_preprocess.shape, "img_preprocess", img_preprocess.dtype)
    print('Run sess.run...')
    outputs = sess.run(None, {input1: img_preprocess})

    print("{} Shape: {}".format(input1, img_preprocess.shape))
    
    inputlist = {input1: list(img_preprocess.shape)}
    outlist = {'{}'.format(outputlist[i].name): list(outputs[i].shape) for i in range(len(outputs))}
    print("outlist", outlist)

    for i in range(len(outputs)):
        print("{}: {}".format(outputlist[i].name, outputs[i].shape))

    print("Generate the config file.")
    write_the_config(inputlist, outlist, folder_name)