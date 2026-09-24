"""
Module: bubble_chart

Code to create a bubble chart showing the relationship between tuition price, acceptance rate,
and endowment size across multiple universities.

Authors: <REPLACE THIS WITH YOU AND YOUR PARTNERS FULL NAMES>
"""
import tkinter as tk

def scale_acceptance_rate(acceptance_rate, max_scaled_value):
    pass


def scale_tuition(tuition, max_scaled_value):
    pass


def scale_endowment(endowment, max_scaled_value):
    pass


def create_bubbles(canvas):
    width = int(canvas["width"])
    height = int(canvas["height"])
    
    # To Do: Write your code for this function below this line.

def get_color(value):
    return "black"

def test_get_color():
    """Runs and checks test cases for the get_color function."""
    print("Testing get_color function")

    print("Testing input: 67")
    if get_color(67) == "yellow":
        print("Passed")
    else:
        print("Failed")

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
