players = [("Aria", 88, True), ("Kael", 95, False), ("Zane", 91, True), ("Mira", 76, True), ("Lyra", 99, True), ("Dax", 84, True)] 

active = [p for p in players if p[2]]

top3 = sorted(active, key=lambda p: p[1], reverse=True)[:3]

result = [f"Rank {i}: {p[0]} ({p[1]})"for i, p in enumerate(top3, start=1)]

print(result)