# Core Motion Energy Model

## Overview
This module focuses on building a complete motion energy model from scratch. You'll implement each component of the Adelson & Bergen (1985) model, understand how they work together, and test the model on various stimuli.

## Learning Objectives
By the end of this module, you will be able to:
- Implement all components of a functional motion energy model
- Create quadrature pairs of spatiotemporal filters
- Compute motion energy through nonlinear operations
- Build a filter bank sensitive to multiple directions and speeds
- Visualize and interpret model responses to different stimuli

## Contents

### Day 15: Filter Bank
- Introduction to the Adelson & Bergen model
- Understanding the model architecture
- Components and information flow
- Mathematical foundations

### Day 16: Spatiotemporal Filters
- Creating space-time Gabor filters
- Implementing directionally selective filters
- Tuning filter parameters for motion selectivity
- Testing filters on simple stimuli

### Day 17: Quadrature Pairs
- Sine and cosine temporal phases
- Implementing quadrature pairs
- Computing energy from filter responses
- Understanding phase invariance

### Day 18: Phase Invariance
- Exploring the squaring and summing operations
- Demonstrating phase invariance properties
- Comparing simple vs. complex cell responses
- Evaluating motion detection performance

### Day 19: Multi-Direction
- Extending the model to multiple directions
- Building a complete direction-selective filter bank
- Implementing orientation tuning
- Testing directional selectivity

### Day 20: Motion Energy Map
- Creating response maps for direction and speed
- Visualizing directional tuning curves
- Implementing speed selectivity
- Building comprehensive motion energy heatmaps

### Day 21: Integration
- Assembling all model components
- End-to-end motion energy computation
- Testing on complex stimuli
- Analyzing model behavior and limitations

## Approach
This module is highly practical, with each topic including:
- Step-by-step model implementation
- Interactive visualizations of model components
- Tests with various motion stimuli
- Hands-on coding exercises with feedback
- Connections to biological mechanisms

## Prerequisites
- Completion of Modules 1-2
- Proficiency with NumPy and SciPy
- Understanding of filtering operations and convolution
- Familiarity with neural response properties 