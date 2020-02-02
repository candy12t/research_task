import numpy as np
from PIL import Image
import subprocess
import cv2
import os


class Video:
    def __init__(self, mp4, rgb, r, g, b):
        self.mp4 = mp4
        self.rgb = rgb
        self.r = r
        self.g = g
        self.b = b
        self.n = 0

    def read_video(self):
        self.video = cv2.VideoCapture(self.mp4)
        if not self.video.isOpened():
            return

    def save_img(self, dirc, x=None, y=None):
        img = self.img.copy()
        if x is None and y is None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            img[:, :, (x, y)] = 0
        img = Image.fromarray(img)
        img.save('{}/{}.{}'.format(dirc, self.n, 'png'))

    def write(self):
        while True:
            ret, frame = self.video.read()
            if ret:
                self.img = np.array(frame)

                self.save_img(self.rgb)
                self.save_img(self.r, 1, 2)
                self.save_img(self.g, 0, 2)
                self.save_img(self.b, 0, 1)

                self.n += 1
            else:
                return

    def open_dir(self):
        input_dir = os.path.dirname(os.path.abspath(self.mp4))
        cmd = 'open {} {} {} {} {}'.format(input_dir, self.rgb, self.r, self.g, self.b)
        subprocess.call(cmd.split())
