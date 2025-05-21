# Intelligent Doorbell: Home Door Security System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4-red.svg)
![YOLO](https://img.shields.io/badge/YOLO-v5-darkgreen.svg)
![FaceNet](https://img.shields.io/badge/FaceNet-OpenCV-orange.svg)

An AI-powered home security system that automatically detects humans approaching your door, recognizes family members, and rings the doorbell only for unknown visitors.

![Intelligent Doorbell System](https://via.placeholder.com/800x400?text=Intelligent+Doorbell+System)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)

## 🔍 Overview

The Intelligent Doorbell system enhances home security by automating visitor detection and identification. Using computer vision and machine learning, it distinguishes between family members and strangers, ringing the doorbell only when unknown individuals approach your door.

Traditional doorbells lack real-time identification capabilities, requiring manual intervention. This intelligent system bridges that gap by providing automated surveillance and visitor recognition.

## ✨ Features

- **Human Detection**: Utilizes YOLO (You Only Look Once) for accurate real-time human detection
- **Face Recognition**: Implements FaceNet to identify family members with high accuracy
- **Automated Operation**: Rings doorbell automatically when unrecognized individuals approach
- **Real-time Processing**: Achieves response times under 1 second
- **Low Resource Consumption**: Optimized for Raspberry Pi 4 hardware
- **Variable Lighting Adaptability**: Functions in different lighting conditions

## 🏗️ System Architecture

The system follows this operational flow:

1. **Detection Phase**: Camera continuously monitors for human presence
2. **Recognition Phase**: When a human is detected, FaceNet verifies if they are a family member
3. **Action Phase**: Automatically rings doorbell if the person is not recognized

### Block Diagram

```
+---------------+     +-----------------+     +-------------------+
| Camera Module | --> | Raspberry Pi 4  | --> | Doorbell Speaker  |
+---------------+     | (YOLO, FaceNet) |     +-------------------+
                      +-----------------+
                             |
                             v
                      +-----------------+
                      | Face Database   |
                      +-----------------+
```

## 🛠️ Hardware Requirements

- Raspberry Pi 4 Model B (2GB+ RAM recommended)
- Raspberry Pi Camera Module or compatible USB camera
- Speaker for doorbell sound
- Power supply for Raspberry Pi
- SD card (16GB+ recommended)
- Optional: Case for housing components

## 💻 Software Requirements

- Raspberry Pi OS (Bullseye or newer)
- Python 3.7+
- OpenCV
- YOLO (small model)
- FaceNet
- NumPy
- TensorFlow Lite

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/intelligent-doorbell.git
   cd intelligent-doorbell
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the camera**:
   ```bash
   # Enable camera in Raspberry Pi configuration
   sudo raspi-config
   # Select Interfacing Options > Camera > Enable
   ```

4. **Create family member database**:
   ```bash
   # Run the data collector script
   python data_collector.py
   ```

5. **Configure settings**:
   ```bash
   # Edit config.py with your desired settings
   nano config.py
   ```

## 🚀 Usage

1. **Start the system**:
   ```bash
   python main.py
   ```

2. **Adding new family members**:
   ```bash
   python data_collector.py --name "Family Member Name"
   ```

3. **Testing the system**:
   ```bash
   python test_recognition.py
   ```

## Main Components

### Data Collector
Captures and processes images of family members to create a face recognition database.

### Face Recognizer
Analyzes camera feed in real-time to detect humans and recognize faces against the stored database.

### Doorbell Controller
Manages the doorbell activation based on recognition results.

## Performance

- Human detection accuracy: 95%
- Face recognition accuracy: 90%
- Average processing time: <1 second

## 🔮 Future Work

- **Cloud Storage Integration**: Store images of visitors for future reference
- **Mobile Notifications**: Send alerts to homeowners when unknown visitors are detected
- **Improved Recognition Model**: Enhanced performance in various environmental conditions
- **Voice Communication**: Two-way audio communication with visitors
- **Integration with Smart Home Systems**: Connect with existing smart home ecosystems

## 🙏 Acknowledgements

Special thanks to Dr. M.D.R. Perera, Senior Lecturer, Department of Computer Science, Faculty of Applied Sciences, University of Sri Jayewardenepura for guidance and support throughout this project.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Developed by K.P.R.D. Pitawala (AS2021934) as part of the ICT 305 2.0 Embedded Systems course at the University of Sri Jayewardenepura.
