import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def imhist(img):
    m, n = img.shape
    histogram = [0.0] * 256
    for i in range(m):
        for j in range(n):
            histogram[img[i, j]] += 1
    return np.array(histogram)/(m*n)


def histeq(img):
    histogram = imhist(img)
    sk = np.uint8(255 * np.cumsum(histogram))
    s1, s2 = img.shape
    Y = np.zeros_like(img)

    for i in range(s1):
        for j in range(s2):
            Y[i, j] = sk[img[i, j]]
    H = imhist(Y)
    return Y, histogram, H, sk


if __name__ == '__main__':
    print('Enter an image filename: ', end='')
    img = np.asarray(Image.open(input()))

    img = np.uint8((0.2126 * img[:, :, 0]) +
                   np.uint8(0.7152 * img[:, :, 1]) +
                   np.uint8(0.0722 * img[:, :, 2]))

    new_img, h, new_h, sk = histeq(img)

    plt.subplot(121)
    plt.imshow(img)
    plt.title('original image')
    plt.set_cmap('gray')
    # show original image
    plt.subplot(122)
    plt.imshow(new_img)
    plt.title('hist. equalized image')
    plt.set_cmap('gray')
    plt.show()

    fig = plt.figure()
    fig.add_subplot(221)
    plt.plot(h)
    plt.title('Original histogram')  # original histogram

    fig.add_subplot(222)
    plt.plot(new_h)
    plt.title('New histogram')  # hist of eqlauized image

    fig.add_subplot(223)
    plt.plot(sk)
    plt.title('Transfer function')  # transfer function

    plt.show()
