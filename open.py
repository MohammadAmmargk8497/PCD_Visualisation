import os
import open3d as o3d
import numpy as np
import sys
from transforms import build_se3_transform
from tqdm import tqdm



def read_lego_loam_data_file(map_path, keyframe_id):
    filename = map_path + 'dump/' + keyframe_id + '/data'
    with open(filename, 'r') as f:
        lines = f.readlines()

    odom = []
    for i in range(7, 11):
        row = [float(x) for x in lines[i].strip().split()]
       # print(f'{i} {row}')
        odom.append(row)

    return np.array(odom)

def create_combined_ply_point_cloud(root_folder, output_ply_file, n):
    # Check if the root folder path exists
    if not os.path.exists(root_folder):
        raise FileNotFoundError(f"The root folder '{root_folder}' does not exist.")
    
    # Create an empty point cloud
    T_static = build_se3_transform([0,0,0,0,0,1.57]) 
    pcd_map = []
    pcd1 = o3d.geometry.PointCloud()
    # Iterate over subfolders in the root folder
    for idx in tqdm(range(n)):
        keyframe_id = str(idx).zfill(6)
        odom = read_lego_loam_data_file(root_folder, keyframe_id)
        odom = T_static @ odom
        
       
        
        pcd = o3d.io.read_point_cloud(root_folder+ 'dump/' +  keyframe_id + '/' + 'cloud.pcd')
        pcd = np.asarray(pcd.points)
        pcd = np.hstack([pcd, np.ones((pcd.shape[0], 1))])
        #print(pcd.shape)
        pcd_map.append(((odom @ pcd.T).T))
        #pcd_map=np.append(((odom @ pcd.T).T), pcd_map)
       
       
   
    pcd_map = np.vstack(pcd_map)
    pcd_map = pcd_map[: , :-1]
 
    print(pcd_map.shape)
   
     
    # Save the combined point cloud in PLY format  
    pcd1.points = o3d.utility.Vector3dVector(pcd_map)
    o3d.io.write_point_cloud(output_ply_file, pcd1)                
    
    

if __name__ == "__main__":
   
    if len(sys.argv) != 4:
        print("Usage: python your_script.py path_arg1 path_arg2 path_arg3")
        sys.exit(1)

    
    root_folder_path = sys.argv[1]
    output_ply_file_path= sys.argv[2]
    n = int(sys.argv[3])
    output_ply_file_path = output_ply_file_path + 'combined_point_cloud.ply'
    create_combined_ply_point_cloud(root_folder_path, output_ply_file_path, n)

