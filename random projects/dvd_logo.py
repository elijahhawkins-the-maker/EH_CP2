import tkinter as tk

class BouncingWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DVD")
        
        # Window dimensions
        self.width, self.height = 250, 250
        
        # Screen dimensions
        self.screen_w = self.root.winfo_screenwidth()
        self.screen_h = self.root.winfo_screenheight()
        
        # Initial position and velocity (pixels per frame)
        self.x, self.y = 100, 100
        self.dx, self.dy = 5, 5
        
        # Basic UI
        label = tk.Label(self.root, text="DVD", font=("Arial", 14))
        label.pack(expand=True)
        
        self.animate()
        self.root.mainloop()

    def animate(self):
        # Update coordinates based on velocity
        self.x += self.dx
        self.y += self.dy
        
        # Check for horizontal collisions (Left/Right edges)
        if self.x <= 0 or self.x >= self.screen_w - self.width:
            self.dx *= -1 # Reverse horizontal direction
            
        # Check for vertical collisions (Top/Bottom edges)
        if self.y <= 0 or self.y >= self.screen_h - self.height:
            self.dy *= -1 # Reverse vertical direction
            
        # Update the window position on the screen
        self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        
        # Schedule the next frame (approximately 60 FPS)
        self.root.after(16, self.animate)

if __name__ == "__main__":
    BouncingWindow()