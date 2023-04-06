import os, sys
import glob
import shutil
from tqdm import tqdm

orig_dataset_path = os.path.join(os.getcwd(),'datasets/TartanAir/')
sequence_name = 'abandonedfactory_sample_P001/P001'

# creat list of all images in dataset of interest
img_paths = sorted(glob.glob(f"{orig_dataset_path + sequence_name }/image_left/*.png", recursive=False))

print()
print(f"{len(img_paths)} images found")

formatted_main_path = os.path.join(os.getcwd(),'datasets/Formatted_TartanAir')
if not os.path.isdir(formatted_main_path):
    print("Created Formatted Dataset Folder for TartanAir datasets")    
    os.mkdir(formatted_main_path)

formatted_sequence_path = formatted_main_path + "/"+ sequence_name + '/image_left/'
if os.path.isdir(formatted_sequence_path):
    print()
    print("The following directory already exits: ")
    print(formatted_sequence_path)
    print("If you'd like to recreate this directory, you will need to delete the current directory.")
    print()

else:
    os.makedirs(formatted_sequence_path)

# create /rgb directory
source_folder = orig_dataset_path + sequence_name + '/image_left/'
destination_folder = formatted_sequence_path


print("\nCopying over images...")
for file_name in tqdm(os.listdir(source_folder)):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # copy only files
    if os.path.isfile(source):

        shutil.copy(source, destination)


# create rgb.txt file and times.txt file
#rgb_file = open(formatted_main_path + "/"+ sequence_name + "/rgb.txt","w+")
times_file = open(formatted_main_path + "/"+ sequence_name + "/times.txt","w+")


print("\nCreating rgb.txt and times.txt...")
for idx,img_path in tqdm(enumerate(img_paths)):

    #rgb_file.write(f"{os.path.basename(img_path)}\r\n")
    times_file.write(f"{float(idx)}\r\n")

     






