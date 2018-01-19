import numpy as np
from PIL import Image
from numpy.fft import fft, ifft

def filterImage(srcImage):

    srcIm = Image.open(srcImage)
    srcArray = np.fromstring(srcIm.tobytes(), dtype=np.int8)

    result = fft(srcArray)
    result = np.where(np.absolute(result) < 9e4, 0, result)

    result = ifft(result)
    result = np.int8(np.real(result))

    im = Image.frombytes(srcIm.mode, srcIm.size, result)

    im.show()

filterImage('./image/input.jpg')