import multiprocessing
import time
from PIL import Image, ImageFilter

img_name = ['1.jpg', 

            '2.jpg',
            '3.jpg',
            '4.jpg',
            '5.jpg',
            '6.jpg',
            '7.jpg',
            '8.jpg',
            '9.jpg',
            '10.jpg']

start = time.perf_counter()
size = (1200, 1200)

def pro_image(img_nmae):
    img = Image.open(img_name)
    img =  img.filter(ImageFilter.GaussianBlur(20))
    
    img.thumbnail(size)
    img.save(processed/{img_name})
    print(f'{img_nmae} was processed.')
    
processed = []
for _ in img_name: #range (10):
     p = multiprocessing.Process(target=pro_image, args=[img_name])
     p.start()
     processed.append(p)
     
for process in processed:
    process.join()

finish = time.perf_counter()    
timer = {round(finish-start, 2)}
print(timer)