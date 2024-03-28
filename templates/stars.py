import random

for i in range(200):
    top = random.randrange(1,115)
    left = random.randrange(1,100)
    delay = random.random() * 5 
    print(f"<div class='star' style='top: {top}%; left: {left}%; animation-delay: {delay}s'></div>")

