import os

folder = ''
text_file = 'Testing'

with open(folder+text_file, "r") as file:
    text_file_data = file.readlines()


photo_data = []
for line in text_file_data:
    temp = line.split('\t')
    photo = temp[2]
    name = temp[4:6]
    name = '{}, {}'.format(name[0], name[1])
    photo_data.append({'name':name, 'photo':photo})
    print('Found Data for {} photo {}'.format(name, photo))

for photo in photo_data:
    os.rename(photo['photo'], photo['name'])