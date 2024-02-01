# Transforming PCD from Car Frame to Map Frame and Visualizing 

## Structure
The above project has 3 scripts :
* open.py-->
  This scripts converts the pcd from local frame to global frame by using odometry data and transformation matrix. The transformed pcd is stored in ply format.
  
* visualize.py
  This script uses open3d to visualise the saved ply file.
* transforms.py

## Usage
 1. To use open.py use ```./create_map.sh #path_to_dump #path_to_store_ply #no. of folders in ./dump```
 2. To visualise use ```./visualise_map.sh #path_to_stored_ply```

## Results
<img width="1060" alt="Screenshot 2024-02-01 at 10 53 33 PM" src="https://github.com/MohammadAmmargk8497/PCD_Visualisation/assets/75717701/6eef4548-101c-4d1d-8cb8-88a9c384d0d1">

![DepthCapture_2024-02-01-22-47-46](https://github.com/MohammadAmmargk8497/PCD_Visualisation/assets/75717701/56aa3146-5213-4cbf-972b-b054fd8274d8)

