import enum

class Moves(enum.Enum):
   Up = 1
   Left = 2
   Right = 3
   Down = 4
   NoMove = 0
def output_image(filename,policy,grid):
    from PIL import Image, ImageDraw,ImageFont
    cell_size = 50
    cell_border = 2
    # Make image
    myFont = ImageFont.truetype('PTMono.ttf', 50)
    # Create a blank canvas
    img = Image.new(
        "RGBA",
        (10 * cell_size, 10 * cell_size),
        "black"
    )
    draw = ImageDraw.Draw(img)
    # Code inspiration/ Code adapted from output_image found at https://cdn.cs50.net/ai/2020/spring/lectures/0/src0/maze.py
    # The code is modified and built upon the CS50 version
    for i in range(len(policy)):
        for j in range(len(policy[0])):
            # Decide color
            fill = (237,240,252)
            if grid[i][j] == -100:
                fill = (255, 0, 0)
            if grid[i][j] == 100:
                fill = (0, 171, 28)

            # Draw cell
            draw.rectangle(
                ([(j * cell_size + cell_border, i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                fill=fill
            )
            
            from random import choice
            values = {Moves.Left:"←",Moves.Right:"→",Moves.Up: "↑",Moves.Down: "↓",Moves.NoMove:""}
            value = values[policy[i][j]]
            # Make arrow if needed
            draw.text((j*cell_size+5*cell_border, i*cell_size-5*cell_border), value, font=myFont, fill =(0, 0, 0))

    img.save(filename)

