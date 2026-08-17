# 📘 Assignment: EEG Balloon with BrainFlow

## 🎯 Objective

Read basic EEG signals with BrainFlow, summarize common brain-wave band patterns, and create an animated balloon that rises or lowers as the overall pattern changes. Begin with BrainFlow's synthetic board so the project works without biosensor hardware.

## 📝 Tasks

### 🛠️	Stream EEG Data

#### Description
Connect to BrainFlow's synthetic board and retrieve rolling windows of EEG samples. Use the supplied session setup and cleanup code so the stream always stops correctly.

#### Requirements
Completed program should:

- Use `BoardIds.SYNTHETIC_BOARD` while developing without physical hardware
- Prepare a BrainFlow session, start its stream, and request the latest two seconds of samples
- Obtain the board's EEG channel indices and sampling rate through `BoardShim`
- Skip analysis until at least one second of samples is available
- Stop the stream and release the session when the visualization closes


### 🛠️	Measure Overall Wave Patterns

#### Description
Summarize the EEG channels with BrainFlow's average band-power calculation. Convert the alpha and beta values into one bounded score that can control the balloon.

#### Requirements
Completed program should:

- Call `DataFilter.get_avg_band_powers()` with all available EEG channels
- Read the alpha and beta powers from the returned delta, theta, alpha, beta, and gamma order
- Calculate an alpha-to-beta ratio using a small nonzero denominator to avoid division by zero
- Compare the current ratio with a baseline and return a score between `-1.0` and `1.0`
- Print the current alpha power, beta power, ratio, and score for observation


### 🛠️	Animate the Balloon

#### Description
Use Matplotlib to display a balloon whose vertical position responds smoothly to the EEG score. Positive scores should lift it, while negative scores should lower it.

#### Requirements
Completed program should:

- Draw a balloon, string, sky, and ground in a Matplotlib figure
- Update the visualization several times per second with `FuncAnimation`
- Move the target height up for positive scores and down for negative scores
- Smooth each movement so the balloon does not jump abruptly between positions
- Keep the balloon within the visible sky and show the current score on screen


### 🛠️	Test and Tune the Experience

#### Description
Run the visualization with synthetic data, verify its behavior, and adjust the movement constants to produce a clear animation.

#### Requirements
Completed program should:

- Run without biosensor hardware by using the synthetic board
- Display continuously for at least 30 seconds without crashing
- Demonstrate both upward and downward motion by temporarily testing positive and negative scores
- Choose and document sensible values for movement speed, smoothing, and height limits in code comments
- Treat the visualization as an educational demonstration, not a medical or diagnostic tool