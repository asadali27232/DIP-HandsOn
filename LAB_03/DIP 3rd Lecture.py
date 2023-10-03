# %% [markdown]
# # Lecture 3: Digital Image Processing
# 
# ### Introduction: Gray Scale Images, Quantization and Color Channels
# 

# %% [markdown]
# <h2>Objectives</h2>
# 

# %% [markdown]
# Image processing and computer vision tasks include displaying, cropping, flipping, rotating, image segmentation, classification, image restoration, image recognition, image generation. Also, working with images via the cloud requires storing, transmitting, and gathering images through the internet.
# 
# Python is an excellent choice as it has many image processing tools, computer vision and artificial intelligence libraries. Finally, it has many libraries for working with files in the cloud and on the internet.
# 
# A digital image is simply a file in your computer. In this lab, you will gain an understanding of these files and learn to work with these files with the Pillow Library (PIL).
# 

# %% [markdown]
# <ul>
#     <li><a href='#PIL'>Python Image Libraries </a>
#         <ul>
#             <li>Image Files and Paths  </li>
#             <li>Load in Image in Python</li>
#             <li>Plotting an Image </li>
#             <li>Gray Scale Images, Quantization and Color Channels  </li>
#             <li> PIL Images into NumPy Arrays  </li>
#         </ul>
#     </li>
#     
# </ul>
# 

# %% [markdown]
# ---
# 

# %% [markdown]
# First, let's define a helper function to concatenate two images side-by-side. You will not need to understand the code below at this moment, but this function will be used repeatedly in this tutorial to showcase the results.
# 

