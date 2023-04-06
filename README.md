# Twilight_SuperPoint_SLAM
Primary Objective: To investigate hypothesized performance improvements of SuperPoint-SLAM, a monocular visual SLAM technique combining superpoint's neural network-based feature detection and description with the ORB-SLAM2 architecture, employing image enhancing modules for underexposed or "twilight" monocular SLAM dataset sequences. 

Secondary Objectve: To provide tools for streamlining evaluation of multiple datasets.

Experiment Overview: We initially test against against the KITTI benchmark to confirm pipeline success. Then, we test against ETH3D and Tartan Air benchmark data sequences which were qualitatively found to have more underexposed images on average or in general througout the entire sequence. Twilight dataset sequences that were too underexposed to initiate SuperPoint-SLAM wihout image enhancment modules were not considered.

# 1. OS and Hardware Prerequisites
We tested this project in *Ubuntu 18.04*. Additionally, the original repository reports testing for *Ubuntu 12.04*, *14.04*, and *16.04*. Using a HP-360x-Spectre with 4 cores, Intel Core i7, and no GPU. Thus we  we achieved SuperPoint-SLAM at 5 seconds per frame.

# 2. Intial Steps
`cd ~/your_preferred_code_direcotry
git clone https://github.com/TwilightSLAM/Twilight_SuperPoint_SLAM.git`

# 3. 3rd Party Installations
We provide the library versions, downloading suggestions, and links to original repositories to streamline the installation process.

## Pangolin v0.6
### Version Used:
### Recommended Steps:
cd 
### Original Repository: https://github.com/stevenlovegrove/Pangolin
''
## OpenCV 3.2

## Eigen3

## SuperPoint-SLAM

## Libtorch

