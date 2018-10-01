# #############################################################################################
# download data via https://drive.google.com/open?id=1IdVBAxKqQqx4yz2ctdEn9dc1YwzNLPnF        #
# download labels via https://drive.google.com/open?id=1aUF_oRhJNb6prBGJ6mhkz-3NJcmbsMRJ      #
# #############################################################################################
import glob
import numpy as np

data_path  = './citi_data/*.npy'
action_label_path = "./citi_labels/action_labels.npy"
subject_label_path = "./citi_labels/subject_labels.npy"


# load labels
action_labels = np.load(action_label_path)
subject_labels = np.load(subject_label_path)


# load data
data_list = sorted(glob.glob(data_path))
data = []
for i, fi in enumerate(data_list):
	print(fi)
	data.append(np.load(fi))
    

# show
print("action label #10: "+str(action_labels[10][0]))
print("subject label #10: "+str(subject_labels[10][0]))
print("action #10 frame #1~#2: "+str(data[0][0:2]))
print("* Each frame is a 57(=19 body_joints * 3(x,y,z)-d feature vector\n\n")