# %%
def get_concat_h(im1, im2):
    dst = Image.new("RGB", (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

# %% [markdown]
# ## Image Files and Paths
# 

# %% [markdown]
# An image is stored as a file on your computer. Below, we define `my_image` as the filename of a file in this directory.
# 

# %%
my_image = "lenna.png"

# %% [markdown]
# A filename consists of two parts: the name of the file and the extension, separated by a full stop (`.`). The extension specifies the format of the Image. There are two popular image formats: Joint Photographic Expert Group image (or `.jpg`, `.jpeg`) and Portable Network Graphics (or `.png`). These file types make it simpler to work with images. For example, it compresses the image, taking less spaces on your drive to store the image.
# 

# %% [markdown]
# Image files are stored in the file system of your computer. The location of it is specified using a "path", which is often unique. You can find the path of your current working directory with Python's `os` module. The `os` module provides functions to interact with the file system, e.g. creating or removing a directory (folder), listing its contents, changing and identifying the current working directory.
# 

# %%
import os

cwd = os.getcwd()
cwd

# %% [markdown]
# The "path" to an image can be found using the following line of code.
# 

# %%
image_path = os.path.join(cwd, my_image)
image_path

# %% [markdown]
# ## Load Images in Python
# 

# %% [markdown]
# Pillow (PIL) library is a popular library for loading images in Python. In addition, many other libraries such as "Keras" and "PyTorch" use this library to work with images. The `Image` module provides functions to load images from and saving images to the file system. Let's import it from `PIL`.
# 

# %%
from PIL import Image

# %% [markdown]
# If the image is in the current working directory, you can load the image as follows using the image's filename and create a PIL Image object:
# 

# %%
image = Image.open(my_image)
type(image)

# %% [markdown]
# If you are working in a Jupyter environment, you can view the image by calling the variable itself.
# 

# %%
image

# %% [markdown]
# ## Plotting an Image
# 

# %% [markdown]
# We can also use the method `show` of PIL objects to display the image. Please note this method may or may not work depending on your setup.
# 

# %%
image.show()

# %% [markdown]
# You can also use <code>imshow</code> method from the <code>matplotlib</code> library to display the image.
# 

# %%
import matplotlib.pyplot as plt

# %%
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.show()

# %% [markdown]
# You can also load the image using its full path. This comes in handy if the image is not in your working directory.
# 

# %%
image = Image.open(image_path)

# %% [markdown]
# We can use the attributes of the image object to get information. The attribute format is the extension or format of the image.
# 

# %% [markdown]
# The attribute `size` returns a tuple, the first element is the number of pixels that comprise the width and the second element is the number of pixels that make up the height of the image.
# 

# %%
print(image.size)

# %% [markdown]
# This is a string specifying the pixel format used. In this case, it's “RGB”. RGB is a color space where red, green, and blue are added together to produce other colors.
# 

# %%
print(image.mode)

# %% [markdown]
# The `Image.open` method does not load image data into the computer memory. The `load` method of `PIL` object reads the file content, decodes it, and expands the image into memory.
# 

# %%
im = image.load()

# %% [markdown]
# We can then check the intensity of the image at the $x$-th column and $y$-th row:
# 

# %%
x = 0
y = 1
im[y, x]

# %% [markdown]
# We will use the array form to access the elements; it is slightly different.
# 

# %% [markdown]
# You can save the image in `jpg` format using the following command.
# 

# %%
image.save("lenna.jpg")

# %% [markdown]
# ## Grayscale Images, Quantization and Color Channels
# 

# %% [markdown]
# ### Grayscale Images
# 

# %% [markdown]
# The `ImageOps` module contains several ‘ready-made’ image processing operations. This module is somewhat experimental, and most operators only work with grayscale and/or RGB images.
# 

# %%
from PIL import ImageOps

# %% [markdown]
# Grayscale images have pixel values representing the amount of light or intensity of that pixel. Light shades of gray have a high-intensity while darker shades have a lower intensity, i.e, white has the highest intensity and black the lowest.
# 

# %%
image_gray = ImageOps.grayscale(image)
image_gray

# %% [markdown]
# The mode is `L` for grayscale.
# 

# %%
image_gray.mode

# %% [markdown]
# ### Quantization
# 

# %% [markdown]
# The Quantization of an image is the number of unique intensity values any given pixel of the image can take. For a grayscale image, this means the number of different shades of gray. Most images have 256 different levels. You can decrease the levels using the method `quantize`. Let's repeatably cut the number of levels in half and observe what happens:
# 

# %% [markdown]
# Half the levels do not make a noticable difference.
# 

# %%
image_gray.quantize(256 // 2)
image_gray.show()

# %% [markdown]
# Let’s continue dividing the number of values by two and compare it to the original image.
# 

# %%
# get_concat_h(image_gray,  image_gray.quantize(256//2)).show(title="Lena")
for n in range(3, 8):
    plt.figure(figsize=(10, 10))

    plt.imshow(get_concat_h(image_gray, image_gray.quantize(256 // 2**n)))
    plt.title("256 Quantization Levels  left vs {}  Quantization Levels right".format(256 // 2**n))
    plt.show()

# %% [markdown]
# ### Color Channels
# 

# %% [markdown]
# We can also work with the different color channels. Consider the following image:
# 

# %%
baboon = Image.open("baboon.png")
baboon

# %% [markdown]
# We can obtain the different RGB color channels and assign them to the variables <code>red</code>, <code>green</code>, and <code>blue</code>:
# 

# %%
red, green, blue = baboon.split()

# %% [markdown]
# Plotting the color image next to the red channel as a grayscale, we see that regions with red have higher intensity values.
# 

# %%
get_concat_h(baboon, red)

# %% [markdown]
# We can do the same for the blue and green channels:
# 

# %%
get_concat_h(baboon, blue)

# %%
get_concat_h(baboon, green)

# %% [markdown]
# ## PIL Images into NumPy Arrays
# 

# %% [markdown]
# NumPy is a library for Python, allowing you to work with multi-dimensional arrays and matrices. We can convert a PIL image to a NumPy array. We use <code>asarray()</code> or <code>array</code> function from NumPy to convert PIL images into NumPy arrays.
# 
# First, let's import the numpy module:
# 

# %%
import numpy as np

# %% [markdown]
# We apply it to the <code>PIL</code> image we get a numpy array:
# 

# %%
array = np.asarray(image)
print(type(array))

# %% [markdown]
# `np.asarray` turns the original image into a numpy array. Often, we don't want to manipulate the image directly, but instead, create a copy of the image to manipulate. The `np.array` method creates a new copy of the image, such that the original one will remain unmodified.
# 

# %%
array = np.array(image)

# %% [markdown]
# The attribute <code>shape</code> of a `numpy.array` object returns a tuple corresponding to the dimensions of it, the first element gives the number of rows or height of the image, the second is element is the number of columns or width of the image. The final element is the number of colour channels.
# 

# %%
# summarize shape
print(array.shape)

# %% [markdown]
# or <code>(rows, columns, colors)</code>. Each element in the color axis corresponds to the following value <code>(R, G, B)</code> format.
# 

# %% [markdown]
# We can view the intensity values by printing out the array, they range from 0 to 255 or $2^{8}$ (8-bit).
# 

# %%
print(array)

# %% [markdown]
# The Intensity values are 8-bit unsigned datatype.
# 

# %%
array[0, 0]

# %% [markdown]
# We can find the maximum and minimum intensity value of the array:
# 

# %%
array.min()

# %%
array.max()

# %% [markdown]
# ### Indexing
# 

# %% [markdown]
# You can plot the array as an image:
# 

# %%
plt.figure(figsize=(10, 10))
plt.imshow(array)
plt.show()

# %% [markdown]
# We can use numpy slicing, for example, we can return the first 256 rows corresponding to the top half of the image:
# 

# %%
rows = 256

# %%
plt.figure(figsize=(10, 10))
plt.imshow(array[0:rows, :, :])
plt.show()

# %% [markdown]
# We can also return the first 256 columns corresponding to the first half of the image.
# 

# %%
columns = 256

# %%
plt.figure(figsize=(10, 10))
plt.imshow(array[:, 0:columns, :])
plt.show()

# %% [markdown]
# If you want to reassign an array to another variable, you should use the `copy` method (we will cover this in the next section).
# 

# %%
A = array.copy()
plt.imshow(A)
plt.show()

# %% [markdown]
# If we do not apply the method copy(), the variable will point to the same location in memory. Consider the array B. If we set all values of array A to zero, as B points to A, the values of B will be zero too:
# 

# %%
B = A
A[:, :, :] = 0
plt.imshow(B)
plt.show()

# %% [markdown]
# We can also work with the different color channels. Consider the baboon image:
# 

# %%
baboon_array = np.array(baboon)
plt.figure(figsize=(10, 10))
plt.imshow(baboon_array)
plt.show()

# %% [markdown]
# We can plot the red channel as intensity values of the red channel.
# 

# %%
baboon_array = np.array(baboon)
plt.figure(figsize=(10, 10))
plt.imshow(baboon_array[:, :, 0], cmap="gray")
plt.show()

# %% [markdown]
# Or we can create a new array and set all but the red color channels to zero. Therefore, when we display the image it appears red:
# 

# %%
baboon_red = baboon_array.copy()
baboon_red[:, :, 1] = 0
baboon_red[:, :, 2] = 0
plt.figure(figsize=(10, 10))
plt.imshow(baboon_red)
plt.show()

# %% [markdown]
# We can do the same for blue:
# 

# %%
baboon_blue = baboon_array.copy()
baboon_blue[:, :, 0] = 0
baboon_blue[:, :, 1] = 0
plt.figure(figsize=(10, 10))
plt.imshow(baboon_blue)
plt.show()

# %% [markdown]
# ### Question 1:
# 
# Use the image `lenna.png` from this lab or take any image you like.
# 
# Open the image and create a PIL Image object called `blue_lenna`, convert the image into a numpy array we can manipulate called `blue_array`, get the blue channel out of it, and finally plot the image
# 

# %%
blue_lenna = Image.open("lenna.png")
blue_array = np.array(blue_lenna)
blue_array[:, :, 0] = 0
blue_array[:, :, 1] = 0
plt.imshow(blue_array)
plt.show()

# %% [markdown]
# # References
# 

# %% [markdown]
# [1] Images were taken from: https://homepages.cae.wisc.edu/~ece533/images/
# 
# [2] <a href='https://pillow.readthedocs.io/en/stable/index.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkCV0101ENCoursera872-2022-01-01'>Pillow Docs</a>
# 
# [3] <a href='https://opencv.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkCV0101ENCoursera872-2022-01-01'>Open CV</a>
# 
# [4] Gonzalez, Rafael C., and Richard E. Woods. "Digital image processing." (2017).
# 


