"""
Image processing

"""
from scipy import misc
lena = misc.face()
import matplotlib.pyplot as plt
plt.gray()
plt.imshow(lena)
plt.show()

import scipy.misc
face = scipy.misc.face()
print(face.shape)
print(face.max)
print(face.dtype)
# plt.axis("off")
plt.gray()
plt.imshow(face)
plt.show()


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('/Volumes/MyStuff/Abinesh/abinesh.jpg')
print img[:22]
imgplot = plt.imshow(img[0:22])

plt.axis("off")
imgplot = plt.imshow(img)
lum_img = img[:,:,1]
print(lum_img)

plt.axis("off")
imgplot = plt.imshow(lum_img)
