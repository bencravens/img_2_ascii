from PIL import Image, ImageEnhance
import math
import numpy as np
import sys

class ascii_art:
    
    def __init__(self):
        #command line argument format:
        #python3 img_2_ascii.py imagefilename.png vertical_scaling charfilename
        #read in filename
        print(sys.argv)
        self.filename = sys.argv[1]
        self.vertical_scaling = int(sys.argv[2])
        self.charfile = sys.argv[3]
        #read in image
        self.img = Image.open(self.filename)
        #increase contrast
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(3)
        #convert to grayscale
        self.img_gray = self.img.convert("L")
        #convert to array of pixel intensities
        self.img_array= np.asarray(self.img_gray)
   
    def make_char_array(self):
        # Create character array for ASCII pixel representations
        self.char_array = []
        charfile = open(self.charfile,"r")
        charlines = charfile.readlines()
        for line in charlines:
            for char in line:
                self.char_array.append(char)
        #get rid of quotes and line terminator characters"
        self.char_array = self.char_array[1:-2]
        self.num_chars = len(self.char_array)

    def normalize_pixel(self,pixel_intensity, num_chars):
        #convert the pixel intensity into an index for the character array
        #pixels go from 0-255
        #add one to avoid zero scale
        pixel_intensity+=1
        #minus one from num_chars due to 0 based index
        return int(math.floor((pixel_intensity/256)*(num_chars-1)))

    def write_to_file(self,filename):
        #now write to file
        myfile = open("{}.txt".format(filename),'w')
        [h,w] = np.shape(self.img_array)
        #want to sample from height only a factor of (1/vertical_scaling) as often as ascii characters tend to stretch upwards
        for i in range(0,h,self.vertical_scaling):
            for j in range(w):
                tempindex = self.normalize_pixel(self.img_array[i,j],self.num_chars)
                tempchar = self.char_array[tempindex]
                myfile.write(tempchar)
            #new height value, thus write to newline
            myfile.write("\n")
        myfile.close()

if __name__=="__main__":
    trollart = ascii_art()
    trollart.make_char_array()
    trollart.write_to_file("out")
