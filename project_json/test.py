import random

data = [
    {"key": "Guido van Rossum", "isTrue": True},
    {"key": "Monty Python", "isTrue": False},
    {"key": "Stefen Houking", "isTrue": False},
    {"key": "Pavel Durov", "isTrue": False}
]

# 1️⃣ "isTrue": False bo'lgan obyektlarni ajratamiz
false_items = [item for item in data if not item["isTrue"]]
print(false_items)

# 2️⃣ Agar kamida 2 ta bo'lsa, tasodifiy 2 tasini tanlaymiz va olib tashlaymiz
if len(false_items) >= 2:
    to_remove = random.sample(false_items, 2)  # Tasodifiy 2 ta tanlash
    data = [item for item in data if item not in to_remove]  # Ularni ro‘yxatdan o‘chirish

# Natijani chop etamiz
print(data)
