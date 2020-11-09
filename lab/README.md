 # Threaded Video Player - Producer Consumer Lab

Please run the following commands first:

In order to run this lab opencv must be installed. To install opencv, please use the following commands. Do note that the ordering is important.

`
sudo zypper -n install python3-devel
sudo zypper -n install ffmpeg ffmpeg-3
sudo zypper -n install gstreamer gstreamer-devel
sudo zypper -n install python3-numpy
sudo pip install --upgrade pip
sudo pip install opencv-python
`

## Running the Lab

- Run `./DisplayGrayscaleLab.py` in the current directory (`/lab`) terminal.

## Lab Properties

- For modularization, I separated the ThreadQueue from the rest of the lab source code. The class represents a queue implemented with a Python list, handled by a thread. The class contains a get method (which dequeues item) and a put method that enqueues items.
- Implemented all features requested in the lab requirements.
