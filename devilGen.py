from barcode import EAN13
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# Make sure to pass the number as string
number = '5901234123457'
  
# Now, let's create an object of EAN13
# class and pass the number
my_code = EAN13(number)
  
# Our barcode is ready. Let's save it.
my_code.save("new_code")

  
drawing = svg2rlg("new_code.svg")
renderPM.drawToFile(drawing, "my.png", fmt="PNG")

