# Task List for 1_visual_neuroscience

This document outlines the tasks for developing the "Visual Neuroscience: From Retina to V1" module of the Motion Energy Models course.

## General Requirements
- Each subsection should have:
  - `overview.ipynb`: Teaching materials with explanations, visualizations, and demonstrations
  - `exercises.ipynb`: Coding exercises for students to implement
- Focus on student implementation with proper scaffolding
- Build on foundations from the previous module
- Lead towards the motion energy model in the next module

## Tasks by Section

### 01_retina_lgn
- **Overview notebook** ✅
  - Explain retinal structure and function ✅
  - Describe ON/OFF receptive fields ✅
  - Cover center-surround organization ✅
  - Explain temporal properties of retinal cells ✅
  - Show LGN organization and function ✅
  - Illustrate magnocellular vs. parvocellular pathways ✅
  - Create visualizations of receptive field responses ✅
- **Exercises notebook** ✅
  - Implement simple center-surround receptive fields ✅
  - Code temporal filters for ON/OFF responses ✅
  - Simulate magnocellular vs. parvocellular responses to stimuli ✅

### 02_receptive_fields
- **Overview notebook** ✅
  - Explain Gabor-like receptive fields in V1 ✅
  - Cover spatial frequency and orientation tuning ✅
  - Describe receptive field mapping techniques ✅
  - Show receptive field changes across the visual hierarchy ✅
  - Demonstrate how Gabors approximate V1 receptive fields ✅
- **Exercises notebook** ✅
  - Implement Gabor filters with different parameters ✅
  - Apply filters to static images ✅
  - Visualize spatial frequency and orientation tuning curves ✅

### 03_simple_complex_cells
- **Overview notebook** ✅
  - Explain simple vs. complex cell properties ✅
  - Describe phase sensitivity vs. phase invariance ✅
  - Introduce quadrature pairs concept ✅
  - Show how complex cells combine simple cell outputs ✅
  - Explain hierarchical processing for feature detection ✅
- **Exercises notebook** ✅
  - Implement simple and complex cell models ✅
  - Create quadrature pairs of Gabor filters ✅
  - Demonstrate phase invariance through coding exercises ✅

### 04_v1_motion
- **Overview notebook** ✅
  - Explain direction selectivity in V1 ✅
  - Cover orientation vs. direction tuning ✅
  - Describe spatiotemporal receptive fields ✅
  - Show how space-time inseparable filters detect motion ✅
  - Illustrate the aperture problem ✅
- **Exercises notebook** ✅
  - Implement space-time inseparable filters ✅
  - Create direction tuning curves ✅
  - Simulate V1 responses to moving stimuli ✅
  - Explore the aperture problem through code ✅

### 05_mt_area
- **Overview notebook** ✅
  - Describe MT/V5 area structure and function ✅
  - Explain direction and speed tuning in MT ✅
  - Cover pattern vs. component motion cells ✅
  - Illustrate hierarchical processing from V1 to MT ✅
  - Describe MT's role in solving the aperture problem ✅
  - Demonstrate population coding of motion direction and speed ✅
  - Show how MT integrates local motion signals into global percepts ✅
- **Exercises notebook** ✅
  - Implement simple MT neuron models ✅
  - Create direction/speed tuning maps ✅
  - Simulate pattern and component selective responses ✅
  - Build models for integrating V1 outputs into MT responses ✅
  - Implement a vector averaging model for motion integration ✅
  - Code a basic solution to the aperture problem using MT-like spatial pooling ✅

### 06_bio_model_link
- **Overview notebook** ✅
  - Connect biological neurons to computational models ✅
  - Map spatiotemporal filters to V1/MT responses ✅
  - Explain how motion energy relates to neural computations ✅
  - Bridge between biology and upcoming model implementation ✅
- **Exercises notebook** ✅
  - Create biologically-inspired filters ✅
  - Compare model outputs to known neural responses ✅
  - Design filters that match specific neural properties ✅

### 07_consolidation
- **Overview notebook**
  - Summarize the visual motion processing pathway
  - Review key concepts from earlier sections
  - Preview motion energy model implementation
  - Present integrative examples of motion computation
- **Exercises notebook**
  - Integrate concepts from previous sections
  - Implement a simplified motion detection system
  - Prepare for motion energy model implementation

## Implementation Timeline
1. Create skeleton notebooks for all sections
2. Develop core content for each overview notebook
3. Design scaffolded exercises with appropriate difficulty progression
4. Add visualizations and interactive components
5. Ensure smooth transitions between sections
6. Review content for accuracy and educational effectiveness

## Dependencies and Resources
- Build on foundations module concepts (convolution, Fourier, filtering)
- Prepare students for motion energy model implementation
- Use NumPy, SciPy, Matplotlib for implementations
- Create reusable utilities for visualizations and simulations

## Completed Sections
- 01_retina_lgn: Both overview and exercises notebooks completed
- 02_receptive_fields: Both overview and exercises notebooks completed
- 03_simple_complex_cells: Both overview and exercises notebooks completed
- 04_v1_motion: Both overview and exercises notebooks completed
- 05_mt_area: Both overview and exercises notebooks completed
- 06_bio_model_link: Both overview and exercises notebooks completed