# Motion Energy + Switching Observer for Multi-Directional Motion Perception

**Maintainer**: Arjun Puri  
**Last Updated**: 04/13/2025

---

**In a nutshell**, this README:

- Explains **why** the project matters in the context of perceptual decision-making.
- Describes **what** each component of the simulation does (RDK stimuli, motion energy, models).
- Provides **clear instructions** for how to set up, run, and analyze results.
- Outlines the **broader significance** (comparing switching vs. accumulator approaches for multi-direction tasks).

## 1. Overview

This repository implements simulations and computational models of human motion perception using **random dot kinematograms (RDKs)**. Specifically, it examines a recent challenge to the classical Bayesian integration framework: **instead of continuously combining sensory likelihood with a prior, humans may \_switch\_ on each trial**—sometimes trusting the prior, sometimes trusting the sensory evidence. This phenomenon can lead to **bimodal** distributions of perceptual estimates, which pure Bayesian accounts do not naturally predict.

We combine:

1. A **Motion Energy** model of low-level visual processing.
2. A **Switching Observer** model that selects between prior- or sensory-driven estimates.
3. A **Decision-making Model** (e.g. a multi-accumulator or race model, a generalized drift-diffusion, etc.) for comparison.

The aim is to see **how closely** these models replicate the observed behavioral patterns—such as **bimodal direction estimates**—and to examine the interplay between **prior knowledge** and **sensory evidence** in multi-direction motion perception tasks.

---

## 2. Motivation

- **Empirical Context**: Laquitaine & Gardner (2018) showed that when humans judge motion directions that deviate from their prior expectations, they often yield **two clusters** of estimates: one near the prior and one near the true motion. This runs counter to a straightforward Bayesian view, which would predict a single “compromise” peak.
- **Why This Project?**
    - **Mechanistic Insight**: We explore a more **neural-like** approach by simulating early visual processing with motion energy filters, then feeding that into decision models.
    - **Comparative Analysis**: We compare the **Switching Observer** (discrete selection of prior vs. evidence) with a **multi-accumulator** or **drift diffusion** style integration approach.
    - **Multi-Directional Extension**: Standard drift-diffusion is often binary (left vs. right). Here, we implement or approximate a *race model* (multiple accumulators, one per direction) so we can handle more than two possible directions (e.g. four or eight directions). This captures more realistic scenarios where motion could be in any of several angles.

---

## 3. Project Goals and Questions

1. **Replicate Bimodal Estimates**
    - Show that a **switching observer** operating on motion energy signals can produce **bimodal** clusters (one near prior mean, one near the true stimulus).
2. **Compare Decision Models**
    - Implement an **accumulation-based** or **race** model for multi-direction choices. Determine if it exhibits similar or different distributions of final estimates and how it incorporates prior bias.
3. **Investigate Prior vs. Sensory Reliability**
    - Manipulate the **strength of the prior** (broad vs. narrow) and **stimulus coherence** (low vs. high). See how these factors influence the probability of switching or the speed of accumulation in each model.
4. **Assess Model Performance**
    - Evaluate *accuracy*, *distribution of estimates*, *bimodality*, and potentially *reaction times* (if implementing time-based accumulation). Compare these metrics to highlight differences between a “switching” strategy and a “continuous accumulation” strategy.

Ultimately, we aim to understand **how a seemingly “heuristic” switching observer** might approximate or diverge from **Bayesian optimal** performance—and how that might be supported by neural-level motion processing.

---

## 4. Repository Structure

```
.
├── README.md                <-- You are here (project overview)
├── src/
│   ├── stimuli.py           <-- RDK generation code (multi-direction)
│   ├── filters.py           <-- Motion energy or spatiotemporal filter utilities
│   ├── observer_switching.py <-- Switching observer model
│   ├── observer_accumulator.py <-- Multi-accumulator / Race / DDM-based model
│   ├── analysis.py          <-- Common analysis functions, e.g. for computing errors, distributions
│   └── utils.py             <-- Utility functions (e.g. circular stats, param management)
├── notebooks/
│   ├── 01_stimulus_demo.ipynb <-- Interactive RDK generation and visualization
│   ├── 02_motion_energy.ipynb <-- Exploring filter responses and direction tuning
│   ├── 03_switching_model.ipynb <-- Running the switching observer across conditions
│   ├── 04_accumulator_model.ipynb <-- Running the race / multi-accumulator model
│   └── 05_analysis_plots.ipynb   <-- Producing final figures, comparing model results
├── experiments/
│   ├── config.yaml             <-- Example parameters for batch runs (coherence levels, prior widths, etc.)
│   ├── run_experiment.py       <-- Command-line script to run a series of trials for each model
│   └── ...
├── results/
│   ├── data/                   <-- Saved simulation data (.csv, .npy, etc.)
│   └── figures/                <-- Final plots/images
├── docs/ 
│   └── project_report.md       <-- Research writeup
├── pyproject.toml
```

---

