from canvas_creator import Canvas, FileSharer
from shapes import Rectange, Square


# I am getting canvas parameters as height and width
canvas_height = int(input('Enter the canvas height: '))
canvas_width = int(input('Enter the canvas width: '))

# I am creating dictionary with two colors (keys)  in it(black, white)
all_colors = {'black' : (0, 0, 0),'white' : (255, 255, 255)}

# Asking the user to choose the color
canvas_color = input('Enter the color (black or white): ')

# Creating the canvas where we will draw
your_canvas = Canvas(canvas_height, canvas_width, all_colors[canvas_color])


while True:
    shape_type = input("What do you like to draw (rectangle or square)? if you want to quit type quit: ")
    # Creating rectangle
    if shape_type.lower() == 'rectangle':
        rec_x = int(input('Type x for rectangle: '))
        rec_y = int(input('Type y for rectangle: '))
        rec_height = int(input('Type height of the  rectange: '))
        rec_width = int(input('Type width of the rectangle: '))
        red = int(input('How much red do you want? '))
        blue = int(input('How much blue do you want? '))
        green =int(input('How much green do you want? '))
        your_rectange = Rectange(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        your_rectange.draw(your_canvas)
    # Creating rectangle
    if shape_type.lower() == 'square':
        s_x = int(input('Type the x for the square: '))
        s_y = int(input('Type the y for the square: '))
        s_side = int(input('Type the side of the square: '))
        red = int(input('How much red do you want? '))
        blue = int(input('How much blue do you want? '))
        green = int(input('How much green do you want? '))
        your_square = Square(x=s_x, y=s_y, side=s_side, color=(red, green, blue))
        your_square.draw(your_canvas)

    # if 'quit' it typed then break
    if shape_type == 'quit':
        break


your_canvas.make('canvas.png')
file_share = FileSharer(filepath='canvas.png')
print(file_share.share())
