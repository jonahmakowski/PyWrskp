import PySimpleGUI as sg


class MarkingCalculator:
    def __init__(self):
        self.window = None
        self.create_screen()
        self.mainloop()

    @staticmethod
    def mark_to_percent(mark, of):
        """Converts a mark to a percentage.

        Args:
            mark: The mark to convert.
            of: The maximum mark.

        Returns:
            The mark as a percentage, rounded to the nearest thousandth.
        """

        percentage = round((mark / of) * 100, 3)
        return percentage

    @staticmethod
    def calculate_grade(marks):
        """Calculates the grade of a given list of marks.

        Args:
            marks: The list of marks.
                   Each mark should be a dictionary that is structured as followed: {'grade': int, 'value': int}

        Returns:
            The overall grade as a percentage.
        """

        added_up = 0
        amount = 0

        if sum([mark['value'] for mark in marks]) != 100:
            return False

        for mark in marks:
            added_up += mark['grade'] * (100 / mark['value'])
            amount += (100 / mark['value'])

        return added_up / amount

    def create_screen(self):
        layout_tab_one = [[sg.Text('Convert your marks to percentage', expand_x=True, justification='center')],
                          [sg.Text('Input Your Mark: '), sg.InputText(key='-MARK-', expand_x=True)],
                          [sg.Text('Input The Maximum Mark: '), sg.InputText(key='-MAX-MARK-', expand_x=True)],
                          [sg.Button('Convert'), sg.Button('Exit')],
                          [sg.Text('Your result goes here: (None Yet! Press the "Convert" button to start!)', key='-Percent-Result-')]]
        layout_tab_two = [[sg.Text('Enter your grades (in percentages) on new lines in the box below:',
                                   expand_x=True, justification='center')],
                          [sg.Multiline(key='-Grades-', expand_x=True, size=(10, 5))],
                          [sg.Text('Enter the values (in percentages) of each grade below, in the same order:',
                                   expand_x=True, justification='center')],
                          [sg.Multiline(key='-Values-', expand_x=True, size=(10, 5))],
                          [sg.Button('Calculate'), sg.Button('Exit')],
                          [sg.Text('Your result goes here: (None Yet! Press the "Calculate" button to start!)', key='-Combine-Result-')]]

        main_layout = [[sg.TabGroup([[sg.Tab("Marks > Percentage", layout_tab_one),
                                      sg.Tab("Combine Marks", layout_tab_two)]])]]

        self.window = sg.Window('Marking Calculator', main_layout.copy())

    def mainloop(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or "Exit" in event:
                self.window.close()
                return

            elif event == 'Convert':
                if not (values['-MARK-'].isdigit() or values['-MAX-MARK-'].isdigit()):
                    sg.popup('Please enter your mark as a number.')
                else:
                    if int(values['-MARK-']) == 0 or int(values['-MAX-MARK-']) == 0:
                        result = 0.0
                    else:
                        result = self.mark_to_percent(float(values['-MARK-']), float(values['-MAX-MARK-']))
                    self.window['-MARK-'].update('')
                    self.window['-MAX-MARK-'].update('')
                    self.window['-Percent-Result-'].update('Your result goes here:  {}'.format(result))

            elif event == 'Calculate':
                grades = values['-Grades-'].split('\n')
                grade_values = values['-Values-'].split('\n')
                new = []
                invalid = False
                
                if (len(grades) == 1 or len(grade_values) == 1) and (grades[0] == '' or grade_values[0] == ''):
                    sg.popup('You must enter at least one mark.')
                    invalid = True
                elif len(grades) != len(grade_values):
                    sg.popup('All grades must have a value and vice versa.')
                    invalid = True
                else:
                    for index in range(len(grades)):
                        if not (grades[index].isdigit() or grades_values[index].isdigit()):
                            sg.popup('Please enter your marks and values as numbers.')
                            invalid = True
                            break
                        new.append({'grade': float(grades[index]), 'value': float(grade_values[index])})

                if not invalid:
                    result = self.calculate_grade(new)
                    if not result:
                        sg.popup('Your percentage values must add up to 100%')
                    else:
                        result = round(result, 3)
                        self.window['-Combine-Result-'].update('Your result goes here:  {}'.format(result))


c = MarkingCalculator()
