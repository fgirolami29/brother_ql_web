from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
from brother_ql.raster import BrotherQLRaster

import qrcode

PX_WIDTH = 306
LABEL_WIDTH_MM = 29
LABEL_HEIGHT_MM = 90


qr = qrcode.make('LAMB')

qr_img = qr.get_image()
qr_img = qr_img.resize((PX_WIDTH, PX_WIDTH))  # Resize QR code to fit label



qlr = BrotherQLRaster("QL-800")
qlr.exception_on_warning = True

# Convert and print label with QR code
label_data = convert(qlr, [qr_img], f"{LABEL_WIDTH_MM}x{LABEL_HEIGHT_MM}")

send(instructions=label_data, printer_identifier="usb://0x04f9:0x209b", backend_identifier="pyusb", blocking=True)

