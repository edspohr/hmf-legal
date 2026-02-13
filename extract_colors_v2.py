from PIL import Image
from collections import Counter

def get_dominant_colors(image_path, num_colors=20):
    try:
        image = Image.open(image_path)
        image = image.convert('RGBA')
        # Resize for faster processing
        image = image.resize((150, 150))
        pixels = list(image.getdata())
        
        filtered_pixels = []
        for r, g, b, a in pixels:
            # Ignore transparent
            if a < 128:
                continue
            # Ignore pure black/white/grays (if strictly equal r=g=b)
            # This is a heuristic to find the colored parts
            if abs(r - g) < 20 and abs(g - b) < 20 and abs(r - b) < 20:
                 continue
            filtered_pixels.append((r, g, b))

        counts = Counter(filtered_pixels)
        common = counts.most_common(num_colors)
        
        print(f"Dominant non-grayscale colors in {image_path}:")
        for color, count in common:
            hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
            print(f"{hex_color} (Count: {count})")
            
    except Exception as e:
        print(f"Error: {e}")

get_dominant_colors('public/logo.png')
