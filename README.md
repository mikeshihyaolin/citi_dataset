# CITI-DailyActivities 3D dataset
**Code Author: Shih-Yao (Mike) Lin**

## Introduction
The CITI-DailyActivities 3D dataset comprises action videos of three modalities such as RGB videos, depth maps, and 3D skeleton structures. It contains fifteen daily activities including walk, sit down, sit still, use a TV remote, stand up, stand still, pick up books, carry books, put down books, carry a backpack, drop a backpack, make a phone call, drink water, wave hand, and clap.

The dataset has 481 sequences. Among them, 182 sequences contain outlier frames presenting in arbitrary locations and lasting for various durations. Ten actors, including eight males and two females, were recruited for building this dataset, and one of them is left-handed. Each activity is performed by each actor between two and five times. A Microsoft Kinect was used for the collection so that the RGB video, the depth maps, and the inferred skeletons of each activity sequence are all available. The skeleton structures in this work were extracted by using the Kinect SDK v1.8

<img src=figs/a01_s11_e01.gif width="150"><img src=figs/a02_s11_e01.gif width="150">
<img src=figs/a03_s11_e01.gif width="150">
<img src=figs/a04_s11_e01.gif width="150">
<img src=figs/a05_s11_e01.gif width="150">
<img src=figs/a06_s11_e01.gif width="150">
<img src=figs/a07_s11_e01.gif width="150">
<img src=figs/a08_s11_e01.gif width="150">
<img src=figs/a09_s11_e01.gif width="150">
<img src=figs/a10_s11_e01.gif width="150">
<img src=figs/a11_s11_e01.gif width="150">
<img src=figs/a12_s11_e01.gif width="150">
<img src=figs/a13_s11_e01.gif width="150">
<img src=figs/a14_s11_e01.gif width="150">
<img src=figs/a15_s11_e01.gif width="150">

## Download data
1. [RGB Images (21GB)](https://drive.google.com/open?id=1wjtMKBEd02muTAMZD9vSLsSj9M2i3qqn) (480x640) 
2. [Depth Images (2.1GB)](https://drive.google.com/open?id=1WnYZHO3406oIDcZl-KxYXBhQNSOELd2W) (320x240)
3. [3D Skeletal Data (256MB)](https://drive.google.com/open?id=1IdVBAxKqQqx4yz2ctdEn9dc1YwzNLPnF) 
4. [Labels](https://drive.google.com/open?id=1aUF_oRhJNb6prBGJ6mhkz-3NJcmbsMRJ)

NOTE: The dataset contains 481 action examples, where action example #1 - #300 are the actions without outlier frames, and action example # 301 - # 482 are the actions with outlier frames. 

## Load skeleton data
```
python citi_loader.py
```
# Citation
```
@article{lin2017recognizing,
  title={Recognizing human actions with outlier frames by observation filtering and completion},
  author={Lin, Shih-Yao and Lin, Yen-Yu and Chen, Chu-Song and Hung, Yi-Ping},
  journal={ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)},
  volume={13},
  number={3},
  pages={28},
  year={2017},
  publisher={ACM}
}
```
