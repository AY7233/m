import matplotlib.pyplot as plt

def clip_polygon(subject_polygon, clip_polygon):
    def inside(p, edge_start, edge_end):
        return (edge_end[0] - edge_start[0]) * (p[1] - edge_start[1]) > (edge_end[1] - edge_start[1]) * (p[0] - edge_start[0])

    def compute_intersection(p1, p2, edge_start, edge_end):
        denom = (edge_end[1] - edge_start[1]) * (p2[0] - p1[0]) - (edge_end[0] - edge_start[0]) * (p2[1] - p1[1])
        if denom == 0:
            return None
        t = ((edge_end[0] - edge_start[0]) * (p1[1] - edge_start[1]) - (edge_end[1] - edge_start[1]) * (p1[0] - edge_start[0])) / denom
        return p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1])

    output_polygon = subject_polygon

    for i in range(len(clip_polygon)):
        edge_start = clip_polygon[i]
        edge_end = clip_polygon[(i + 1) % len(clip_polygon)]
        input_polygon = output_polygon
        output_polygon = []

        if not input_polygon:
            break

        S = input_polygon[-1]
        for E in input_polygon:
            if inside(E, edge_start, edge_end):
                if not inside(S, edge_start, edge_end):
                    intersection = compute_intersection(S, E, edge_start, edge_end)
                    if intersection:
                        output_polygon.append(intersection)
                output_polygon.append(E)
            elif inside(S, edge_start, edge_end):
                intersection = compute_intersection(S, E, edge_start, edge_end)
                if intersection:
                    output_polygon.append(intersection)
            S = E

    return output_polygon

def plot_polygon(polygon, color='blue', label='Polygon'):
    if polygon:
        x, y = zip(*polygon)
        plt.fill(x, y, color=color, alpha=0.5, label=label)
        plt.plot(x, y, color=color)

def get_polygon_input(polygon_name):
    points = []
    num_points = int(input(f"Enter the number of points for the {polygon_name} (minimum 3): "))
    for i in range(num_points):
        x = float(input(f"Enter x-coordinate of point {i + 1}: "))
        y = float(input(f"Enter y-coordinate of point {i + 1}: "))
        points.append((x, y))
    return points

def menu():
    print("\nMenu:")
    print("1. Clip a polygon")
    print("2. Exit")
    return int(input("Enter your choice: "))

def main():
    while True:
        choice = menu()
        if choice == 1:
            print("Define the Subject Polygon:")
            subject_polygon = get_polygon_input("subject polygon")
            print("Define the Clipping Polygon:")
            clip_polygon_input = get_polygon_input("clipping polygon")

            clipped_polygon = clip_polygon(subject_polygon, clip_polygon_input)

            plt.figure()
            plt.xlim(-10, 10)
            plt.ylim(-10, 10)

            plot_polygon(subject_polygon, color='blue', label='Subject Polygon')
            plot_polygon(clip_polygon_input, color='red', label='Clipping Polygon')
            plot_polygon(clipped_polygon, color='green', label='Clipped Polygon')

            plt.title("Sutherland-Hodgman Polygon Clipping Algorithm")
            plt.legend()
            plt.grid()
            plt.show()
        elif choice == 2:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
