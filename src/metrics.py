
def count_handovers(satellite_history):
    """Count how many times the connected satellite changes."""

    handovers = 0

    for i in range(1, len(satellite_history)):
        if satellite_history[i] != satellite_history[i - 1]:
            handovers += 1

    return handovers


def calculate_average_signal(signal_history):
    """Calculate the average signal quality."""

    if not signal_history:
        return 0

    return sum(signal_history) / len(signal_history)


# Test example
if __name__ == "__main__":
    satellite_history = [
        "Satellite A",
        "Satellite A",
        "Satellite B",
        "Satellite B",
        "Satellite C"
    ]

    signal_history = [80, 75, 85, 70, 90]

    print("Total handovers:", count_handovers(satellite_history))
    print(
        "Average signal quality:",
        round(calculate_average_signal(signal_history), 2)
    )
