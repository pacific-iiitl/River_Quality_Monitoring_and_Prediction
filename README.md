# Real Time Detection and Prediction of Water Contamination Level

![Project Status](https://img.shields.io/badge/status-in_progress-yellowgreen)
![Language](https://img.shields.io/badge/language-Python-blue)
![Technology](https://img.shields.io/badge/technology-IoT%20%26%20ML-lightgrey)
![Institute](https://img.shields.io/badge/institute-IIIT%20Lucknow-brightgreen)

This project is a part of a research program on river water(s) funded by CST-UP and has to be executed by December 2026 (probable).
Files (like model.pkl, sensor_data_log, and water_quality_dataset) uploaded in the project folder structure are for demonstration only and to keep exclusivity of ongoing work; these files don't contain actual data of the program.

## Overview
This project focuses on real-time monitoring and predictive analysis of water contamination using IoT sensors and machine learning techniques. With the growing concern of deteriorating water quality, the system aims to collect, process, and analyze key water quality parameters to provide timely insights that can help in ensuring safe and clean water sources.

## Objectives
- Develop a prototype to collect relevant water quality data (pH, dissolved oxygen, turbidity, temperature, etc.) using sensor arrays.  
- Design a data pipeline for efficient storage, preprocessing, and model training.  
- Implement machine learning models to classify water contamination levels and predict potential issues.  
- Provide real-time sharing of water contamination insights through dedicated applications.

## Methodology
- IoT sensors gather diverse water attributes from field and lab setups.  
- Real-time data is streamed and processed on an edge device.  
- A **Random Forest classifier** is deployed to categorize water quality based on standard parameters.  
- YOLOv8 based object detection is used to estimate water bank height for precise contamination analysis.  
- Data augmentation and feature extraction techniques optimize model accuracy.  

## Results
- The prototype is capable of continuous data collection and analysis.  
- Early results indicate successful classification of water quality into designated categories with good accuracy.  
- Real-time monitoring allows for proactive intervention and management.  
- Data visualization interfaces provide easy access to quality indices and parameters.

## Conclusion
This project establishes a foundation for intelligent real-time water quality monitoring using IoT and ML. Ongoing efforts focus on expanding datasets and refining models for enhanced accuracy and reliability.

## Future Work
- Increase dataset coverage for better model generalization and accuracy.  
- Implement transfer learning for faster real-time inference on edge devices.  
- Develop mobile and web applications for broader accessibility.  
- Integrate cloud computing and AI to predict long-term trends and anomalies.

## Acknowledgments
Supervised by Dr. Niharika Anand at Indian Institute of Information Technology, Lucknow.

