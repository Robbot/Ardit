import canvas as canvas

from canvas import Canvas
from shapes import Rectangle, Square
# # Create 3d numpy array of zeros, then replace zeros (black pixels) with yellow pixels
# data = np.zeros((5, 4, 3), dtype=np.uint8)
# data[:] = [255, 255, 0]
# print(data)
#
# # Make a red patch
# data[1:4, 1:3] = [255, 0, 0]
# # or like this one
# data[3:4, 1:4] = [45, 3, 233]
# img = Image.fromarray(data, 'RGB')
# img.save('canvas.png')

#Get canvas width and height from the user:
canvas.width = int(input("Enter canvas width: "))
canvas.height = int(input("Enter canvas height: "))

#Make dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

#Create canvas with the user data
canvas = Canvas(height=canvas.height, width=canvas.width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw (rectangle or square)? Enter quit to end program. ")
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x coordinate for upper left corner of your rectangle: "))
        rec_y = int(input("Enter y coordinate for upper left corner of your rectangle: "))
        rec_a = int(input("Enter width of your rectangle: "))
        rec_b = int(input("Enter height of your rectangle: "))
        red = int(input("How much red should the rectangle have: "))
        green = int(input("How much green should the rectangle have: "))
        blue = int(input("How much blue should the rectangle have: "))
        r1 = Rectangle(x=rec_x, y=rec_y, a=rec_a, b=rec_b, color=(red, green, blue))
        r1.draw(canvas)
    if shape_type.lower() == "square":
        rec_x = int(input("Enter x coordinate for upper left corner of your square: "))
        rec_y = int(input("Enter y coordinate for upper left corner of your square: "))
        rec_a = int(input("Enter width and height of your square: "))
        red = int(input("How much red should the square have: "))
        green = int(input("How much green should the square have: "))
        blue = int(input("How much blue should the square have: "))
        s1 = Square(x=rec_x, y=rec_y, a=rec_a, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type.lower() == "quit":
        break

canvas.make("canvas.png")


