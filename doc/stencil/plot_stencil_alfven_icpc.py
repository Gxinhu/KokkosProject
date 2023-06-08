import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
#rc('text', usetex=True)

size=np.array([32,48,64,92,128,160,192,224,256,320,384,448,512,640,768])

# test_stencil_3d_flat
v0=np.array([38.4557,73.9336,78.7416,84.718,86.6486,88.5446,88.0435,88.033,86.7633,87.526,85.5697,87.0251,85.8294,84.4155,84.9425])

# test_stencil_3d_flat_1d_array
v1=np.array([86.6895,304.168,653.985,1209.65,1547.7,1173.86,1690.25,1127.23,592.943,421.34,360.829,332.553,326.96,325.748,328.157])

# test_stencil_3d_flat_vector without views
v2=np.array([86.6326,249.19,408.487,497.684,574.4,593.71,574.989,521.73,492.164,411.498,359.633,322.05,315.404,323.845,320.712])

# test_stencil_3d_flat_vector with    views
v3=np.array([113.547,346.809,729.462,903.837,1665.2,1964.12,1790.5,1123.92,592.683,421.522,362.668,324.958,317.823,328.213,328.01])

# test_stencil_3d_range
v4=np.array([59.3529,226.386,282.152,322.772,331.511,332.473,314.108,313.294,311.524,312.29,302.43,317.347,297.092,303.334,298.868])

# test_stencil_3d_range_vector
v5=np.array([133.815,339.407,676.623,875.324,1384.53,1983.01,1168.1,1000.37,483.492,424.788,352.237,314.275,305.922,329.188,315.589])

# test_stencil_3d_range_hierarchical
v6=np.array([172.698,384.544,700.884,1063.57,1315.71,1870.55,1599.11,987.452,477.457,421.849,351.897,312.2,317.42,318.79,313.824])

# test_stencil_3d_range_hierarchical_linearized
v7=np.array([155.591,348.164,699.027,1203.61,1398.05,2041.68,1703.39,987.258,554.394,417.759,349.021,306.144,312.927,319.737,315.308])

plt.plot(size,v0, label='# test_stencil_3d_flat')
plt.plot(size,v1, label='# test_stencil_3d_flat_1d_array')
plt.plot(size,v2, label='# test_stencil_3d_flat_vector without views')
plt.plot(size,v3, label='# test_stencil_3d_flat_vector with    views')
plt.plot(size,v4, label='# test_stencil_3d_range')
plt.plot(size,v5, label='# test_stencil_3d_range_vector')
plt.plot(size,v6, label='# test_stencil_3d_range_hierarchical')
plt.plot(size,v7, label='# test_stencil_3d_range_hierarchical_linearized')
plt.grid(True)
plt.title('3d 7 points stencil kernel performance')
plt.xlabel('N - linear size')
plt.ylabel(r'Bandwidth (GBytes/s)')
plt.legend()
plt.show()
