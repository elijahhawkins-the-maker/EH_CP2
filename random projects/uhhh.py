import tkinter as tk
import math
import random

# --- CONFIGURATION SETTINGS ---
POPUP_COUNT = 200       # How many pop-ups to spawn
POPUP_WIDTH = 120     # Width of each pop-up
POPUP_HEIGHT = 120     # Height of each pop-up
ROTATION_SPEED = 10   # Degrees per frame (higher = faster)
ORBIT_RADIUS = 150    # Distance from the mouse cursor
# ------------------------------

def start_multi_prank():
    root = tk.Tk()
    root.withdraw()  # Hide the main "master" window

    popups = []
    # Assign each pop-up a starting angle so they are spaced out
    angles = [random.randint(0, 360) for _ in range(POPUP_COUNT)]
    
    # Create the individual windows
    for i in range(POPUP_COUNT):
        win = tk.Toplevel(root)
        win.overrideredirect(True)
        win.attributes("-topmost", True)
        win.geometry(f"{POPUP_WIDTH}x{POPUP_HEIGHT}")
        
        # Give each one a random color for extra chaos
        color = random.choice(["red", "blue", "green", "purple", "orange", "black"])
        label = tk.Label(win, text="Bruh", fg="white", bg=color, font=("Arial", 10, "bold"))
        label.pack(expand=True, fill="both")
        
        # Block the close button (Alt+F4 still works on the active window)
        win.protocol("WM_DELETE_WINDOW", lambda: None)
        popups.append(win)

    def update_swarm():
        # Get the master mouse position
        mx = root.winfo_pointerx()
        my = root.winfo_pointery()

        for i, win in enumerate(popups):
            # Calculate unique orbit for this window
            rad = math.radians(angles[i])
            new_x = mx + int(ORBIT_RADIUS * math.cos(rad)) - (POPUP_WIDTH // 2)
            new_y = my + int(ORBIT_RADIUS * math.sin(rad)) - (POPUP_HEIGHT // 2)

            win.geometry(f"+{new_x}+{new_y}")
            
            # Increment this specific window's angle
            angles[i] = (angles[i] + ROTATION_SPEED) % 360

        root.after(10, update_swarm)

    update_swarm()
    root.mainloop()

if __name__ == "__main__":
    start_multi_prank()