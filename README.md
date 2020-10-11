# Player detection with keras-yolo3

Forked from https://github.com/qqwweee/keras-yolo3
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction

An application of the Keras implementation as created by https://github.com/qqwweee. Visit that repo for steps on how to use. In this repo Keras was used to identify all different types of people on a basketball court (two opposing teams + referees)


---

## Description

### Part 1
I applied the pre trained YOLOv3 model to identify humans within the basketball court. Model performed quite well as you can see in the GIF below. This application was fairly easy, all that was required was to download the pretrained weights and configurations and load the video in.

[INSERT GIF]

### Part 2
Tried to classify all humans on the court in one of three classes (Team 1, Team 2, Referee). This was significantly harder, these were the steps I followed:
1. Turn video of a full game into frames. Video was at 25FPS so there were a a total of ~60k (25 * 40mins of playing time * 60s) images created.
2. Manually label training images. I used LabelImg to do this but only labelled 352 (320 for training, 32 validating). I used images from the video at 1FPS instead of 25FPS to get more varied images. Labelling more images would no doubt improve the performance of the model but the task was strenuous already. Maybe another time I can use Amazon mechanical turk. Thank you to Panos Sotirellos for helping with the labelling.
3. Trained the model based on labelled data. For optimal results I had to:
  a. Find optimal size of anchor boxes to feed into training. Ended up with height~45px, width~15px.
  b. Play with different versions of the yolov3 (tiny model, actual model, freezing a variable number of layers when applying the trained weights etc)
  c. Variable learning rates, epochs
4. Apply the prediction model based on different levels of confidence (ended up showing all boxes with 25%+ confidence)

As you can see the model is just about showing some signs of a learning behaviour. Confidence is still quite low and resulting predictions way too noisy. More images would definitely be of value here and perhaps some feature engineering (eg. first detect all humans and only after that's done classify them). Some more powerful models would also lead to a significant improvement.

[INSERT GIF]
