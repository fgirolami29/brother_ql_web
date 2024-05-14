from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
from brother_ql.raster import BrotherQLRaster
from PIL import Image
import qrcode

# Define label size in dots (for QL-800 printer)
LABEL_WIDTH_DOTS = 306
LABEL_HEIGHT_DOTS = 991

# Generate QR code
qr = qrcode.make('ARCOR2')
qr_img = qr.get_image()

# Calculate scaling factor for the QR code
scale_factor = min(LABEL_WIDTH_DOTS / qr_img.width, LABEL_HEIGHT_DOTS / qr_img.height)
qr_img = qr_img.resize((int(qr_img.width * scale_factor), int(qr_img.height * scale_factor)))

# Calculate the position to paste the QR code in the center of the label
pos_x = (LABEL_WIDTH_DOTS - qr_img.width) // 2
pos_y = (LABEL_HEIGHT_DOTS - qr_img.height) // 2

# Create blank label image
label_img = Image.new('RGB', (LABEL_WIDTH_DOTS, LABEL_HEIGHT_DOTS), color='white')

# Paste QR code onto label image
label_img.paste(qr_img, (pos_x, pos_y))

# Initialize Brother QL raster
qlr = BrotherQLRaster("QL-800")
qlr.exception_on_warning = True

# Convert and print label with QR code
label_data = convert(qlr, [label_img], "29x90")
send(instructions=label_data, printer_identifier="usb://0x04f9:0x209b", backend_identifier="pyusb", blocking=True)
