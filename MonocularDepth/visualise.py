import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud('./pointCloudDeepLearning.ply')
pcd.estimate_normals()

# to obtain a consistent normal orientation
#pcd.orient_normals_towards_camera_location(pcd.get_center())

# or you might want to flip the normals to make them point outward, not mandatory
#pcd.normals = o3d.utility.Vector3dVector( - np.asarray(pcd.normals))

# surface reconstruction using Poisson reconstruction
#mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)
radii = [1, 1, 1, 1]
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
    pcd, o3d.utility.DoubleVector(radii))
# paint uniform color to better visualize, not mandatory
mesh.paint_uniform_color(np.array([0.7, 0.7, 0.7]))

o3d.io.write_triangle_mesh('a.ply', mesh)

