# 9001VPet
9001VPet – A terminal-based virtual dog pet game in Python
Interact with your dog entirely via the command line—no GUI.

## 📋 Features

- **Six care actions**: Feed, Play, Clean, Sleep, Shake Paw, Lie Down  
- **Real-time stat decay**: Hunger, Happiness, Health and Energy decrease over elapsed time  
- **Dynamic ASCII art**: After each action, the dog’s pose (ASCII art) updates  
- **UI**:  
  - Menu shows three actions per row  
  - Stats print two per row, plus “time since last action”  
- **Random events**: Small chance to find a bone, slip and lose health, etc.  
- **Game over**: If any stat hits 0, the game ends with a “Game Over” message  

---
## ▶️ Usage
├── dogpet.py # Defines the DogPet class (all methods)

├── main.py # Entry point: imports DogPet from dogpet.py and runs the game loop

Run the game by executing: python main.py
