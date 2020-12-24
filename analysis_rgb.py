# # cspace.py
# import streamlit as st
# import cv2
import numpy as np


# ori = cv2.imread('cat.jpg')
# image = cv2.cvtColor(ori, cv2.COLOR_RGB2BGR)
# st.image(image, use_column_width=True)

# ## Red
# ## set green and red channels to 0
# r = image.copy()
# r[:, :, 1] = 0
# r[:, :, 2] = 0
# st.image(r, use_column_width=True)

# ## Green
# ## set blue and red channels to 0
# g = image.copy()
# g[:, :, 0] = 0
# g[:, :, 2] = 0
# st.image(g, use_column_width=True)

# ## Blue 
# ## set red and green channels to 0
# b = image.copy()
# b[:, :, 0] = 0
# b[:, :, 1] = 0
# st.image(b, use_column_width=True)

# # in CV2 : BGR

############################################

if __name__ == '__main__':
    import imageio
    import matplotlib.pyplot as plt

    pic = imageio.imread('/home/chieh/programme/cat.jpg')
    plt.figure()
    plt.imshow(pic)
    plt.savefig('save_img.jpg')
    # plt.show()
    print('Type of the image : ' , type(pic))
    print()
    print('Shape of the image : {}'.format(pic.shape))
    print('Image Hight {}'.format(pic.shape[0]))
    print('Image Width {}'.format(pic.shape[1]))
    print('Dimension of Image {}'.format(pic.ndim))

    print('Image size {}'.format(pic.size))
    print('Maximum RGB value in this image {}'.format(pic.max()))
    print('Minimum RGB value in this image {}'.format(pic.min()))

    # Let's pick a specific pixel located at 100 th Rows and 50 th Column. 
    # And view the RGB value gradually.
    print(pic[ 100, 50 ])
    a = pic[ 100, 50 ]
    ## Output: [24 20 17] > R = 24；G = 20；B = 17

    # A specific pixel located at Row : 100 ; Column : 50 
    # Each channel's value of it, gradually R , G , B
    print('Value of only R channel {}'.format(pic[ 100, 50, 0]))
    print('Value of only G channel {}'.format(pic[ 100, 50, 1]))
    print('Value of only B channel {}'.format(pic[ 100, 50, 2]))

    # plt.title('R channel')
    # plt.ylabel('Height {}'.format(pic.shape[0]))
    # plt.xlabel('Width {}'.format(pic.shape[1]))

    # plt.imshow(pic[ : , : , 0])
    # plt.show()

    # plt.title('G channel')
    # plt.ylabel('Height {}'.format(pic.shape[0]))
    # plt.xlabel('Width {}'.format(pic.shape[1]))

    # plt.imshow(pic[ : , : , 1])
    # plt.show()

    # plt.title('B channel')
    # plt.ylabel('Height {}'.format(pic.shape[0]))
    # plt.xlabel('Width {}'.format(pic.shape[1]))

    # plt.imshow(pic[ : , : , 2])
    # plt.show()


    # pic = imageio.imread('cat.jpg')
    # pic[50:150 , : , 0] = 255 # full intensity to those pixel's R channel
    # plt.figure( figsize = (10,10))
    # plt.imshow(pic)
    # plt.show()

    pic[ : , : , 1] = 0
    pic[ : , : , 2] = 0
    # a = np.mean(np.array(pic[ : , : , 0]))
    a = np.mean(pic[ : , : , 0])
    print(a)
    b = np.mean(pic[ 100 , 50 , 0])
    print(b)
    # plt.imshow(pic)
    # plt.show()


    ###
    
    # pic = imageio.imread('cat.jpg')

    # fig, ax = plt.subplots(nrows = 1, ncols=3, figsize=(15,5))

    # for c, ax in zip(range(3), ax):
        
    #     # create zero matrix
    #     split_img = np.zeros(pic.shape, dtype="uint8") # 'dtype' by default: 'numpy.float64'
        
    #     # assing each channel 
    #     print(c)
    #     split_img[ :, :, c] = pic[ :, :, c]
        
    #     # display each channel
    #     ax.imshow(split_img)
    # plt.show()