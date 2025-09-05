import turtle as t

# open file for writing (append mode so you can see each run)
log_file = open("pattern.txt", "w")

# recursive function to draw a fractal edge
def draw_edge(length, depth):
    if depth == 0:
        log_file.write(f"Forward {length}\n")
        t.forward(length)
    else:
        seg = length / 3
        draw_edge(seg, depth - 1)
        t.right(60)
        log_file.write("Right 60\n")
        draw_edge(seg, depth - 1)
        t.left(120)
        log_file.write("Left 120\n")
        draw_edge(seg, depth - 1)
        t.right(60)
        log_file.write("Right 60\n")
        draw_edge(seg, depth - 1)

# function to draw polygon with given parameters
def draw_polygon(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        t.right(angle)
        log_file.write(f"Right {angle}\n")

def main():
    # user inputs
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # log the inputs
    log_file.write(f"Polygon with {sides} sides, length {length}, depth {depth}\n")

    # setup turtle
    scr = t.Screen()
    scr.setup(900, 900)
    t.speed(0)
    t.hideturtle()

    # move turtle so the figure is centered
    t.penup()
    t.goto(-length // 2, -length // 4)
    t.pendown()

    # draw fractal polygon
    draw_polygon(sides, length, depth)

    # close log file
    log_file.close()

    t.done()

if __name__ == "__main__":
    main()
