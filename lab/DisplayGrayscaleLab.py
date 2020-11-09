#!/usr/bin/env python3

# Author: Bryan Ramos
# Course: Theory of Operating Systems (OS)
# Instructors: Eric Freudenthal and David Pruitt
# Assignment: Lab 3 - Threaded Video Player

import cv2
import threading

VIDEOFILE = "../clip.mp4"
DELIMITER = "\0"

class ThreadQueue(): # queue implemented with python list
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(24)

    def put(self, item):
        self.empty.acquire()
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.full.release()

    def obtain(self):
        self.full.acquire()
        self.lock.acquire()
        item = self.queue.pop(0)
        self.lock.release()
        self.empty.release()
        return item


# based on extractFrames.py
def extractFrames(fileName, frameQueue):
    if fileName is None:
        raise TypeError
    if frameQueue is None:
        raise TypeError

    count = 0 #initialize frame count

    vidcap = cv2.VideoCapture(fileName)

    # read one frame
    success, image = vidcap.read()

    print(f'Reading frame {count} {success}')
    while success:
        # add frame to buffer
        frameQueue.put(image)

        success, image = vidcap.read()
        print(f'Reading frame {count} {success}')
        count += 1

    print('Finished extracting frames');
    frameQueue.put(DELIMITER)

if __name__ == "__main__":

    colorFrames = ThreadQueue()
    grayFrames = ThreadQueue()

    # three functions needed: extract frames, convert frames to grayscale,
    # and display frames at original framerate (24fps)
    extract = threading.Thread(target = extractFrames, args = (VIDEOFILE, colorFrames))

    extract.start()
