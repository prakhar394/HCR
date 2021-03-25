from PIL import Image
img = Image.open(r"/Users/prakhardungarwal/Downloads/IMAGE PROJECT/Code Files/source_main/image/TestImage.jpg")
top=0
bottom=300
for i in range(0,5):
    area = (20, top,3000, bottom)
    cropped_img = img.crop(area)
    top=top+150
    bottom=bottom+150
    im1 = cropped_img.save(r"/Users/prakhardungarwal/Downloads/IMAGE PROJECT/Code Files/source_main/image/"+str(i)+".jpg")