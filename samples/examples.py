'''
#   problem 1


# Step 1: Create a file named motto.txt and write the first line
file_path = 'motto.txt'

# Open file in write mode ('w')
with open(file_path, 'w') as file:
    file.write('Fiat Lux!\n')

# Step 2: Reopen the file to print its content
with open(file_path, 'r') as file:
    content = file.read()
    print("Content of motto.txt after first write:")
    print(content)

# Step 3: Append the file with the second line
with open(file_path, 'a') as file:
    file.write('Let there be light\n')

# Step 4: Reopen the file to print the updated content
with open(file_path, 'r') as file:
    updated_content = file.read()
    print("\nContent of motto.txt after appending:")
    print(updated_content)
'''

'''
#problem 2

from matplotlib import image
from matplotlib import pyplot
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

path = os.path.dirname(os.path.abspath(__file__))
filename1 = path + '/' + 'united-states-of-america-flag-square-xs.bmp'
data1 = image.imread(filename1)




# Display image information
print('Image type is: ', type(data))
print('Image shape is: ', data.shape)

# Add some color boundaries to modify an image array
plot_data = data.copy()

# Write the modified images
image.imsave(path+'/'+'lenna-mod.jpg', plot_data)

plot_data = data.copy()
flag = data1.copy()

for width in range(250):
    for height in range(250):
        plot_data[height][262+width] = flag[height][width]



# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()
'''


'''

#problem 3

import PyPDF2 
import re

file_handle = open(r'C:\Users\ashko\OneDrive\Documents\GitHub\ROAR-Academy\samples\ssa.pdf', 'rb') 
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)   # this tells you total pages 
page_object = pdfReader.pages[0]    # We just get page 0 as example 
page_text = page_object.extract_text()   # this is the str type of full page



page_text = re.sub(r'[^A-Za-z ]+', '', page_text)
page_text = page_text.lower()

l = page_text.split()


D = {}
for i in range(page_number):

    page_object = pdfReader.pages[i]    # We just get page 0 as example 
    page_text = page_object.extract_text()   # this is the str type of full page
    page_text = re.sub(r'[^A-Za-z ]+', '', page_text)
    page_text = page_text.lower()
    l = page_text.split()


    for word in l:
        if word in D:
            D[word]+=1

        else:
            D[word] = 1
print(D)
'''
