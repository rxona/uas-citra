import cv2
from imwatermark import WatermarkEncoder

bgr = cv2.imread('cover.png')
message = open('message.txt').read()

encoder = WatermarkEncoder()
encoder.set_watermark('bytes', message.encode('utf-8'))
bgr_encoded = encoder.encode(bgr, 'dwtDctSvd')

cv2.imwrite('cover-stegano.png', bgr_encoded)