## 5. Methods Outline

### 5.1 Random Dot Kinematogram (RDK)
- Generate multi-direction stimuli: on each trial, the “true” motion direction is sampled from a distribution (e.g. uniform among {0°, 90°, 180°, 270°}, or a continuous distribution).
- Vary **coherence**: a fraction of dots move in the true direction, the rest move randomly.
- Implement standard RDK logic: each frame updates dots, wraps around edges, etc.

### 5.2 Motion Energy Filtering
- Use **spatiotemporal Gabor filters** or a simplified correlation-based approach to estimate motion direction from raw frames.
- Return either a **time series** of directional energy (for each frame) or an **aggregate direction tuning** (e.g. filter responses across multiple angle channels).

### 5.3 Decision Models

#### 5.3.1 Switching Observer
- **Prior**: define a distribution or just a set of expectations over possible directions (e.g. more likely 0° vs. uniform).
- **Sensory**: from the motion energy output, pick the most likely direction(s) or get a measure of reliability.
- **Switch**: on each trial, either adopt the prior-based guess or the sensory-based guess, according to a reliability threshold (probabilistic or deterministic).
- **Output**: final reported direction (leading to discrete categories or a continuous angle, depending on setup).

#### 5.3.2 Multi-Accumulator (or Race) Model
- **Parallel accumulators**: each direction has an accumulator that integrates the (noisy) evidence favoring that direction over time.
- **Initial bias**: incorporate prior knowledge by starting accumulators at different levels or modulating drift rates.
- **Decision**: whichever accumulator hits the threshold first is the chosen direction. (Alternatively, after a fixed time, pick the accumulator with the highest value.)
- **Output**: chosen direction, and optionally reaction time.

### 5.4 Analysis
- **Accuracy**: compare chosen direction to ground truth.
- **Distribution of Estimates**: check for **bimodality** or multi-peaked outcomes.
- **Effect of Coherence**: plot how performance changes from low to high coherence.
- **Effect of Prior**: see how a strong prior biases the decisions or leads to more switching.
- **Reaction Times** (if using time-based accumulators): distribution or mean RT as a function of coherence.

---

## 6. Installation and Usage

1. **Install dependencies** (e.g., into a virtual environment):

TODO: Update this with `uv` commands

2. **Run a demo notebook** (for RDK stimulus generation):
   ```bash
   jupyter notebook notebooks/01_stimulus_demo.ipynb
   ```
   This will demonstrate how the random dot stimuli look and let you tweak parameters.

3. **Experiment Script**:
    - Edit `experiments/config.yaml` to set the range of coherence levels, directions, prior distributions, etc.
    - Run:
      ```bash
      python experiments/run_experiment.py
      ```
    - Results (model outputs, logs, etc.) will be saved in the `results/data/` directory.

4. **Analysis and Figures**:
    - Open `notebooks/05_analysis_plots.ipynb` to load simulation data, generate histograms, psychometric curves, etc.
    - Final plots will be saved to `results/figures/`.

---

## 7. Expected Results

- **Switching Observer**:
    - Should yield **bimodal** distributions of reported directions when the true motion direction diverges from the prior’s mean *and* the sensory evidence is low/moderate reliability.
    - As coherence increases, it should rely more consistently on the true motion direction.
- **Multi-Accumulator**:
    - With a prior bias, you may see a shift in the probability of choosing certain directions.
    - You typically get a single “winning accumulator” but can see how often the prior-favored accumulator wins under low vs. high coherence.
- **Comparison**:
    - Does the multi-accumulator also produce discrete “switches” or a more graded pattern of decisions?
    - Are there conditions where the two models behave similarly in average accuracy but differ in the shape of the distribution of chosen directions?

---

## 8. Future Extensions

1. **Continuous Angles**: Move beyond discrete directions, implementing a continuous race or “map” of accumulators.
2. **Parameter Fitting**: Fit the models to actual human data (if available) to see which better explains the distribution of estimates.
3. **Neural Implementation**: Replace the single-likelihood readout with a more biologically detailed neural network model or hierarchical Bayesian approach.
4. **Reaction Time Analysis**: Compare predicted RT distributions from the multi-accumulator approach to behavioral RT data.

---

## 9. References

- **Laquitaine & Gardner (2018)**: *A Switching Observer for Human Perceptual Estimation.* Neuron, 97(2), 462–474.
- **Adelson & Bergen (1985)**: *Spatiotemporal energy models for the perception of motion.* JOSA A, 2(2), 284–299.
- **Gold & Shadlen (2007)**: *The neural basis of decision making.* Annual Review of Neuroscience, 30, 535–574. (Covers drift diffusion in perceptual tasks)
- **Churchland et al. (2008)**: *Decision-making with multiple alternatives.* Nature Neuroscience, 11, 693–702. (Discusses multi-accumulator or race models)
- More references in `docs/project_report.md`.

---

### Contact

For questions or feedback, please reach out at arjunpur2@gmail.com