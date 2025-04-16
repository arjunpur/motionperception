# Modeling Motion Perception in V1 and MT

**Maintainer**: Arjun Puri  
**Last Updated**: 04/16/2025

## Context

Visual motion processing involves multiple stages in the primate brain. Neurons in primary visual cortex (V1) are selective for oriented edges and their motion direction, forming the basic units of motion processing [1]. However, because of the **aperture problem** (an oriented receptor can only sense motion component perpendicular to its orientation), a single V1 neuron's local view is often ambiguous [2]. The middle temporal area (MT, also called V5) integrates V1 inputs to infer the true global motion of objects [2]. Indeed, area MT plays a crucial role in visual motion perception [3], containing neurons that solve the aperture problem by combining signals from many V1 cells [2]. Some MT neurons are **pattern-selective**, responding to the overall motion of a complex pattern (like a plaid) rather than just its components, whereas others remain **component-selective** like V1 [2]. Furthermore, experiments with stochastic motion (random dot stimuli) have shown that MT population activity correlates with perception – MT neurons likely provide the signals on which motion discrimination decisions are based [4]. This project will recreate these concepts in a computational model, investigating how neural population models for V1 and MT encode motion perception.

## Key Question

How do population codes in V1 and MT transform local motion signals into a robust, global direction estimate? How does this vary across different stimulus types (drifting grating, plaid grating, RDK)?

## Why It Matters
- Local vs. Global Motion: Individual V1 neurons have small receptive fields and can only sense motion orthogonal to their preferred orientation, creating ambiguity (the "aperture problem").
- MT Integration: MT neurons pool signals over larger receptive fields, resolving ambiguities in motion direction and improving robustness in noisy conditions.
- Population Coding & Perception: Understanding the computational principles behind this transformation bridges our knowledge of neural representations and real-world perception, showing how seemingly simple local detectors can collectively give rise to sophisticated motion perception.

## Project Goals
- Implement Motion Stimuli: Drifting gratings, plaid gratings, and RDK, each with parameterized control over direction, coherence, etc.
- Build a V1 Model: A population of direction-tuned units to represent local motion signals, including noise modeling (Poisson or Gaussian).
- Build an MT Model: Pool/Integrate V1 outputs to produce pattern-selective or component-selective MT neurons with broader tuning.
- Decode & Analyze: Apply population decoding (vector averaging, max-likelihood, etc.) to quantify how well local signals or integrated signals recover true stimulus motion.
- Compare & Validate: Examine how the model performs across stimulus types, coherence levels, and parameter manipulations. Plot tuning curves, psychometric-like curves, and compare to known experimental data.

## Repository Structure

```
.
├── stimuli/
│   ├── generate_gratings.py
│   ├── generate_plaids.py
│   └── generate_rdk.py
├── models/
│   ├── v1_model.py
│   ├── mt_model.py
│   └── pooling_schemes.py
├── analysis/
│   ├── decoding.py
│   ├── psychometric_analysis.py
│   └── visualization.py
├── notebooks/
│   ├── 01_Stimulus_Demos.ipynb
│   ├── 02_V1_Population.ipynb
│   ├── 03_MT_Integration.ipynb
│   ├── 04_Decoding_Analysis.ipynb
│   └── 05_Final_Results_and_Figures.ipynb
├── README.md          # (this file)
```

## Project Milestones & Checklist

### 1. Foundational Research & Setup
- [ ] Review Literature: Read core papers on V1 & MT motion processing, and population coding principles.
- [ ] Project Outline: Finalize approach (rate-based vs spiking, which decoding methods to use, etc.).
- [ ] Environment Setup: Install Python libraries, create GitHub repo, confirm everything runs.

### 2. Stimulus Construction
- [ ] Drifting Gratings: Implement code to generate drifting sinusoidal gratings.
- [ ] Plaid Gratings: Implement superposition of two drifting gratings to form plaid stimuli.
- [ ] Random Dot Kinematogram (RDK): Implement coherent vs noise dot motion, adjustable coherence and speed.
- [ ] Visualization: Plot or animate example stimuli to verify correctness.

