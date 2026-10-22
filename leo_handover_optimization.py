
# Project: LEO Satellite Handover Optimization

print("========================================")
print("   LEO SATELLITE HANDOVER OPTIMIZATION")
print("========================================")

print("Project started successfully!")

# Sample satellite signal quality scores
satellites = {
    "Satellite A": 70,
    "Satellite B": 90,
    "Satellite C": 60
}

print("\nAvailable Satellites:")

for satellite, signal in satellites.items():
    print(satellite, ":", signal)

best_satellite = max(satellites, key=satellites.get)

print("\nBest Satellite:", best_satellite)
print("Signal Quality:", satellites[best_satellite])

print("\n--- HANDOVER SIMULATION ---")

# Sample signal quality at different time steps
signal_history = {
    0: {"Satellite A": 80, "Satellite B": 60, "Satellite C": 40},
    1: {"Satellite A": 65, "Satellite B": 75, "Satellite C": 45},
    2: {"Satellite A": 40, "Satellite B": 85, "Satellite C": 55},
    3: {"Satellite A": 25, "Satellite B": 70, "Satellite C": 80},
}

current_satellite = "Satellite A"

for time, signals in signal_history.items():
    best_satellite = max(signals, key=signals.get)

    # Switch if the current satellite signal becomes weak
    if signals[current_satellite] < 50:
        current_satellite = best_satellite

    print(
        "Time:", time,
        "| Connected Satellite:", current_satellite,
        "| Signal:", signals[current_satellite]
    )