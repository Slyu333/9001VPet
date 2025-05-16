import time
import random

class DogPet:
    def __init__(self, name):
        self.name = name
        self.poses = {
            "default": r"""
           /^ ^\  
          / 0 0 \ 
          V\ Y /V 
           / - \  
          |    \  
          || (__V 
""",
            "feed": r"""
           /^ ^\  
          / o o \   🍖
          V\ Y /V 
           / - \  
""",
            "play": r"""
           /^ ^\   🎾
          / > < \ 
         (   o   )
          \  O  / 
""",
            "clean": r"""
           /^ ^\  
          / 0 0 \   🛁
           \ U /  
""",
            "sleep": r"""
           z Z Z
           /^ ^\  
          / - - \  
         (  -_-  ) 💤
""",
            "shake_paw": r"""
           /^ ^\  
          / 0 0 \  
          V\ y /V  🐾
           /   \  
""",
            "lie_down": r"""
          ________
         /        \
        /  z Z Z   \
        \          /
         \________/
           ( •• )
"""}
        self.last_action = "default"
        self.hunger = 50
        self.happiness = 50
        self.health = 100
        self.energy = 50
        self.last_update = time.time()

    def show_status(self):
        self._apply_time_decay()
        art = self.poses.get(self.last_action, self.poses["default"])
        print(art)


        print(f"name: {self.name}")
        print(f"Hunger:    {self.hunger}/100    Happiness: {self.happiness}/100")
        print(f"Health:    {self.health}/100    Energy:    {self.energy}/100")

        delta = time.time() - self.last_update
        hrs = int(delta // 3600)
        mins = int((delta % 3600) // 60)
        print(f"Time since last action: {hrs}h {mins}m")

        tags = self._status_tags()
        print(f"status: {','.join(tags)}")

    def _status_tags(self):
        tags = []
        if self.hunger < 20:
            tags.append("Hungry")
        if self.happiness < 20:
            tags.append("Bored")
        if self.health < 20:
            tags.append("Unwell")
        if self.energy < 20:
            tags.append("Tired")
        return tags or ["Content"]

    def _apply_time_decay(self):
        """
        Decrease status based on hours passed since last action

        """
        now = time.time()
        hours_passed = (now - self.last_update)/3600
        self.hunger = max(0, self.hunger - int(4*hours_passed))
        self.happiness = max(0, self.happiness - int(3  * hours_passed))
        self.energy    = max(0, self.energy    - int(5  * hours_passed))
        self.health = max(0, self.health - int(2 * hours_passed))
        self.last_update = now

    def is_game_over(self):
        return any([
            self.hunger <= 0,
            self.happiness <= 0,
            self.health <= 0,
            self.energy <= 0
        ])


    def feed(self):
        self.last_action = "feed"
        self._apply_time_decay()
        if self.hunger > 80:
            print(f"{self.name} is not very hungry right now.")
        else:
            self.hunger = min(100, self.hunger + 30)
            print(f"You fed {self.name}. Yum! Hunger +30.")
        self._random_event("feed")

    def play(self):
        self.last_action = "play"
        self._apply_time_decay()
        if self.energy < 20:
            print(f"{self.name} is too tired to play.")
        else:
            self.happiness = min(100, self.happiness + 25)
            self.energy = max(0, self.energy - 20)
            print(f"You played fetch with {self.name}. Happiness +25, Energy -20.")
        self._random_event("play")

    def clean(self):
        self.last_action = "clean"
        self._apply_time_decay()
        print(f"You gave {self.name} a bath. Shiny coat! Happiness +10.")
        self.happiness = min(100, self.happiness + 10)
        self._random_event("clean")

    def sleep(self):
        self.last_action = "sleep"
        self._apply_time_decay()
        print(f"{self.name} curls up and naps... 💤")
        time.sleep(1)  # simulate nap
        self.energy = 100
        self.hunger = max(0, self.hunger - 10)
        print(f"{self.name} woke up refreshed! Energy full, Hunger -10.")

    def shake_paw(self):
        self.last_action = "shake_paw"
        self._apply_time_decay()
        print(f"{self.name} lifts a paw and shakes it! 🐾 Happiness +5")
        self.happiness = min(100, self.happiness + 5)

    def lie_down(self):
        self.last_action = "lie_down"
        self._apply_time_decay()
        print(f"{self.name} lies down and rests.")

    def _random_event(self, context):
        chance = random.random()
        if context == "play" and chance < 0.1:
            print(f"Lucky find! {self.name} dug up a bone. Hunger +10.")
            self.hunger = min(100, self.hunger + 10)
        elif context == "clean" and chance < 0.1:
            print(f"Oh no! {self.name} slipped and got a little scrape. Health -5.")
            self.health = max(0, self.health - 5)

