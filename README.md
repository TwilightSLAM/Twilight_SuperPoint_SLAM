# Twilight_SuperPoint_SLAM
Primary Objective: To investigate hypothesized performance improvements of SuperPoint-SLAM, a monocular visual SLAM technique combining superpoint's neural network-based feature detection and description with the ORB-SLAM2 architecture, employing image enhancing modules for low light or "twilight" monocular SLAM dataset sequences. 

Secondary Objectve: To provide tools for streamlining evaluation of multiple datasets.

Experiment Overview: We initially test against against the KITTI benchmark to confirm pipeline success. Then, we test against ETH3D and Tartan Air benchmark data sequences which were qualitatively found to have more underexposed images on average or in general througout the entire sequence. Twilight dataset sequences that were too underexposed to initiate SuperPoint-SLAM wihout image enhancment modules were not considered.

# 1. OS and Hardware Prerequisites
We tested this project in *Ubuntu 18.04*. Additionally, the original repository reports testing for *Ubuntu 12.04*, *14.04*, and *16.04*. Using a HP-360x-Spectre with 4 cores, Intel Core i7, and no GPU. Thus we  we achieved SuperPoint-SLAM at 5 seconds per frame.

# 2. Intial Steps
`
cd ~/your_preferred_code_direcotry
git clone https://github.com/TwilightSLAM/Twilight_SuperPoint_SLAM.git
cd Twilight_SuperPoint_SLAM
`

# 3. 3rd Party Installations
We provide the library versions, downloading suggestions, and links to original repositories to streamline the installation process.

## Pangolin v0.6
### Recommended Steps:
``` bash
# build in third party directory (recommended)
cd thirdparty

# build Pangolin
git clone 
git clone --recursive https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
git checkout v0.6
./scripts/install_prerequisites.sh recommended
mkdir build && cd build
cmake ..
make -j2
make install

# return to thirdparty directory
cd ../..
```
### Original Repository: https://github.com/stevenlovegrove/Pangolin

## OpenCV 3.2
```bash
Recommended Guide: https://gist.github.com/syneart/3e6bb68de8b6390d2eb18bff67767dcb
```
### Original Repository:

## Eigen3 3.4
You should have already installed libeigen via the recommended instruction for building OpenCV. If not, install 
```bash


```
### Original Repository:

## SuperPoint-SLAM

### Recommended Steps:
```bash

```
### Original Repository:

## Libtorch
### Version Used:
### Recommended Steps:
```bash

```
### Original Repository:

4. Install SLAM Datasets and Enhance Images
Follow steps in [INSERT REPO HERE] to download visual slam datasets (KITTI, Tartan Air, ETH3D and TUM) and generate new images using low light image enhancement modules (Bread, Dual, EnlightenGAN and ZeroDCE).

Once images are downloaded, use the recommended direcotry formatting to store you images in order to use `run_multiple_sequences.py` and `evaluate_multiple_sequences.py`.

5. Run SuperPoint-SLAM

6. Evaluate 
