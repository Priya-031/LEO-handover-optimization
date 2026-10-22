
def select_strongest_satellite(visible_satellites):
    """
    Select the visible satellite with the strongest signal.
    """

    if not visible_satellites:
        return None

    best_satellite = max(
        visible_satellites,
        key=visible_satellites.get
    )

    return best_satellite


# Test example
if __name__ == "__main__":
    visible_satellites = {
        "Satellite A": 80,
        "Satellite C": 60
    }

    best = select_strongest_satellite(visible_satellites)

    print("Selected satellite:", best)
