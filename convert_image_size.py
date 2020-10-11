from PIL import Image
import numpy as np
import glob

def convert_image_size(input_path="../images/*.jpg", output_path="../resized_images/"):
    images = glob.glob(input_path) # obtain a list of all images
    for image in images:
        im = Image.open(image)
        # resize but keep aspect ratio
        data_padded = np.pad(np.asarray(im), ((0,182), (0,0), (0, 0)), 'constant') # pad height with 0s to create 416X416
        imp = Image.fromarray(data_padded) # turn back into PIL object

        name = image.split("/")[-1] # get the exact name of the image
        new_path = output_path + name # and store in new path, resized
        imp.save(new_path)

#def convert_image_size_back_to_original(input_path="../resized_images/", output_path="../original_size/"):



convert_image_size()
