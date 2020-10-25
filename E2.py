# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# E2.1
import numpy as np
### Start of your code ##
H = np.array([[0, 1, 2], [3, 4, 5],[6, 7, 8]])
H = H + 10
print(H)
### End   of your code ##

# E2.2
rng = np.random.RandomState(57)
### Start of your code ##
import random
I =[[random.uniform(0,5)]*3]*3
print(I)
### End   of your code ##

I

# E2.3
A = np.array([[ 1, 2, 3, 4], [ 5, 6, 7, 8], [ 9, 10, 11, 12], [13, 14, 15, 16]])
### Start of your code ##
B = A[2:4, 2:4]
### End   of your code ##

print(f'A=\n{A}\n')
print(f'B=\n{B}')

# E2.4
A = A * 7
B = A[2:4, 2:4]
print(f'A=\n{A}\n')
print(f'B=\n{B}')

# E2.5
### Start of your code ##
A = np.array([[ 1, 2, 3, 4], [ 5, 6, 7, 8], [ 9, 10, 11, 12], [13, 14, 15, 16]])
rows = np.array([[2,2],[3,3]]) 
cols = np.array([[2,3],[2,3]])
B = A[rows, cols]
### End   of your code ##

A*=7
print(f'A=\n{A}\n')
print(f'B=\n{B}')

# E2.6
rng = np.random.RandomState(57)
D = rng.randint(0, 10, (5,4))
E = rng.randint(0, 10, 20)
print(f'D=\n{D}\n')
print(f'E=\n{E}')
### Start of your code ##
E_row_major = E.reshape((5,4))
# row-major code here
print(f'\nafter row-major reshape:\nE_row_major=\n{E_row_major}')
E_col_major = E.reshape((5,4),order='F')
# column-major code here
print(f'\nafter column-major reshape:\nE_row_major=\n{E_col_major}')

### End   of your code ##

# E2.7
rng = np.random.RandomState(57)
F = rng.randint(0, 10, (5,4))
print(f'\nF:\n{F}')

### Start of your code ##

# row-major code here
F_flattened_row_major = F.flatten(order='C')
print(f'\nFlattened(row-major):\n{F_flattened_row_major}')

# column-major code here
F_flattened_column_major = F.flatten(order='F')
print(f'\nFlattened(column-major):\n{F_flattened_column_major}')

### End   of your code ##

# E2.8
# E2.8.1
grayscale_image = np.array(range(20)).reshape(4,5)

print(f'This grayscale_image is\
 {grayscale_image.shape[0]}x{grayscale_image.shape[0]}\
 and\
 has {grayscale_image.ndim} dimenions.')
grayscale_image

### Start of your code ##
grayscale_image_flattened = grayscale_image.flatten(order='C')
print(grayscale_image_flattened)
### End   of your code ##
grayscale_image_flattened

# E2.8.2
RGB_image = np.array(range(12)).reshape(3,2,2)
print(f'This RGB_image is\
 {RGB_image.shape[1]}x{RGB_image.shape[2]}\
 and\
 has {RGB_image.ndim} dimenions.')
RGB_image
### Start of your code ##
RGB_image_flattened = RGB_image.flatten(order='C')
print(RGB_image_flattened)
### End   of your code ##
RGB_image_flattened

# E2.8.3
RGB_images = np.array(range(24)).reshape(2,3,2,2)


print(f'There are {RGB_images.shape[0]} RGB_images\
 : each of size\
 {RGB_images.shape[-2]}x{RGB_images.shape[-1]}.\
 So our tensor has {RGB_images.ndim} dimensions(4D).\
\nThe shape of the tensor is: {RGB_images.shape}')

print(f'  The first number  ({RGB_images.shape[0]}): indicated the number of images,\
\n  The second number ({RGB_images.shape[1]}): indicated the number of layers of images (Red,Green,Blue),\
\n  The third number  ({RGB_images.shape[2]}): indicated the number of rows in each layer,\
\n  The last number   ({RGB_images.shape[3]}): indicated the number of columns in each layer.\n')

print(f'RGB_images array look like:\n{RGB_images}')



### Start of your code ##
RGB_images_flattened = np.reshape(RGB_images,(2,-1),order='C')
print(RGB_images_flattened)
### End   of your code ##
RGB_images_flattened




# E3.1
### Start of your code ##
def flatten_images(images):
  if images.ndim <= 3 :
      images_flattened = np.reshape(images,(1, -1),order='C')
  else:
      images_flattened = np.reshape(images,(2,-1),order='C')
  return images_flattened
 ### End   of your code ##

np.equal(grayscale_image_flattened,flatten_images(grayscale_image)).all()
np.equal(RGB_image_flattened ,flatten_images(RGB_image)).all()
np.equal(RGB_images_flattened,flatten_images(RGB_images)).all()


# E3.2















