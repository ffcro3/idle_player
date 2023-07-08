from screenCapture import setInterval, capture
import threading

x = 1
fps = 1/20
screen = setInterval(fps, capture)
t = threading.Timer(10, setInterval.cancel)
t.start()
