# Super-Resolution Generative Adversarial Network (SRGAN) for CT and PET Image Fusion

## Project Overview

This project presents a Super-Resolution Generative Adversarial Network (SRGAN) designed to fuse Computed Tomography (CT) and Positron Emission Tomography (PET) images. The primary objective is to enhance digital health solutions by improving the quality and sensitivity of lesion detection in medical imaging.

## Table of Contents

- [Background](#background)
- [Problem Statement](#problem-statement)
- [Approach](#approach)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Learnings](#learnings)
- [Contributing](#contributing)

## Background

CT and PET imaging are essential techniques in medical diagnostics. However, they have limitations regarding resolution and sensitivity. By fusing these two modalities using advanced machine learning techniques, we aim to provide more accurate and detailed images for better clinical decision-making.

## Problem Statement

Traditional methods of lesion detection often suffer from low sensitivity and poor image quality, making it difficult to accurately diagnose and assess medical conditions. This project addresses these challenges by developing an innovative SRGAN approach to enhance image fusion quality.

## Approach

The approach involves the following key steps:

1. **Data Collection**: Gather CT and PET images from publicly available medical imaging datasets.
2. **Preprocessing**: Normalize and preprocess the images to ensure consistent input for the model.
3. **Model Development**: Implement the SRGAN architecture using Convolutional Neural Networks (CNN) to facilitate high-resolution image generation.
4. **Training**: Train the model on the preprocessed dataset, optimizing for high sensitivity in lesion detection.
5. **Evaluation**: Assess the model's performance through quantitative metrics and visual comparisons.

## Architecture

The SRGAN architecture consists of two primary components:

1. **Generator**: Generates high-resolution images from low-resolution inputs (CT and PET images).
2. **Discriminator**: Distinguishes between real high-resolution images and those produced by the generator, enhancing the generator's ability to produce realistic outputs.

## Installation

To run this project, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/srgan-ct-pet-fusion.git
   cd srgan-ct-pet-fusion
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the SRGAN model for CT and PET image fusion, follow these steps:

1. Place your preprocessed CT and PET images in the designated input directory.
2. Run the training script:
   ```bash
   python train.py
   ```

3. To generate fused images, execute:
   ```bash
   python generate.py --input_ct path_to_ct_image --input_pet path_to_pet_image --output_path path_to_output_image
   ```

## Results

The results section should include:

- **Quantitative Metrics**: PSNR, SSIM, etc.
- **Visual Comparisons**: Before and after images demonstrating the effectiveness of the SRGAN in improving image quality and sensitivity in lesion detection.

## Learnings

From an MBA perspective, this project has provided me with valuable insights, including:

1. **Interdisciplinary Collaboration**: The integration of AI and healthcare highlights the importance of cross-functional teamwork between data scientists and healthcare professionals.
   
2. **Business Impact**: Understanding how advanced technologies like SRGAN can enhance diagnostic accuracy directly ties to improved patient outcomes, which is critical in healthcare decision-making.

3. **Market Potential**: The project illustrates the growing demand for AI-driven solutions in healthcare, presenting opportunities for startups and established companies to innovate in medical imaging.

4. **Project Management**: Coordinating data collection, model training, and evaluation emphasized the importance of effective project management skills in delivering a technical project on time.

5. **User-Centric Design**: Focusing on the end-users—radiologists and clinicians—helped in tailoring the solution to their needs, showcasing the importance of user feedback in product development.

## Contributing

Contributions are welcome! Please follow these steps to contribute to the project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to the branch and create a pull request.
