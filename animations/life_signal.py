import time
import sys

def animate():
    frames = [
        "   🔱   ",
        "  🔱🔱  ",
        " 🔱⛰️🔱 ",
        "🔱⛰️⚙️🔱",
        " 🔱⚙️🔱 ",
        "  🔱🔱  ",
        "   🔱   "
    ]
    colors = ["\033[92m", "\033[94m", "\033[93m", "\033[91m"] # Green, Blue, Yellow, Red
    
    print("\033[2J\033[H") # Clear screen
    try:
        for _ in range(3): # Run for 3 cycles to show the pulse
            for i, frame in enumerate(frames):
                color = colors[i % len(colors)]
                sys.stdout.write(f"\r{color}{frame}\033[0m")
                sys.stdout.flush()
                time.sleep(0.15)
        print("\n\n--- [TERRAPRIME] Life Signal Pulsing: ACTIVE ---")
    except KeyboardInterrupt:
        print("\n--- [TERRAPRIME] Life Signal Pulsing in Background ---")

if __name__ == "__main__":
    animate()
