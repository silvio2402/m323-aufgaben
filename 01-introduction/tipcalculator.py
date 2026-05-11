def calculate_tip(n_people: int):
    if n_people > 5:
        return 0.20  # 20% tip
    if n_people > 0:
        return 0.10  # 10% tip
    return 0.0

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
tip_percentage = calculate_tip(len(names))
print(f"Tip percentage: {tip_percentage * 100}%")