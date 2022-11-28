
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image,ImageEnhance
from param_config import train_img_size

def enh(img):
    img_ = cv2.GaussianBlur(cv2.imread(img), (3,3), 1,1)
    converterC = ImageEnhance.Contrast(Image.fromarray(img_))
    img_ = converterC.enhance(1)
    converterS = ImageEnhance.Sharpness(img_)
    img_ = converterS.enhance(8)
    return img_

def resized(imp):
    im = Image.open(imp)
    im = im.convert('RGB')
    im = im.resize(train_img_size)
    return im
def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def font_selection(fonts_path):

    font_list = glob.glob(fonts_path +"*")
    return (random.choices(font_list,k=len(font_list)))

def get_text():
    text = "mode creates two blocks of text. First block is the instruction of recepies, second is a paragraph with the description"
    return text

def crop_fixed(img):
    w,h = img.size

    return [np.array(img)[0:int(h/2),0:w],np.array(img)[int(h/2)+15:int(h),0:w]]

def get_random_crop(image, crop_height, crop_width):

    max_x = int((image.size[1] - crop_width)/3)
    max_y = int((image.size[0] - crop_height)/3)

    x = np.random.randint(0, max_x)
    y = np.random.randint(0, max_y)

    crop = np.array(image)[y: y + crop_height, x: x + crop_width]

    return crop
