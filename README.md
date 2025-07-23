# Automated-Fruit-Sorting-System

This project presents an **automated fruit sorting system** that combines **embedded systems**, **robotic control**, and **computer vision** to classify and sort bananas based on ripeness and type. The system integrates image processing techniques, machine learning, and shape analysis to deliver a real-time, efficient, and scalable solution for agricultural automation.

<p align="center">
<img width="300" height="448" alt="image" src="https://github.com/user-attachments/assets/27d99648-6ffd-4810-a218-a9282188ab62" />
</p>



## Project Overview

The goal is to design and implement a **fully autonomous fruit sorting system** capable of:

- Detecting **banana ripeness** (unripe, ripe, rotten) using color-based analysis
- **Classifying bananas** among other fruits using deep learning
- Distinguishing fruits by **shape** using classical image processing
- Controlling a robotic arm to physically sort fruits based on classification

## System Components

### Embedded Intelligence

- **Color Detection**: Classifies bananas by analyzing RGB pixel values
- **Deep Learning**: CNN trained to distinguish bananas from other fruits
- **Shape-Based Detection**: Uses edge detection and contour analysis to identify banana geometry

### Hardware Integration

- **Raspberry Pi 3**: Hosts the camera, runs algorithms
- **Spy Camera**: Captures live fruit images
- **AL5D Robotic Arm**: Physically moves fruits to the appropriate bin based on classification

##  How It Works

1. **Image Capture**: The Spy camera takes real-time images of the fruits
2. **Preprocessing**: Grayscale conversion, blurring, noise filtering
3. **Color & Shape Analysis**: Ripeness and fruit type are detected
4. **Sorting**: AL5D robotic arm sorts the fruit accordingly

## Technologies Used

- **Python**, **OpenCV**, **NumPy**
- **TensorFlow** (for CNN training)
- **Raspberry Pi 3**
- **AL5D Robotic Arm**
- **Spy Camera**

## Performance

- CNN model trained with custom fruit dataset
- Achieved **99% accuracy** in classifying bananas

<img width="400" height="182" alt="image" src="https://github.com/user-attachments/assets/97ccf512-b484-442c-a885-62d567402ee9" />

- Real-time processing optimized for embedded hardware
- Smooth coordination between vision system and robotic actuation

