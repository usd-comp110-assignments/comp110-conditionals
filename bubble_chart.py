import tkinter as tk

def create_bubbles(canvas):
    pass

def get_color(value):
    pass

def test_get_color():
    pass

def main():
    """
    Main function 
    """

    root = tk.Tk()
    root.title("USD COMP110 Bubble Chart")

    canvas = tk.Canvas(root, width=500, height=500, bg="white")
    canvas.pack()

    create_bubbles(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()