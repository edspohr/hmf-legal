from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def get_kmeans_colors(image_path, num_colors=5):
    try:
        image = Image.open(image_path)
        image = image.convert('RGBA')
        image = image.resize((150, 150))
        
        # Convert to numpy array
        arr = np.array(image)
        
        # Reshape to list of pixels
        pixels = arr.reshape(-1, 4)
        
        # Filter transparent pixels
        pixels = pixels[pixels[:, 3] > 128]
        
        # Take only RGB
        if len(pixels) > 0:
            rgb_pixels = pixels[:, :3]
            
            kmeans = KMeans(n_clusters=num_colors)
            kmeans.fit(rgb_pixels)
            
            colors = kmeans.cluster_centers_
            
            print(f"K-Means palette for {image_path}:")
            for color in colors:
                hex_color = '#{:02x}{:02x}{:02x}'.format(int(color[0]), int(color[1]), int(color[2]))
                print(hex_color)
        else:
            print("No opaque pixels found.")
            
    except Exception as e:
        print(f"Error: {e}")

get_kmeans_colors('public/logo.png')
