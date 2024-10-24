import matplotlib.pyplot as plt

INSIDE = 0  
LEFT = 1    
RIGHT = 2   
BOTTOM = 4  
TOP = 8     

def compute_code(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

def cohen_sutherland_line_clip(x0, y0, x1, y1, x_min, y_min, x_max, y_max):
    code0 = compute_code(x0, y0, x_min, y_min, x_max, y_max)
    code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
    clipped = False

    while True:
        if (code0 | code1) == 0:
            clipped = True
            break
        elif (code0 & code1) != 0:
            break
        else:
            code_out = code0 if code0 != 0 else code1
            if code_out & TOP:
                x = x0 + (x1 - x0) * (y_max - y0) / (y1 - y0)
                y = y_max
            elif code_out & BOTTOM:
                x = x0 + (x1 - x0) * (y_min - y0) / (y1 - y0)
                y = y_min
            elif code_out & RIGHT:
                y = y0 + (y1 - y0) * (x_max - x0) / (x1 - x0)
                x = x_max
            elif code_out & LEFT:
                y = y0 + (y1 - y0) * (x_min - x0) / (x1 - x0)
                x = x_min

            if code_out == code0:
                x0, y0 = x, y
                code0 = compute_code(x0, y0, x_min, y_min, x_max, y_max)
            else:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)

    if clipped:
        return (x0, y0), (x1, y1)
    return None

def plot_line(x0, y0, x1, y1, clipped_line=None):
    plt.plot([x0, x1], [y0, y1], color='blue', label='Original Line')
    if clipped_line:
        (x0_clipped, y0_clipped), (x1_clipped, y1_clipped) = clipped_line
        plt.plot([x0_clipped, x1_clipped], [y0_clipped, y1_clipped], color='red', label='Clipped Line')

def main():
    x_min, y_min = 1, 1
    x_max, y_max = 5, 5

    plt.xlim(0, 6)
    plt.ylim(0, 6)
    plt.axhline(y_min, color='black', linestyle='--')
    plt.axvline(x_min, color='black', linestyle='--')
    plt.axhline(y_max, color='black', linestyle='--')
    plt.axvline(x_max, color='black', linestyle='--')
    plt.fill_between([x_min, x_max], y_min, y_max, color='lightgray', alpha=0.5)

    while True:
        print("Enter the coordinates of the line:")
        x0 = float(input("x0: "))
        y0 = float(input("y0: "))
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        
        clipped_line = cohen_sutherland_line_clip(x0, y0, x1, y1, x_min, y_min, x_max, y_max)
        plot_line(x0, y0, x1, y1, clipped_line)

        plt.title("Cohen-Sutherland Line Clipping Algorithm")
        plt.legend()
        plt.grid()
        plt.show()

        cont = input("Do you want to clip another line? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
