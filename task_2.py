import shutil

with open('desktop.txt', 'w') as f:
    f.write(
        '[Desktop Entry]\n'
        'Name=Известные выпускники\n'
        'GenericName=ИБСТ\n'
        'Comment=da da ya\n'
        'URL=https://dep_ibst.pnzgu.ru/main/graduate\n'
        'Type=Link\n'
        'Icon=text-html\n'
        'Terminal=false\n'
    )
shutil.move('D:/институт/Питон/Lab_3/desktop.txt', 'C:/Users/ashot/Рабочий стол')