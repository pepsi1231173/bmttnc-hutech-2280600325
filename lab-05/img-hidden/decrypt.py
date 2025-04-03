import sys
from PIL import Image
def decode_image(encoded_image_path):
        img = Image.open(encoded_image_path)
        width, height = img.size
        binary_message = ""
        
        for row in range(height):
            for col in range(width):
                pixel  =list(img.getpixel((col,row)))
                
                for color_channel in range(3):
                    binary_message += format(pixel[color_channel], '08b')[-1]
                    
        message = ""
        for i in range(0, len(binary_message),8):
            char = chr (int(binary_message[i:i+8],2))
            if char == '\0':
                break
            message += char
            
        return message
        
def main():
    if len(sys.argv) !=2:
        print("Usage: python encrypt.py <image_path> <message>")
        return
    
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decode message:", decoded_message)
    
if __name__ == "__main__":
    main()
    