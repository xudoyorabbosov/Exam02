def reoder_fish (fish):
    parts = fish.split()
    return f"{parts[1]} {parts[2]} {parts[0]}"
print(reoder_fish("Abbosov Xudoyor Fayzulloevich"))