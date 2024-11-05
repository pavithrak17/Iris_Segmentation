
# MINI PROJECT COMPUTER GRAPHICS

# Iris Segmentation Project

This project focuses on accurately isolating the iris from the eye using image processing techniques, aimed at enhancing biometric identification systems. Using the **MediaPipe** library and **OpenCV**, it segments the iris in real-time from live video feeds, providing essential functionality for reliable and secure biometric applications.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Requirements](#setup-and-requirements)
- [Usage](#usage)
- [Results and Discussion](#results-and-discussion)
- [Future Improvements](#future-improvements)

## Introduction
Iris segmentation is crucial for biometric systems as it allows accurate identification by isolating the iris. This project uses facial landmark detection and the minimal enclosing circle method to locate and segment the iris effectively. It operates in real-time, adapting to environmental changes, and handles various challenges such as fluctuating lighting and partial obstructions.

## Features
- Real-time iris segmentation using video feeds.
- High accuracy and robustness under different lighting conditions.
- Ability to handle obstructions from eyelids or eyelashes.
- Efficient performance with low latency, suitable for dynamic environments like security systems.

## Technologies Used
- **Python**: Core programming language.
- **OpenCV**: For image processing and video frame capture.
- **MediaPipe Face Mesh**: For facial landmark detection.
- **NumPy**: For numerical operations.

## Setup and Requirements

### Software Requirements
- **Python**: Version 3.6 or later.
- **OpenCV**: Version 4.x.
- **MediaPipe**: Version 0.8.x or later.
- **NumPy**: Version 1.21.x or later.

### Hardware Requirements
- **Camera**: 720p resolution or higher with a 30 FPS frame rate recommended.
- **Processor**: Modern multi-core processor (e.g., Intel i5 or AMD Ryzen).
- **GPU**: Optional for enhanced performance.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/pavithrak17/Iris_Segmentation.git 
   cd iris-segmentation
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script using:
```bash
python iris_segmentation.py
```
The program will capture video from your webcam, detect facial landmarks, and highlight the iris in real-time.

## Results and Discussion
The algorithm effectively segments the iris with high precision, even in challenging conditions. Real-time video processing ensures smooth operation, making it ideal for use in biometric verification.

## Future Improvements
- Integrate deep learning for improved feature extraction.
- Expand testing on diverse iris datasets for higher robustness.
- Enhance lighting adaptability for more accurate segmentation.

## References
- [Deep Learning-Based Iris Segmentation Algorithm for Effective Iris Recognition System (2022)](https://example.com)
- [Iris-SAM: Iris Segmentation Using a Foundation Model (2024)](https://example.com)
