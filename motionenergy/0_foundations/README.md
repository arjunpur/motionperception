# Tasks to Complete the 0_foundations Notebooks

## 01_introduction
- Notebook appears to have a good start but is incomplete
- Tasks:
  1. Complete the "5. Course Roadmap" section which was cut off
  2. Add sections on the historical context of motion energy models
  3. Add a section connecting to biological vision
  4. Add links to key research papers

## 02_visual_stimuli
- This notebook is very incomplete, only containing an introduction
- Tasks:
  1. Add sections on different types of motion stimuli:
     - Drifting gratings (implementation and visualization)
     - Random dot kinematograms
     - Moving bars and edges
     - Plaid patterns
  2. Add code examples for generating each stimulus type
  3. Implement visualization of stimuli in both time and space-time
  4. Add section on the properties and applications of each stimulus

## 03_convolution
- Notebook has introduction but missing implementation
- Tasks:
  1. Add section on intuitive understanding of convolution with visual examples
  2. Implement 1D convolution from scratch and visualize it
  3. Implement 2D convolution and apply to images
  4. Add section on convolution properties (associativity, commutativity)
  5. Connect convolution to visual system processing

## 04_fourier_transform
- Basic structure is there but content is incomplete
- Tasks:
  1. Complete the introduction to frequency analysis
  2. Add visualization of spatial and temporal frequencies
  3. Implement and explain the Fourier Transform
  4. Add section on the frequency domain representation of motion
  5. Connect to motion processing in the visual system

## 05_filtering
- Introductory section exists but needs implementation
- Tasks:
  1. Implement and visualize different types of filters (low-pass, high-pass, band-pass)
  2. Add section on filter design considerations
  3. Add detailed section on Gabor filters with implementation
  4. Create examples of filtering in the context of motion detection
  5. Explain filter separability (spatial/temporal)

## 06_spatiotemporal
- Has introduction but needs content development
- Tasks:
  1. Implement functions for creating 3D (x, y, t) stimuli
  2. Add visualization of motion in space-time (2D+time and 3D visualizations)
  3. Add section on spatiotemporal slicing techniques
  4. Implement motion trajectory analysis
  5. Connect to the next module on motion energy models

## 07_review
- Has a good outline but needs expanded integration and exercises
- Tasks:
  1. Complete the conceptual map of motion energy model foundations
  2. Add integrative exercises that combine concepts from all sections
  3. Create visual summaries of key relationships
  4. Add a comprehensive glossary of terms
  5. Include a preview of the next module

## General Tasks for All Notebooks
1. Ensure all code examples are fully implemented and run without errors
2. Add full solutions to all exercises while maintaining educational value
3. Add knowledge checks/quizzes at key points
4. Implement interactive visualizations where appropriate
5. Ensure consistent notation and terminology across all notebooks
6. Add references and further reading at the end of each notebook


# Foundations: Visualizing Motion & Math Tools

## Overview
This module builds the mathematical and conceptual foundations needed to understand motion energy models. You'll develop intuition for how motion is represented in space-time and learn the essential signal processing tools that underlie motion detection.

## Learning Objectives
By the end of this module, you will be able to:
- Visualize motion patterns in the spatiotemporal domain
- Understand and implement basic spatial and temporal filters
- Apply convolution operations to signals and images
- Analyze signals using Fourier transforms
- Create and manipulate visual stimuli for motion perception

## Contents

### [Day 1: Introduction](./01_introduction/)
- Overview of motion energy models
- Historical context and importance
- Basic concepts and terminology
- Motion as orientation in space-time

### [Day 2: Visual Stimuli](./02_visual_stimuli/)
- Creating drifting gratings
- Random dot kinematograms
- Moving bars and edges
- Visualizing motion in space-time

### [Day 3: Convolution](./03_convolution/)
- 1D and 2D convolution operations
- Kernels and filter responses
- Implementing convolution from scratch
- Convolution in the context of visual processing

### [Day 4: Fourier Transform](./04_fourier_transform/)
- Spatial and temporal frequency domains
- Understanding the Fourier transform
- Frequency representation of motion
- Analyzing motion signals in frequency space

### [Day 5: Filtering](./05_filtering/)
- Low-pass, high-pass, and band-pass filters
- Gabor filters and their properties
- Implementing and applying spatial filters
- Filter design considerations

### [Day 6: Spatiotemporal Representation](./06_spatiotemporal/)
- Building 3D visual stimuli
- Space-time slicing techniques
- Analyzing motion trajectories
- Spatiotemporal frequency analysis

### [Day 7: Review & Reflection](./07_review/)
- Knowledge mapping and integration
- Connecting concepts to neural mechanisms
- Synthesizing foundational concepts
- Preparing for the visual neuroscience module

## How to Use This Module

Each section contains:
1. An **overview notebook** with explanations, visualizations, and code examples
2. An **exercises notebook** with hands-on tasks to reinforce your understanding

We recommend:
- Working through each section in order
- Running all the code examples in the overview notebooks
- Completing the exercises before moving to the next section
- Revisiting the review section to solidify your understanding

## Prerequisites
- Basic Python programming
- Familiarity with NumPy and Matplotlib
- Basic understanding of calculus and linear algebra

## Resources
For additional resources, see the [references section](../references/additional_resources.md) of the course. 
