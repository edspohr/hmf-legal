from PIL import Image
from collections import Counter

def get_dominant_colors(image_path, num_colors=5):
    try:
        image = Image.open(image_path)
        image = image.convert('RGB')
        # Resize for faster processing
        image = image.resize((150, 150))
        pixels = list(image.getdata())
        
        # Filter out white/near-white and black/near-black backrounds if necessary
        # specific to this logo which might have transparency transparent converted to black/white
        # But let's just get counts first.
        
        counts = Counter(pixels)
        common = counts.most_common(num_colors)
        
        print(f"Dominant colors in {image_path}:")
        for color, count in common:
            hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
            print(f"{hex_color} (Count: {count})")
            
    except Exception as e:
        print(f"Error: {e}")

get_dominant_colors('public/logo.png')
