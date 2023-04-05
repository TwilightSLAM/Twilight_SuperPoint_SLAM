import os, sys
import shutil
from tqdm import tqdm
from datetime import datetime


def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__


twilight_superpoint_slam = os.getcwd()
dataset_executable_path = "./Examples/Monocular/mono_kitti" 
vocabuylary_path = "Vocabulary/superpoint_voc.yml.gz"
yaml_path = "Examples/Monocular/KITTI04-12.yaml"

sequences_04  = ["04","04_bread","04_dual","04_egan","04_zero"]
sequences_06  = ["06","06_bread","06_dual","06_egan","06_zero"]
sequences_07  = ["07","07_bread","07_dual","07_egan","07_zero"]

sequences = sequences_04
# set directory to Twighlight-SLAM
try:
    os.mkdir(os.path.join(os.getcwd(),'evaluations'))
except:
    print("Evaluations folder already exists")

for sequence in tqdm(sequences):

    # set directory to SuperPoint-SLAM
    os.chdir(os.path.join(os.getcwd(),'SuperPoint_SLAM'))
    sequence_path = "data_odometry_color/dataset/sequences/" + sequence

    # execute sequence
    blockPrint()
    os.system(f"{dataset_executable_path} {vocabuylary_path} {yaml_path} {sequence_path}")
    enablePrint()

    # reutrn to Twilight-SLAM directory and save trajectory
    os.chdir(twilight_superpoint_slam)
    original = 'SuperPoint_SLAM/KeyFrameTrajectoryTUM.txt'
    now = datetime.now()
    timestamp = f"Y{now.year}_M{now.month}_D{now.day}_H{now.hour}_M{now.minute}_S{now.second}"
    target = f'evaluations/{sequence}_KeyFrameTrajectoryTUM_{timestamp}.txt'

    if os.path.isfile(target):
        print(f"File {target} already exists")
    else:
        shutil.copyfile(original, target)

