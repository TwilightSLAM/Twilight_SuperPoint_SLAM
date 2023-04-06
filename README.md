# Twilight_SuperPoint_SLAM
Primary Objective: To investigate hypothesized performance improvements of SuperPoint-SLAM, a monocular visual SLAM technique combining superpoint's neural network-based feature detection and description with the ORB-SLAM2 architecture, employing image enhancing modules for underexposed or "twilight" monocular SLAM dataset sequences. 

Secondary Objectve: To provide tools for streamlining evaluation of multiple datasets.

Experiment Overview: We initially test against against the KITTI benchmark to confirm pipeline success. Then, we test against ETH3D and Tartan Air benchmark data sequences which were qualitatively found to have more underexposed images on average or in general througout the entire sequence. Twilight dataset sequences that were too underexposed to initiate SuperPoint-SLAM wihout image enhancment modules were not considered.

