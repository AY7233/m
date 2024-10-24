import numpy as np 
import matplotlib.pyplot as plt 

def reflection(points, axis): 
    if axis == 'x': 
        reflection_matrix = np.array([ 
            [1, 0, 0], 
            [0, -1, 0], 
            [0, 0, 1] 
        ]) 
    elif axis == 'y': 
        reflection_matrix = np.array([ 
            [-1, 0, 0], 
            [0, 1, 0], 
            [0, 0, 1] 
        ]) 
    else: 
        raise ValueError("Invalid axis. Choose 'x' or 'y'.") 
    return transformation(points, reflection_matrix) 

def shearing(points, direction, factor): 
    if direction == 'x': 
        shearing_matrix = np.array([ 
            [1, factor, 0], 
            [0, 1, 0], 
            [0, 0, 1] 
        ]) 
    elif direction == 'y': 
        shearing_matrix = np.array([ 
            [1, 0, 0], 
            [factor, 1, 0], 
            [0, 0, 1] 
        ]) 
    else: 
        raise ValueError("Invalid direction. Choose 'x' or 'y'.") 
     
    return transformation(points, shearing_matrix) 

def transformation(points, transformation_matrix): 
    transformed_points = [] 
    for point in points: 
        homogeneous_point = np.array([point[0], point[1], 1]) 
        transformed_point = transformation_matrix @ homogeneous_point 
        transformed_points.append(transformed_point[:2]) 
    return np.array(transformed_points) 

def plot_points(points, color='blue', label=None): 
    x, y = points[:, 0], points[:, 1] 
    plt.scatter(x, y, color=color, label=label) 
    plt.plot(x, y, color=color) 
    plt.axis('equal') 

def user_input(): 
    num_points = int(input("Enter the number of points: ")) 
    points = [] 
    for i in range(num_points): 
        x = float(input(f"Enter x-coordinate of point {i + 1}: ")) 
        y = float(input(f"Enter y-coordinate of point {i + 1}: ")) 
        points.append([x, y]) 
    return np.array(points) 

def menu(): 
    print("Choose the transformation:") 
    print("1. Reflection") 
    print("2. Shearing") 
    return int(input("Enter the number of your choice: ")) 

def main(): 
    points = user_input() 
     
    choice = menu() 

    if choice == 1: 
        axis = input("Enter the axis of reflection (x or y): ").lower() 
        transformed_points = reflection(points, axis) 
        plot_points(points, color='red', label='Original Points') 
        plot_points(transformed_points, color='green', label=f'Reflected across {axis}-axis') 

    elif choice == 2: 
        direction = input("Enter the direction of shearing (x or y): ").lower() 
        factor = float(input(f"Enter the shearing factor in {direction}-direction: ")) 
        transformed_points = shearing(points, direction, factor) 
        plot_points(points, color='red', label='Original Points') 
        plot_points(transformed_points, color='green', label=f'Sheared Points along {direction}-axis') 
    else: 
        print("Invalid choice.") 
        return 
    
    plt.legend() 
    plt.title("2D Transformation: Reflection and Shearing") 
    plt.show() 

if __name__ == "__main__": 
    main()
