import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
import sys


def vis(path):
    pcd = o3d.io.read_point_cloud(path)
    downpcd = pcd.voxel_down_sample(voxel_size=0.02)
    with o3d.utility.VerbosityContextManager(
            o3d.utility.VerbosityLevel.Debug) as cm:
                labels = np.array(
                downpcd.cluster_dbscan(eps=0.02, min_points=10, print_progress=True))

    print(type(pcd))
    print(np.asarray(pcd.points))
    max_label = labels.max()
    print(f"point cloud has {max_label + 1} clusters")
    colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0
    downpcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    o3d.visualization.draw_geometries([pcd],
                                  zoom=0.2,
                                  front=[-0.4999, -0.1659, -0.8499],
                                  lookat=[2.1813, 2.0619, 2.0999],
                                   up=[0.1204, -0.9852, 0.1215])

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python your_script.py path_arg1 path_arg2 path_arg3")
        sys.exit(1)

    root_folder_path = sys.argv[1]   
    vis(root_folder_path)
