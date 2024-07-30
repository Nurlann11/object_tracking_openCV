# Object Tracking with OpenCV

## Overview

This project provides an implementation of object tracking using OpenCV. The script captures video input, tracks a selected object throughout the video, and outputs a new video with the tracked object highlighted.

## Features

- **Object Selection**: Allows the user to select an object to be tracked in the initial frame.
- **Object Tracking**: Utilizes the KCF (Kernelized Correlation Filters) tracker to follow the object in subsequent frames.
- **Output Video**: Saves the video with the tracked object highlighted with bounding boxes and coordinates displayed.
- **Frame Rate Handling**: Adjusts processing speed to match the original video's frame rate.

### Video Example

Here is a video example:

<video width="540" height="460" controls>
  <source src="race.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<video width="540" height="460" controls>
  <source src="tracked_output.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>