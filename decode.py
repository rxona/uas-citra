import cv2
from imwatermark import WatermarkDecoder

bgr = cv2.imread('cover-stegano.png')
message = open('message.txt').read()

decoder = WatermarkDecoder('bytes', len(message) * 8)
watermark = decoder.decode(bgr, 'dwtDctSvd')
print(watermark.decode('utf-8'))