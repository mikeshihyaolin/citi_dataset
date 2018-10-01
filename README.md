# CITI-DailyActivities 3D dataset
The CITI-DailyActivities 3D dataset comprises action videos of three modalities such as RGB videos, depth maps, and 3D skeleton structures. It contains fifteen daily activities including walk, sit down, sit still, use a TV remote, stand up, stand still, pick up books, carry books, put down books, carry a backpack, drop a backpack, make a phone call, drink water, wave hand, and clap.

The dataset has 481 sequences. Among them, 181 sequences contain outlier frames presenting in arbitrary locations and lasting for various durations. Ten actors, including eight males and two females, were recruited for building this dataset, and one of them is left-handed. Each activity is performed by each actor between two and five times. A Microsoft Kinect was used for the collection so that the RGB video, the depth maps, and the inferred skeletons of each activity sequence are all available. The skeleton structures in this work were extracted by using the Kinect for Windows SDK v1.8

## Load data
```
python citi_loader.py
```
