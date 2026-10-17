import random

challenges = {
 "happy": ["Придумай назву для своєї гри", "Напиши 3 речі, які сьогодні вдалися"],
 "tired": ["Зроби перерву на 5 хвилин", "Намалюй простий план свого дня"],
 "bored": ["Придумай нове правило для улюбленої гри","Зміни щось маленьке у своїй кімнаті"]
}

default_challenges = ["Випий води", "Запиши одну маленьку ціль на сьогодні"]

def choose_challenge(mood, energy,mode):
 if mood == "happy":
  challenge = random.choice(challenges["happy"])
 elif mood in ("tired", "bored"):
  challenge = random.choice(challenges[mood])
 else:
  challenge = default_challenges[2]
 if energy >= 7:
  challenge = challenge + " і зроби це просто зараз!"
 return challenge

def calculate_points(energy, mode):
 if energy < 1 or energy > 10:
  return 0

 points = 5  # базові бали

 if energy >= 7:
  points = points + 3
 elif energy <= 3:
  points = points + 1

 if mode == "study":
  points = points + 2
 return points
print("=== Генератор міні-челенджів ===")
name = input("Як тебе звати? ")
mood = input("Який у тебе настрій? happy / tired / bored: ")
energy = int((input("Скільки в тебе енергії від 1 до 10? ")))
mode = input("Обери режим fun або study: ")
challenge = choose_challenge(mood, energy,mode)
points = calculate_points(energy, mode)
print()
print(f"{name}, твій челендж:")
print(challenge)
print(f"Бали за виконання: {points}")