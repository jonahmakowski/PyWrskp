# Import the fractions module to handle fractions
from fractions import Fraction

# Import the tkinter module to create a GUI
import tkinter as tk

def main():
  # Create the main window
  window = tk.Tk()
  window.title("Scientific Calculator")
  
  # Create the display
  display = tk.Entry(window, font=("Calibri", 20), justify="right", width=25)
  display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
  
  # Define the functions for the calculator buttons
  def button_click(number):
    # Insert the number into the display
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))
  
  def button_clear():
    # Clear the display
    display.delete(0, tk.END)
  
  def button_equal():
    # Calculate the result and display it
    try:
      result = eval(display.get())
      display.delete(0, tk.END)
      display.insert(0, str(result))
    except:
      display.delete(0, tk.END)
      display.insert(0, "Error")
  
  def button_fraction():
    # Convert the display value to a fraction and display it
    try:
      result = Fraction(display.get())
      display.delete(0, tk.END)
      display.insert(0, str(result))
    except:
      display.delete(0, tk.END)
      display.insert(0, "Error")
  
  # Create the buttons
  button_1 = tk.Button(window, text="1", font=("Calibri", 20), width=5, height=2, command=lambda: button_click(1))
  button_2 = tk.Button(window, text="2", font=("Calibri", 20), width=5, height=2, command=lambda: button_click(2))
  button_3 = tk.Button(window, text="3", font=("Calibri", 20), width=5, height=2, command=lambda: button_click(3))
  button_4 = tk.Button(window, text="4", font=("Calibri", 20), width=5, height=2, command=lambda: button_click(4))
  button_5 = tk.Button(window, text="5", font=("Calibri", 20), width=5, height=2, command=lambda: button_click(5))
  button_6 = tk.Button(window, text="6", font=("Calibri", 20), width=5, height=2, command=lambda: button_click(6))
  button_7 = tk.Button(window, text="7", font=("Calibri", 20), width=5, height=2, command=lambda: button_click(7))
  button_8 = tk.Button(window, text="8", font=("Calibri", 20), width=5, height=2, command=lambda: button_click(8))

  button_9 = tk.Button(window, text="9", font=("Calibri", 20), width=5, height=2, command=lambda: button_click(9))
  button_0 = tk.Button(window, text="0", font=("Calibri", 20), width=5, height=2, command=lambda: button_click(0))
  button_add = tk.Button(window, text="+", font=("Calibri", 20), width=5, height=2, command=lambda: button_click("+"))
  button_subtract = tk.Button(window, text="-", font=("Calibri", 20), width=5, height=2, command=lambda: button_click("-"))
  button_multiply = tk.Button(window, text="*", font=("Calibri", 20), width=5, height=2, command=lambda: button_click("*"))
  button_divide = tk.Button(window, text="/", font=("Calibri", 20), width=5, height=2, command=lambda: button_click("/"))
  button_exponent = tk.Button(window, text="^", font=("Calibri", 20), width=5, height=2, command=lambda: button_click("^"))
  button_clear = tk.Button(window, text="AC", font=("Calibri", 20), width=5, height=2, command=button_clear)
  button_equal = tk.Button(window, text="=", font=("Calibri", 20), width=5, height=2, command=button_equal)
  button_fraction = tk.Button(window, text="Fraction", font=("Calibri", 10), width=11, height=2, command=button_fraction)
  
  # Place the buttons in the grid
  button_7.grid(row=1, column=0, padx=5, pady=5)
  button_8.grid(row=1, column=1, padx=5, pady=5)
  button_9.grid(row=1, column=2, padx=5, pady=5)
  button_add.grid(row=1, column=3, padx=5, pady=5)
  button_4.grid(row=2, column=0, padx=5, pady=5)
  button_5.grid(row=2, column=1, padx=5, pady=5)
  button_6.grid(row=2, column=2, padx=5, pady=5)
  button_subtract.grid(row=2, column=3, padx=5, pady=5)
  button_1.grid(row=3, column=0, padx=5, pady=5)
  button_2.grid(row=3, column=1, padx=5, pady=5)
  button_3.grid(row=3, column=2, padx=5, pady=5)
  button_multiply.grid(row=3, column=3, padx=5, pady=5)
  button_0.grid(row=4, column=0, padx=5, pady=5)
  button_clear.grid(row=4, column=1, padx=5, pady=5)
  button_equal.grid(row=4, column=2, padx=5, pady=5)
  button_divide.grid(row=4, column=3, padx=5, pady=5)
  button_fraction.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
  button_exponent.grid(row=5, column=2, padx=5, pady=5)
  
  # Run the main loop
  window.mainloop()

# Call the main function
if __name__ == "__main__":
  main()

