# image_encryption.py

from PIL import Image
import random

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Convert to a list of tuples (R, G, B)
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    
    # Encrypt pixels by swapping and applying XOR operation
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y][x]
            
            # XOR operation on each color channel using key
            r_enc = r ^ key
            g_enc = g ^ key
            b_enc = b ^ key
            
            # Swap pixels randomly (optional)
            if random.choice([True, False]):
                r_enc, g_enc, b_enc = g_enc, b_enc, r_enc
            
            pixels[y][x] = (r_enc, g_enc, b_enc)
    
    # Create a new image and put the encrypted pixels
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_pixels = [pixel for row in pixels for pixel in row]
    encrypted_img.putdata(encrypted_pixels)
    
    # Save the encrypted image
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Convert to a list of tuples (R, G, B)
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    
    # Decrypt pixels by reversing the XOR operation
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y][x]
            
            # Reverse XOR operation using the same key
            r_dec = r ^ key
            g_dec = g ^ key
            b_dec = b ^ key
            
            pixels[y][x] = (r_dec, g_dec, b_dec)
    
    # Create a new image and put the decrypted pixels
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_pixels = [pixel for row in pixels for pixel in row]
    decrypted_img.putdata(decrypted_pixels)
    
    # Save the decrypted image
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    # File paths
    input_image = "sample.jpg"
    encrypted_image = "encrypted_image.png"
    decrypted_image = "decrypted_image.png"

    # Encryption key
    key = 150  # You can change this key to any integer value

    # Encrypt the image
    encrypt_image(input_image, encrypted_image, key)

    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image, key)
