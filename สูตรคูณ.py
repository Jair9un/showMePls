import tkinter


def show_multiply():
    number = int(number_input.get())

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)


window = tkinter.Tk()
window.title('แม่สูตรคูณ')
window.minsize(width=400, height=600)

title_label = tkinter.Label(master=window, text='สูตรคูณแม่')
title_label.pack

number_input = tkinter.Entry(master=window)
number_input.pack

output_button = tkinter.Button( master=window, text='ได้แก่')
output_button.pack

output_label = tkinter.Label(master=window)
output_label.pack

window.mainloop()