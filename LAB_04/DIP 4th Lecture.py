# %% [markdown]
# # Lecture 4: Digital Image Processing
# 
# ### Line or Path Finding Algorithms using Neighbourhood and Adjaency Processing
# 

# %% [markdown]
# ## Objectives
# 
# - Creating a binary image using <code>numpy</code>
# - Show images using <code>matplotlib</code>
# - Writing function to find N4, N8 and ND neighbours of a pixel
# - Implimenting line or path finding algorithms using N4 and N8 neighbours and Adjaency Processing
# 

# %% [markdown]
# ---
# 

# %% [markdown]
# ### Helper Function
# 

# %%
def line_remover(image, line):
    image = image.copy()

    for p in line:
        image[p[0], p[1]] = 1

    return image

# %% [markdown]
# ### Importing Libraries
# 

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ### Creating a Binary Image
# 
# Create a binary images using <code>numpy</code> array. The image should be of size 300x300 and should have a straight line or path in it. The line or path should be of thickness 1 pixel and should be in the middle of the image.
# 

# %%
image = np.ones((300, 300))
image[:, 150] = 0

plt.imshow(image, cmap="gray")

# %% [markdown]
# ### Finding Neighbours
# 
# Write a functions to find N4, N8 and ND neighbours of a pixel. The function should take the pixel location. The function should return the N4, N8 or ND neighbours of the pixel.
# 

# %% [markdown]
# #### N4 Neighbours
# 

# %%
def get4_neighbours(p):
    # print(" ", image[p[0] - 1, p[1]])
    # print(image[p[0], p[1] - 1], image[p[0], p[1]], image[p[0], p[1] - 1])
    # print(" ", image[p[0] + 1, p[1]])

    return [[p[0] - 1, p[1]], [p[0], p[1] - 1], [p[0], p[1] + 1], [p[0] + 1, p[1]]]


get4_neighbours([4, 5])

# %% [markdown]
# #### N8 Neighbours
# 

# %%
def get8_neighbours(p):
    # print(image[p[0] - 1, p[1] - 1], image[p[0] - 1, p[1]], image[p[0] - 1, p[1] + 1])
    # print(image[p[0], p[1] - 1], image[p[0], p[1]], image[p[0], p[1] + 1])
    # print(image[p[0] + 1, p[1] - 1], image[p[0] + 1, p[1]], image[p[0] + 1, p[1] + 1])

    return [[p[0] - 1, p[1] - 1], [p[0] - 1, p[1]], [p[0] - 1, p[1] + 1], [p[0], p[1] - 1], [p[0], p[1] + 1], [p[0] + 1, p[1] - 1], [p[0] + 1, p[1]], [p[0] + 1, p[1] + 1]]


get8_neighbours([4, 5])

# %% [markdown]
# #### ND Neighbours
# 

# %%
def getD_neighbours(p):
    # print(image[p[0] - 1, p[1] - 1], " ", image[p[0] - 1, p[1] + 1])
    # print(" ", image[p[0], p[1]], " ")
    # print(image[p[0] + 1, p[1] - 1], " ", image[p[0] + 1, p[1] + 1])

    return [[p[0] - 1, p[1] - 1], [p[0] - 1, p[1] + 1], [p[0] + 1, p[1] - 1], [p[0] + 1, p[1] + 1]]


getD_neighbours([4, 5])

# %% [markdown]
# ### Line or Path Finding Algorithms
# 
# Write a function to find the path or line in the binary image. The function should take the binary image as input and return the coordinates of path or line in the image.
# 

# %% [markdown]
# #### Straight Line or Path
# 

# %%
def line_finder_using_N4(image):
    V = 0
    line = []

    for M in range(0, image.shape[0] - 1):
        for N in range(0, image.shape[1] - 1):
            if image[M, N] == V:
                N4 = get4_neighbours([M, N])
                for nbr in N4:
                    if (nbr[0] > 0 and nbr[1] > 0) and image[nbr[0], nbr[1]] == V:
                        line.append(nbr)
                    break
    return line

# %% [markdown]
# #### Test the Algorithm
# 
# As a test case, use the binary image created above and find the path or line in it. To test the algorithm, plot the binary image and remove the path or line found in the image to check, usig helper function <code>line_remover</code>.
# 

# %%
print("Cordinates of line are:", line_finder_using_N4(image))

plt.title("Removing line to check if coordinates are correct", fontsize=10)
plt.imshow(line_remover(image, line_finder_using_N4(image)), cmap="gray")

# %% [markdown]
# ### Creating a Binary Image
# 
# Create a binary images using <code>numpy</code> array. The image should be of size 300x300 and should have a straight line or path in it. The line or path should be of thickness 1 pixel and should be along one of the diagonal in the image.
# 

# %%
dig_line_image = np.ones((300, 300))

for i in range(0, 300):
    dig_line_image[i, i] = 0

plt.imshow(dig_line_image, cmap="gray")

# %% [markdown]
# #### Check
# 
# As you see <code>line_finder_using_N4</code> does not work for diagonal lines. This is because the diagonal line does not have any N4 neighbours. To find the diagonal line, we need to use N8 neighbours.
# 

# %%
print("Cordinates of line are:", line_finder_using_N4(dig_line_image))

plt.title("Removing line to check if coordinates are correct", fontsize=10)
plt.imshow(line_remover(dig_line_image, line_finder_using_N4(dig_line_image)), cmap="gray")
print("It does not work for diagonal line")

# %% [markdown]
# #### Diagonal Line or Path
# 

# %%
def line_finder_using_N8(image):
    V = 0
    line = []

    for M in range(0, image.shape[0] - 1):
        for N in range(0, image.shape[1] - 1):
            if image[M, N] == V:
                N8 = get8_neighbours([M, N])
                for nbr in N8:
                    if (nbr[0] > 0 and nbr[1] > 0) and image[nbr[0], nbr[1]] == V:
                        line.append(nbr)
                    break
    return line

# %% [markdown]
# #### Test the Algorithm
# 
# As a test case, use the binary image created above and find the path or line in it. To test the algorithm, plot the binary image and remove the path or line found in the image to check, usig helper function <code>line_remover</code>.
# 

# %%
print(line_finder_using_N8(dig_line_image))

plt.title("Removing line to check if coordinates are correct", fontsize=10)
plt.imshow(line_remover(dig_line_image, line_finder_using_N8(dig_line_image)), cmap="gray")

# %% [markdown]
# ---
# 

# %% [markdown]
# ## Conclusion
# 
# In this lecture, we learned how to create a binary image and find the path or line in it using N4, N8 and ND neighbours and Adjaency Processing. We also learned how to test the algorithm using helper function <code>line_remover</code>.
# 


