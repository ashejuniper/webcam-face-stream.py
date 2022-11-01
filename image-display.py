import cv2
import numpy as np
import sys


def read_int():
    value_bytes = sys.stdin.buffer.read(4)
    value = int.from_bytes(value_bytes, 'little')

    return value


def read_image():
    img_size = read_int()
    height = read_int()
    width = read_int()
    img_bytes = sys.stdin.buffer.read(img_size)

    pixel_count = int(img_size / 3)

    print(pixel_count)

    flat_img = np.frombuffer(img_bytes, dtype=np.int8)
    img = np.reshape(flat_img, newshape=(3, width, height))
    # assert np.array_equal(x, deserialized_x), "Deserialization failed..."

    return img


while True:
    img = read_image()
    cv2.imshow('Image Display', img)

	# Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
