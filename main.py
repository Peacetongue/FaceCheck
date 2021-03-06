import face_recognition as fr
import PIL.Image
from PIL import Image
import PIL.ImageDraw
import urllib.request as ur

url = str(input())
ur.urlretrieve(url,"HUI.jpg")

img = fr.load_image_file("HUI.jpg")
#print(img)
face_loc = fr.face_locations(img)
no_of_faces = len(face_loc)
#print(no_of_faces)
pil_image = PIL.Image.fromarray(img)
for face_location in face_loc:
    top,right,bottom,left = face_location
    draw_shape = PIL.ImageDraw.Draw(pil_image)
    draw_shape.rectangle([left, top, right, bottom],outline="green")
pil_image.save("faces.jpg")
rimg = Image.open("faces.jpg")
rimg.show()