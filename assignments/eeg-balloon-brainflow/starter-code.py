"""Starter code for the EEG Balloon with BrainFlow assignment."""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse
from brainflow.board_shim import BoardIds, BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter

BOARD_ID = BoardIds.SYNTHETIC_BOARD.value
WINDOW_SECONDS = 2
MIN_HEIGHT = 1.5
MAX_HEIGHT = 8.0
MOVEMENT_SPEED = 1.2
SMOOTHING = 0.15


def calculate_wave_score(
    data, eeg_channels: list[int], sampling_rate: int, baseline_ratio: float
) -> tuple[float, float]:
    """Return a bounded wave score and the current alpha-to-beta ratio."""

    # BrainFlow returns average powers in this order:
    # delta, theta, alpha, beta, gamma.
    average_powers, _ = DataFilter.get_avg_band_powers(
        data, eeg_channels, sampling_rate, True
    )

    # TODO: Read alpha and beta from average_powers.
    # TODO: Calculate alpha / (beta + a small nonzero value).
    # TODO: Compare the ratio with baseline_ratio and clamp the score to [-1, 1].
    # TODO: Print alpha, beta, ratio, and score before returning them.
    raise NotImplementedError


def create_scene():
    """Create the balloon visualization and return its changing artists."""

    figure, axes = plt.subplots(figsize=(7, 7))
    axes.set(xlim=(0, 10), ylim=(0, 10), title="BrainFlow EEG Balloon")
    axes.set_facecolor("#bde8ff")
    axes.axhspan(0, 1, color="#70b85d")
    axes.set_xticks([])
    axes.set_yticks([])

    balloon = Ellipse((5, 4), width=2.2, height=2.8, color="#ff5d73")
    axes.add_patch(balloon)
    (string,) = axes.plot([5, 5], [1.5, 2.6], color="#555555", linewidth=2)
    score_text = axes.text(0.3, 9.5, "Wave score: waiting for data")
    return figure, axes, balloon, string, score_text


def main() -> None:
    """Stream EEG data and animate the balloon."""

    params = BrainFlowInputParams()
    board = BoardShim(BOARD_ID, params)
    sampling_rate = BoardShim.get_sampling_rate(BOARD_ID)
    eeg_channels = BoardShim.get_eeg_channels(BOARD_ID)
    window_samples = WINDOW_SECONDS * sampling_rate

    figure, _, balloon, string, score_text = create_scene()
    state = {"height": 4.0, "baseline_ratio": None}

    def update(_frame):
        data = board.get_current_board_data(window_samples)
        if data.shape[1] < sampling_rate:
            return balloon, string, score_text

        # Establish a baseline from the first complete data window.
        if state["baseline_ratio"] is None:
            powers, _ = DataFilter.get_avg_band_powers(
                data, eeg_channels, sampling_rate, True
            )
            state["baseline_ratio"] = float(powers[2] / (powers[3] + 1e-12))

        score, ratio = calculate_wave_score(
            data, eeg_channels, sampling_rate, state["baseline_ratio"]
        )

        # TODO: Compute a target height from score and MOVEMENT_SPEED.
        # TODO: Clamp the target to MIN_HEIGHT and MAX_HEIGHT.
        # TODO: Smooth state["height"] toward the target using SMOOTHING.

        height = state["height"]
        balloon.center = (5, height)
        string.set_data([5, 5], [1, height - 1.4])
        score_text.set_text(f"Wave score: {score:+.2f}  Ratio: {ratio:.2f}")
        return balloon, string, score_text

    animation = None
    streaming = False
    try:
        board.prepare_session()
        board.start_stream()
        streaming = True
        animation = FuncAnimation(
            figure, update, interval=250, blit=False, cache_frame_data=False
        )
        plt.show()
    finally:
        # Keep a reference until the window closes, then safely free the board.
        _ = animation
        if streaming:
            board.stop_stream()
        if board.is_prepared():
            board.release_session()


if __name__ == "__main__":
    main()
