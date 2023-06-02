import os
import json


class Schedule:
    def __init__(self, show=True, name='schedule_data.txt'):
        try:
            self.pyWrskp = os.environ["PYWRKSP"]
        except KeyError:
            self.pyWrskp = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                                      '\nPlease enter the pwd for the pyWrskp repo not including the '
                                                      '"home" section')
        self.name = self.pyWrskp + '/docs/txt-files/' + name
        if show:
            info = input('What would you like to do? \noptions: print, create, or empty (p/c/e)')
            if info == 'c':
                self.create_built_in()
            elif info == 'p':
                self.show()
            elif info == 'e':
                self.empty()
    
    def create_built_in(self):
        end_time = input('What is the end time for this event?\nplease use 24hr clock')
        name = input('What is the name of this event?')
        start_time = input('What is the start time for this event?\nplease use 24hr clock')
        all_events = self.read()
        if all_events is None:
            all_events = []
        all_events.append({'start_time': start_time, 'end_time': end_time, 'name': name})
        with open(self.name, 'w') as outfile:
            json.dump(all_events, outfile)

    def create(self, start_time, end_time, name):
        all_events = self.read()
        if all_events is None:
            all_events = []
        all_events.append({'start_time': start_time, 'end_time': end_time, 'name': name})
        with open(self.name, 'w') as outfile:
            json.dump(all_events, outfile)
    
    def read(self):
        try:
            with open(self.name) as json_file:
                info = json.load(json_file)
            info = sorted(info, key=lambda i: i['start_time'], reverse=True)
        except FileNotFoundError:
            info = None
        return info
    
    def show(self):
        events = self.read()
        if events is None or events == []:
            print('you have no events saved')
        else:
            print('Name, start, end')
            for item in events:
                print('{}, {}, {}'.format(item['name'], item['start_time'], item['end_time']))

    def empty(self):
        with open(self.name, 'w') as outfile:
            json.dump([], outfile)


if __name__ == "__main__":
    s = Schedule()
