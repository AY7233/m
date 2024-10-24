import numpy as np
import matplotlib.pyplot as plt

def plot_polygon(points, color='blue'):
    points = np.vstack([points, points[0]])  # Close the polygon
    plt.plot(points[:, 0], points[:, 1], color=color)
    plt.fill(points[:, 0], points[:, 1], color=color, alpha=0.5)

def translate(points, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    translated_points = points_homogeneous @ translation_matrix.T
    return translated_points[:, :2]

def scale(points, sx, sy):
    scaling_matrix = np.array([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, 1]])
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    scaled_points = points_homogeneous @ scaling_matrix.T
    return scaled_points[:, :2]

def rotate(points, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                [np.sin(theta), np.cos(theta), 0],
                                [0, 0, 1]])
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    rotated_points = points_homogeneous @ rotation_matrix.T
    return rotated_points[:, :2]

def main():
    plt.figure(figsize=(10, 8))

    # Define a square polygon
    square = np.array([[1, 1],
                       [1, -1],
                       [-1, -1],
                       [-1, 1]])

    # Plot original square
    plt.subplot(231)
    plot_polygon(square, color='blue')
    plt.title('Original Square')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    
    # Translation
    translated_square = translate(square, 2, 1)
    plt.subplot(232)
    plot_polygon(translated_square, color='green')
    plt.title('Translated Square')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    
    # Scaling
    scaled_square = scale(square, 2, 0.5)
    plt.subplot(233)
    plot_polygon(scaled_square, color='red')
    plt.title('Scaled Square')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    
    # Rotation
    rotated_square = rotate(square, 45)
    plt.subplot(234)
    plot_polygon(rotated_square, color='orange')
    plt.title('Rotated Square (45°)')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    
    # Combined transformations
    combined_transform = translate(scale(rotate(square, 45), 2, 0.5), 2, 1)
    plt.subplot(235)
    plot_polygon(combined_transform, color='purple')
    plt.title('Combined Transformations')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
