#welcome to my breakdowne' of an astro image, or ig any image but you wouldnt get any data and
#half the functions wont work, so in any case, lets begin!

print('loading required modules...')
import getpass
import cv2 as cv
import numpy as np
user = getpass.getuser()
threshold = 0.35

print('Loaded.')
print(f'Welcome to ImageX BREAKDOWN {user}!')
print('Lets begin, first type in the full path to the image, or if its in the ''same directory, just type the name!')
path = input()

def load_functions():
    global image, imageG
    image = cv.imread(path)
    imageG = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

    #cv.imshow('gray', imageG)

def star_detction():
    #this was my basis for StarRemvoal on github
    template = cv.imread('template.tif', 0)
    w, h = template.shape[::-1]

    res = cv.matchTemplate(imageG, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    mask = np.zeros_like(imageG)

    starcount = int(0)
    for pt in zip(*loc[::-1]):
        printed_stars = cv.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255, 0.5), 1)
        cv.circle(mask, (pt[0] + 4, pt[1] + 4), (w - h + 3), 255, -3)
        starcount = starcount + 1
    cv.imshow('processed', image)
    cv.imshow('mask', mask)
    print(f'Detected {starcount} stars.')

def colours():
    r = image.copy()
    r[:, :, 0] = 0
    r[:, :, 1] = 0
    cv.imshow('red', r)
    g = image.copy()
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    cv.imshow('green', g)
    b = image.copy()
    b[:, :, 1] = 0
    b[:, :, 2] = 0
    cv.imshow('blue', b)

def histogram():
    
load_functions()
colours()
star_detction()


cv.waitKey(0)