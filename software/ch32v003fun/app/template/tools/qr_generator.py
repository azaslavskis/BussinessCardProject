import requests
import typer
from PIL import Image
from io import BytesIO

app = typer.Typer()

def image_to_c_array(image_bytes, output_c_file_path, x, y):
    """
    Converts an image byte stream into a C array and writes it to a .c file.

    Args:
    - image_bytes: Bytes of the image.
    - output_c_file_path: Path to the output .c file where the C array will be written.
    - x: Width to resize the image.
    - y: Height to resize the image.
    """
    # Open the image from the byte stream and convert to 1-bit mode ('1' is black and white)
    im = Image.open(BytesIO(image_bytes)).convert('1')
    im_resize = im.resize((x, y))
    
    # Create a buffer to hold the resized image in PPM format (raw pixel data)
    buf = BytesIO()
    im_resize.save(buf, 'ppm')
    byte_im = buf.getvalue()

    # Skip the PPM header (which includes width, height, and metadata)
    header_len = len(f"P6\n{x} {y}\n255\n")  # PPM format header length
    image_data = byte_im[header_len:]

    # Generate C-style byte array
    c_array = "const unsigned char qr_code_one[] = {\n  "
    byte_array = [f"0x{byte:02x}" for byte in image_data]
    
    # Format the output to have 12 bytes per line
    for i in range(0, len(byte_array), 12):
        c_array += ", ".join(byte_array[i:i+12]) + ",\n  "
    
    # Remove trailing comma and newline, and close the array
    c_array = c_array.rstrip(",\n  ") + "\n};\n"

    # Length of the byte array
    array_len = len(image_data)
    c_array += f"const unsigned int qr_code_one_len = {array_len};\n"

    # Write the C array to the specified output .c file
    with open(output_c_file_path, 'w') as output_file:
        output_file.write(c_array)

    print(f"Generated C array written to {output_c_file_path}")

@app.command()
def generate_qr_code(qr_code_string: str):
    url = f"https://api.qrserver.com/v1/create-qr-code/?size=48x48&data={qr_code_string}"
    print(f"Requesting QR code from: {url}")
    r = requests.get(url, allow_redirects=True)
    
    if r.status_code == 200:
        image_to_c_array(r.content, "qr.h", 48, 48)
    else:
        print(f"Failed to retrieve QR code. Status code: {r.status_code}")

if __name__ == "__main__":
    app()
