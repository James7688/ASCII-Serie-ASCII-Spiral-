import math
import time
import shutil
import sys

CLEAR = "\033[2J\033[H"

def main():
    cols, rows = shutil.get_terminal_size(fallback=(80, 24))

    w, h = cols, rows
    center_x, center_y = w // 2, h // 2

    t = 0 

    try:
        while True:
            sys.stdout.write(CLEAR)

            for y in range(h):
                line = []
                for x in range(w):
  
                    dx = x - center_x
                    dy = y - center_y
                    dist = math.sqrt(dx*dx + dy*dy)

                    angle = math.atan2(dy, dx)

                    v = math.sin(dist * 0.25 - t + angle * 2)

                    if v > 0.6:
                        ch = "@"
                    elif v > 0.2:
                        ch = "*"
                    elif v > -0.2:
                        ch = "+"
                    elif v > -0.6:
                        ch = "-"
                    else:
                        ch = " "

                    line.append(ch)

                sys.stdout.write("".join(line) + "\n")

            sys.stdout.flush()
            t += 0.15       
            time.sleep(0.03)  

    except KeyboardInterrupt:
        sys.stdout.write("\033[0m\n")

if __name__ == "__main__":
    main()
