"""Wir möchten eine App, welche für ein Auto-Rennen die gesamte Zeit für
alle Runden berechnet. Die App soll auch die Durchschnittszeit pro
Auto berechnen. Die erste Runde wird nicht mitgezählt, da es sich
hier um eine "Warm-up" Runde handelt."""


def calculate_total_time(race_times: list[float]) -> float:
    return sum(race_times[1:])  # exclude warm-up round


def calculate_average_time(race_times: list[float]) -> float:
    total_time = calculate_total_time(race_times)
    num_races = len(race_times) - 1  # exclude warm-up round
    if num_races == 0:
        return 0.0
    return total_time / num_races

def main():
    all_race_times = {
        "Car A": [60.5, 58.2, 59.0, 57.8],
        "Car B": [62.0, 61.5, 60.8, 59.9],
        "Car C": [59.8, 58.7, 57.6, 56.4],
    }
    for car, times in all_race_times.items():
        total_time = calculate_total_time(times)
        average_time = calculate_average_time(times)
        print(f"{car}: Total Time = {total_time:.2f} seconds, Average Time = {average_time:.2f} seconds")
        
if __name__ == "__main__":
    main()
