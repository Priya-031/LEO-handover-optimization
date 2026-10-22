
def select_satellite(current_satellite, signals, min_signal=50, hysteresis=10):
    """
    Select a satellite while avoiding unnecessary handovers.

    signals: dictionary containing visible satellites and signal scores.
    min_signal: minimum acceptable signal score.
    hysteresis: required improvement before switching satellites.
    """

    if not signals:
        return current_satellite

    # Keep the current satellite if its signal is acceptable.
    if current_satellite in signals:
        current_signal = signals[current_satellite]

        if current_signal >= min_signal:
            best_satellite = max(signals, key=signals.get)

            # Switch only if the new satellite is sufficiently better.
            if signals[best_satellite] >= current_signal + hysteresis:
                return best_satellite

            return current_satellite

    # If the current satellite is unavailable or too weak,
    # select the strongest available satellite.
    best_satellite = max(signals, key=signals.get)

    if signals[best_satellite] >= min_signal:
        return best_satellite

    return None


# Test example
if __name__ == "__main__":
    signals = {
        "Satellite A": 65,
        "Satellite B": 70,
        "Satellite C": 45
    }

    current = "Satellite A"

    selected = select_satellite(current, signals)

    print("Current satellite:", current)
    print("Signal scores:", signals)
    print("Selected satellite:", selected)
