import tkinter as tk

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.resizable(False, False)

        # Add to the power of and square root buttons.
        self.buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
            ("^", 5, 0),  # Power of button.
            ("√", 5, 1)   # Square root button.
        ]

        self.display = tk.Entry(self.root, width=30)
        self.display.grid(row=0, columnspan=4)

        for text, row, col in self.buttons:
            button = tk.Button(self.root, text=text, width=5, height=2)
            button.grid(row=row, column=col)
            button["command"] = lambda x=text: self.click(x)

        self.operators = ["+", "-", "*", "/", "^", "√"]

    def click(self, text):
        if text in self.operators:
            self.operator = text
            self.first_number = float(self.display.get())
            self.display.delete(0, tk.END)
        elif text == "=":
            second_number = float(self.display.get())
            result = self.__calculate__(self.first_number, second_number, self.operator)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        else:
            self.display.insert(tk.END, text)

    def __calculate__(self, first_number, second_number, operator):
        if operator == "+":
            return first_number + second_number
        elif operator == "-":
            return first_number - second_number
        elif operator == "*":
            return first_number * second_number
        elif operator == "/":
            return first_number / second_number
        elif operator == "^":
            return first_number ** second_number
        elif operator == "√":
            return second_number ** 0.5

if __name__ == "__main__":
    calculator = Calculator()
    calculator.root.mainloop()