### 3. V1 Model Layer
- [ ] Single Neuron Tuning: Implement direction-tuned response function (e.g., Gaussian or cosine).
- [ ] Population: Scale up to a population covering all directions; add noise modeling (Poisson/Gaussian).
- [ ] Validate: Plot population responses to drifting grating, plaid, and RDK to see direction peaks.

### 4. MT Model Layer
- [ ] Pooling Mechanism: Integrate multiple V1 neurons' outputs to form MT neurons with broader tuning.
- [ ] Pattern vs Component: Show that some MT neurons can resolve plaid ambiguity, while others remain component-like.
- [ ] Noise & Normalization (Optional): Explore advanced features like divisive normalization.

### 5. Population Decoding
- [ ] Implement Decoders: Vector average, winner-take-all, and (optionally) Bayesian or ML decoders.
- [ ] Compare V1 vs MT: Show how decoding from MT can better recover true motion (especially for plaids or low-coherence RDK).
- [ ] Performance Metrics: Plot psychometric-like curves for coherence levels; measure error or % correct.

### 6. Analysis & Validation
- [ ] Tuning Curves: Characterize direction tuning widths in V1 vs MT.
- [ ] Noise Characteristics: Evaluate trial-to-trial variability, Fano factor, or correlations (if implemented).
- [ ] Parameter Sensitivity: Check how changing number of neurons, noise amplitude, pooling weights affect performance.

### 7. Final Results & Write-Up
- [ ] Figures & Plots: Generate key plots (population activity, tuning curves, decoding performance).
- [ ] Research-Style Report: Draft a blog post / README section with Introduction, Methods, Results, Discussion.
- [ ] GitHub Polishing: Clean code notebooks, add explanatory comments, ensure reproducibility.

### 8. Optional Extensions
- [ ] Spiking Models: Investigate using Brian2 or NEST for a spiking version of the same architecture.
- [ ] Correlated Noise: Add correlated variability in V1 or MT to see how it impacts decoding.
- [ ] Larger Scenes / Depth / Speed: Model additional aspects of motion selectivity in MT.
- [ ] Recurrent / Feedback Connections: Investigate if adding recurrent connectivity within MT (or feedback from MT to V1) enhances or stabilizes direction discrimination.
- [ ] Attention or Top-Down Modulation: Add a simple gating or gain control that represents "attention to motion" and see how it affects performance.
- [ ] Decision Layer (e.g., an LIP-like Module): Implement a drift-diffusion or attractor network model that accumulates the MT response over time until a threshold is reached, replicating reaction-time and choice dynamics.
- [ ] Spiking vs. Rate: Compare a rate-based version of your model to a spiking version to see differences in temporal coding or variability.
- [ ] Spatial Patterns: Look at more complex stimuli (e.g., multiple motion directions in different parts of the visual field). Study how MT might segment or integrate motions.

## References

[1] Gur, M., & Snodderly, D. M. (2007). Direction selectivity in V1 of alert monkeys: evidence for parallel pathways for motion processing. Journal of Physiology, 585(2), 383-400.

[2] Rust, N. C., Mante, V., Simoncelli, E. P., & Movshon, J. A. (2006). How MT cells analyze the motion of visual patterns. Nature Neuroscience, 9(11), 1421-1431.

[3] Heeger, D. J., Simoncelli, E. P., & Movshon, J. A. (1996). Computational models of cortical visual processing. Proceedings of the National Academy of Sciences, 93(2), 623-627.

[4] Britten, K. H., Newsome, W. T., Shadlen, M. N., Celebrini, S., & Movshon, J. A. (1996). A relationship between behavioral choice and the visual responses of neurons in macaque MT. Visual Neuroscience, 13(1), 87-100.
