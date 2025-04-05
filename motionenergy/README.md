# Motion Energy Models in Neuroscience - Course

## 📋 Course Overview

This 30-day comprehensive course explores Motion Energy Models in the context of visual neuroscience. Students will gain deep intuition about both the mathematical foundations and computational implementations of these models, with a focus on how they relate to neural mechanisms of motion perception.

The course follows the structure outlined in the knowledge tree, progressing from mathematical foundations to advanced applications. Through a combination of theoretical explanations, interactive visualizations, and hands-on coding exercises, students will build a complete motion energy model and apply it to real-world problems.

## 🎯 Learning Objectives

By the end of this course, students will be able to:

1. Understand the mathematical foundations of motion perception
2. Visualize and analyze motion in spatiotemporal representations
3. Implement spatial and temporal filters for motion detection
4. Build a complete motion energy model from scratch
5. Connect computational models to neurobiological mechanisms
6. Compare motion energy models with other approaches
7. Apply models to practical motion detection problems

## 📚 Course Structure

The course is divided into four modules, each corresponding to one week of the 30-day learning plan:

### Module 1: [Foundations: Visualizing Motion & Math Tools](./0_foundations/)
- Mathematical tools for understanding motion
- Spatiotemporal representation of visual stimuli
- Convolution, filtering, and Fourier analysis

### Module 2: [Visual Neuroscience: From Retina to V1](./1_visual_neuroscience/)
- Neural pathways for visual processing
- Receptive fields and motion-sensitive neurons
- Simple and complex cells in the visual cortex

### Module 3: [Core Motion Energy Model](./2_motion_energy_model/)
- Implementing the Adelson & Bergen model
- Spatiotemporal filters and quadrature pairs
- Directional tuning and motion energy computation

### Module 4: [Extensions, Comparison & Application](./3_extensions_applications/)
- Opponent motion mechanisms
- Comparison with other motion detection models
- Real-world applications and research connections

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.8+
- Basic experience with Python programming
- Familiarity with scientific computing libraries (NumPy, SciPy)
- Basic understanding of calculus and linear algebra

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/arjunpur/motionenergy.git
   cd motionenergy
   ```

2. Create and activate a virtual environment using uv:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows use `.venv\\Scripts\\activate`
   ```

3. Install dependencies using uv:
   ```bash
   uv pip install -r requirements.txt
   ```

4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## �� Course Materials

Each module contains:

- **Jupyter notebooks** with explanations, visualizations, and code
- **Exercises** to reinforce concepts and build skills
- **Example solutions** for self-assessment
- **Supplementary readings** for deeper understanding

## 📅 Recommended Schedule

Follow the [30-day learning plan](./README.md#-30-day-checklist-mastering-motion-energy-models) outlined in the main README.md, which provides a day-by-day breakdown of topics and activities.

## 🔧 Utilities

The course includes several utility modules to help with implementation:

- `filtering.py`: Functions for creating and applying filters
- `stimuli_generation.py`: Tools for generating motion stimuli
- `energy_computation.py`: Functions for computing motion energy
- `visualization.py`: Tools for visualizing filters and responses

## 📚 References

Key papers and resources are listed in the [references section](./references/additional_resources.md).

## 👨‍🏫 How to Use This Course

1. Start with Module 1 and work through the modules sequentially
2. For each topic, first read the notebook explanations
3. Run the interactive demonstrations to build intuition
4. Complete the exercises in each section
5. Check your understanding with the provided quizzes
6. Explore the supplementary readings for deeper insights

Happy learning!


# ✅ 30-Day Checklist: *Mastering Motion Energy Models*

---

### 🔹 **Week 1: Foundations – Visualizing Motion & Math Tools**

**Goal:** Build an intuitive grasp of motion in space-time and basic math tools

| Day | Focus | Task |
|-----|-------|------|
| 1 | Orientation | Read overview of motion energy models (high-level) + review diagram |
| 2 | Visual Stimuli | Visualize drifting gratings in space-time (Python or notebook) |
| 3 | Convolution | Study 1D/2D convolution + practice with kernels |
| 4 | Fourier Basics | Learn Fourier Transform (spatial & temporal frequency) |
| 5 | Filtering | Play with spatial filters (low-pass, Gabor) on images |
| 6 | Spatiotemporal | Build a small 3D stimulus (e.g., moving bar) & try space-time slicing |
| 7 | Reflect & Review | Mind-map what you've learned (motion as slanted plane, filters, convolution) |

---

### 🔹 **Week 2: Visual Neuroscience – From Retina to V1**

**Goal:** Understand how motion is represented biologically

| Day | Focus | Task |
|-----|-------|------|
| 8 | Retina & LGN | Quick read on early vision → highlight transformations from light to code |
| 9 | Receptive Fields | Draw and simulate Gabor-like receptive fields |
|10 | Simple vs. Complex | Understand quadrature pairs + biological meaning |
|11 | V1 Motion | Study direction/orientation selectivity in V1 |
|12 | MT Area | Watch MT/MT+ neuron tuning (direction + speed) |
|13 | Bio–Model Link | Link spatiotemporal filters to V1/MT responses |
|14 | Consolidate | Sketch or explain how motion is computed in cortex from inputs |

---

### 🔹 **Week 3: Core Motion Energy Model**

**Goal:** Construct and understand all components of the model

| Day | Focus | Task |
|-----|-------|------|
|15 | Filter Bank | Study Adelson & Bergen model; write out components |
|16 | Spatiotemporal Filters | Build space-time Gabor filters for 1 direction |
|17 | Quadrature Pairs | Simulate sine/cosine temporal pairs, compute energy |
|18 | Phase Invariance | Understand & demonstrate squaring + summing |
|19 | Multi-Direction | Implement simple filter bank for multiple directions |
|20 | Motion Energy Map | Create response heatmap over direction/speed |
|21 | Integrate | Write a notebook that walks through full model on a simple stimulus |

---

### 🔹 **Week 4: Extension, Comparison & Application**

**Goal:** Use your knowledge to connect with broader ideas

| Day | Focus | Task |
|-----|-------|------|
|22 | Opponent Motion | Add direction-opponent subtraction to your model |
|23 | Biological Validation | Read a neuroscience paper using ME models |
|24 | Comparison | Compare with optical flow (Horn-Schunck or Lucas-Kanade) |
|25 | Code Project | Motion detection on video or simulated eye |
|26 | Research Bridge | Sketch how you might use ME models in a research question |
|27 | Explain It | Make a simple graphic/video where you teach ME models |
|28 | Synthesis | Build a concept map of ME models (math ↔ biology ↔ code) |
|29 | Review + Quiz | Write or quiz yourself on: filters, quadrature, energy, opponent motion |
|30 | Reflection | Reflect on your growth, open questions, and next directions |


---

© 2023 Motion Energy Course 