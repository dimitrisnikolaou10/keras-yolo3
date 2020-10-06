import glob
import math

def convert_from_path(start_path="../images/*.txt", end_path='../resized_images/custom_annotations.txt'):
    new_annotations = open(end_path, 'w')
    annotated_images = glob.glob(start_path)
    for image in annotated_images:
        if "classes" in image:
            continue
        annotations = open(image, "r")
        Lines = annotations.readlines()
        image_name = '../resized_images/' + image.split("/")[-1][0:-4] + ".jpg"
        new_annotations.write(image_name)
        for line in Lines:
            all_items = line.split(" ")

            ann_class, center_x, center_y, width, height = all_items[0], all_items[1], all_items[2], all_items[3], all_items[4]

            center_x = math.floor(416*float(center_x))
            width = math.floor(416*float(width))
            center_y = math.floor(234*float(center_y))
            height = math.floor(234*float(height))
            x_min = center_x - math.floor(width/2)
            x_max = center_x + math.floor(width/2)
            y_min = center_y - math.floor(height/2)
            y_max = center_y + math.floor(height/2)
            new_annotations.write(" ")
            new_annotations.write(str(x_min))
            new_annotations.write(",")
            new_annotations.write(str(y_min))
            new_annotations.write(",")
            new_annotations.write(str(x_max))
            new_annotations.write(",")
            new_annotations.write(str(y_max))
            new_annotations.write(",")
            new_annotations.write(str(ann_class))
        new_annotations.write("\n")


convert_from_path()
