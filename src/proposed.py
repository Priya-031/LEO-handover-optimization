
def select_satellite(current_satellite, signals, min_signal=50, hysteresis=10):
    """Reduce unnecessary handovers using a switching threshold."""

    if not signals:
        return None

    best_satellite = max(signals, key=signals.get)

    if current_satellite not in signals:
        return best_satellite if signals[best_satellite] >= min_signal else None

    current_signal = signals[current_satellite]

    if current_signal < min_signal:
        return best_satellite if signals[best_satellite] >= min_signal else None

    if signals[best_satellite] >= current_signal + hysteresis:
        return best_satellite

    return current_satellite


if __name__ == "__main__":
    signals = {
        "Satellite A": 65,
        "Satellite B": 70,
        "Satellite C": 45
    }

    selected = select_satellite("Satellite A", signals)
    print("Selected satellite:", selected)
