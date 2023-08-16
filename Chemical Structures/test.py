import pickle

c1 = pickle.load(open("Chemical Structures/outputs/cyclohexane_dist_mat_modified.bin",'rb'))

c2 = pickle.load(open("Chemical Structures/outputs/cyclohexane_dist_mat_without_intermediate_pts.bin",'rb'))

diff = c1-c2

print(diff.max(axis=None)) # Should not be greater than 0 beacuse adding the intermediate nodes decreases the distance between the nodes