
from PIL import Image , ImageEnhance

def getAttributes(image):
    print("Format ::",image.format,'\n')
    print("Mode ::  ",image.mode,'\n')
    print("Image Size ::",image.size,'\n')
    print("Color Pallete if exists :: ",image.palette,'\n')

def convertToPNG(image):
    filename = image.filename.split('.')
    image.save(filename[0] + '.png')

def resizeImage(image):
    sx,sy = list(map(int, input("Enter size to be made.").split(' ')))
    size = (sx,sy)
    filename = image.filename.split('.')
    image = image.resize(size)
    image.save(filename[0]+'reized'+'.'+filename[1])

def cropImage(image):
    x,y,x1,y1 = list(map(int, input("Enter Dimensions to be cropped as (x1,y1,x2,y2).").split(' ')))
    dimensions = (x,y,x1,y1)
    filename = image.filename.split('.')
    cropped_image = image.crop(dimensions)
    cropped_image.save(filename[0]+'cropped'+'.'+filename[1])

def imagePaste(img1,img2,pos):
    filename = img1.filename.split('.')
    temp_img = img1.copy()
    temp_img.paste(img2,pos,img1)
    temp_img.save(filename[0]+'pasted'+'.'+filename[1])

def rotateImage(image,angle):
    filename = image.filename.split('.')
    image_rotated = image.rotate(angle,expand=True)
    image_rotated.save(filename[0]+'rotated'+'.'+filename[1])

def imageFlip(image):
    filename = image.filename.split('.')
    image_flipped = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_flipped.save(filename[0]+'flipped'+'.'+filename[1])

def colorTransform_GRAYS(image):
    filename = image.filename.split('.')
    grayscale = image.convert("L")    
    grayscale.save(filename[0]+'grayscale'+'.'+filename[1])

def splitBands(image):
    filename = image.filename.split('.')    
    r,g,b = image.split()
    new_image = Image.merge("RGB",(g,r,b))
    new_image.save(filename[0]+'merged'+'.'+filename[1])

def addContrast(image,level):
    filename = image.filename.split('.')   
    new_image = ImageEnhance.Contrast(image)
    new_image.enhance(level).save(filename[0]+'contrasted'+'.'+filename[1])

def addSharpness(image,level):
    filename = image.filename.split('.')   
    new_image = ImageEnhance.Sharpness(image)
    new_image.enhance(level).save(filename[0]+'sharpened'+'.'+filename[1])

def enhanceColor(image,level):
    filename = image.filename.split('.')   
    new_image = ImageEnhance.Color(image)
    new_image.enhance(level).save(filename[0]+'colorEnhanced'+'.'+filename[1])

def addBrightness(image,level):
    filename = image.filename.split('.')   
    new_image = ImageEnhance.Brightness(image)
    new_image.enhance(level).save(filename[0]+'brightened'+'.'+filename[1])

if __name__ == '__main__':
    image_path1 = '1.jpg'
    image1 = Image.open(image_path1)
    image_path2 = '1.jpg'
    image2 = Image.open(image_path2)
    pos = ((200),(600))

    cropImage(image1)