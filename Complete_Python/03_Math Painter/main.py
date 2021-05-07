import numpy as np
from PIL import Image

# Create 3d numpy array of zeros, then replace zeros (black pixels) with yellow pixels
data = np.zeros((5,4,3), dtype = np.uint8)
data[:] = [255, 255, 0]
print(data)

#Make a red patch
data[1:4,1:3] = [255, 0, 0]
#or like this one
data[3:4, 1:4] = [45, 3, 233]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')