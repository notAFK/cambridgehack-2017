import sys
import os

SOURCE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SOURCE + os.path.pardir)
DATA = os.path.join(ROOT, 'data')

IMAGES = os.path.join(DATA, 'images')
UPLOAD = os.path.join(DATA, 'upload')
AUDIO = os.path.join(DATA, 'audio')

WEBSITE = os.path.join(ROOT, 'website/public/')
