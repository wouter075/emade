from PIL import Image
from PIL.Image import Resampling
from fpdf import FPDF

pdf = FPDF('P', 'pt', 'A4')
pdf.add_page()

image_list = ["sum.png", "solve_c.png", "solve_x.png"]

margin = 10
factor = 2

for image in image_list:
    img = Image.open(image)

    width = img.width
    height = img.height

    img = img.resize((int(width / factor), int(height / factor)), Resampling.LANCZOS)
    img.save(image)

    # display width and height
    print("The height of the image is: ", height)
    # print("The width of the image is: ", width)

    pdf.image(image, x=None, y=margin, w=0, h=0, type='', link='')
    margin += int(height / factor) + margin


pdf.output('output.pdf', 'F')
