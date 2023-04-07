import os, sys
import shutil
from tqdm import tqdm
from datetime import datetime


def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__


twilight_superpoint_slam = os.getcwd()

# paths from the SuperPoint-SLAM Directory
vocabuylary_path = "./vocabulary/superpoint_voc.yml.gz"
mono_kitti_path = "./Examples/Monocular/mono_kitti"     # monocular kitti executable path
kitti_yaml_path = "./Examples/Monocular/KITTI04-12.yaml"  # kitti .ymal file for sequqnce 4-12

mono_tartan_path = "./Examples/Monocular/mono_tartan"     # monocular kitti executable path
tartan_yaml_path = "Examples/Monocular/TARTAN_AIR.yaml"  # kitti .ymal file for sequqnce 4-12


# KITTI sequences
sequences_04  = ["04","04_bread","04_dual","04_egan","04_zero"]
sequences_06  = ["06","06_bread","06_dual","06_egan","06_zero"]
sequences_07  = ["07","07_bread","07_dual","07_egan","07_zero"]

# Tartan Air sequences
sequences_P001 = ["abandonedfactory_sample_P001/P001"]


# select sequences to run
kitti_sequences = []
tartan_sequences = []

kitti_sequences = ["04_zero"]


# set directory to Twighlight-SLAM
try:
    os.mkdir(os.path.join(os.getcwd(),'evaluations'))
except:
    print("Evaluations folder already exists")

for sequence in tqdm(kitti_sequences):
    print(f"\n\nTESTING SEQUENCE: {sequence}")
    
    # set directory to SuperPoint-SLAM
    os.chdir(os.path.join(os.getcwd(),'thirdparty/SuperPoint_SLAM'))
    sequence_path = "../../datasets/KITTI/data_odometry_color/dataset/sequences/" + sequence

    # execute sequence
    print(f"\n{mono_kitti_path} {vocabuylary_path} {kitti_yaml_path} {sequence_path}")
    os.system(f"{mono_kitti_path} {vocabuylary_path} {kitti_yaml_path} {sequence_path}")

    # reutrn to Twilight-SLAM directory and save trajectory
    os.chdir(twilight_superpoint_slam)
    original = 'thirdparty/SuperPoint_SLAM/KeyFrameTrajectory.txt'
    now = datetime.now()
    timestamp = f"Y{now.year}_M{now.month}_D{now.day}_H{now.hour}_M{now.minute}_S{now.second}"
    target = f'evaluations/estimated_trajectories/KITTI/{sequence}_KeyFrameTrajectory_{timestamp}.txt'

    if os.path.isfile(target):
        print(f"File {target} already exists")
    else:
        shutil.copyfile(original, target)


for sequence in tqdm(tartan_sequences):
    print(f"\n\nTESTING SEQUENCE: {sequence}")
    
    # set directory to SuperPoint-SLAM
    os.chdir(os.path.join(os.getcwd(),'thirdparty/SuperPoint_SLAM'))
    sequence_path = "Formatted_TartanAir/" + sequence

    # execute sequence
    os.system(f"{mono_tartan_path} {vocabuylary_path} {tartan_yaml_path} {sequence_path}")

    # reutrn to Twilight-SLAM directory and save trajectory
    os.chdir(twilight_superpoint_slam)
    original = 'thirdparty/SuperPoint_SLAM/KeyFrameTrajectory.txt'
    now = datetime.now()
    timestamp = f"Y{now.year}_M{now.month}_D{now.day}_H{now.hour}_M{now.minute}_S{now.second}"
    target = f'evaluations/estimated_trajectories/TartanAir/{sequence.split("/")[-1]}_KeyFrameTrajectory_{timestamp}.txt'

    if os.path.isfile(target):
        print(f"File {target} already exists")
    else:
        shutil.copyfile(original, target)

