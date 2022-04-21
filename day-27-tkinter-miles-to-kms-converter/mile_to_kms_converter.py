from tkinter import *

def convert_to_kms():
    data_in_miles = miles_input.get()
    data_in_kms = float(data_in_miles) * 1.60934
    kms_result_label.config(text=f'{data_in_kms}')

window = Tk()
window.title("Miles to Kms Converter")
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

kms_result_label = Label(text=0)
kms_result_label.grid(column=1, row=1)

kms_label = Label(text="Km(s)")
kms_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert_to_kms)
calculate_button.grid(column=1, row=2)

window.mainloop()