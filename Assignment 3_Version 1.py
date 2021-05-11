#!/usr/bin/env python
__author__ = "Alexander Kissiedu, Isaac Armah-Mensah & Elliot Attipoe"
__copyright__ = "Copyright 2021, The DigiCap Project"
__license__ = "GPL"
__version__ = "1.0.1"

from tkinter import *
# from tkinter.ttk import *
from tkcalendar import *
from tkinter import messagebox
# from datetime import timedelta
import datetime
from pathlib import Path
import csv

# create Tk window

root = Tk()
root.geometry("900x600")
root.title('Wage Calculator')

# Creating various frames for the controls
frame1 = Frame(root, bd=7)
frame1.pack()
frame2 = LabelFrame(root, text='Select Start Date & Time', bd=7)
frame2.pack()
frame3 = LabelFrame(root, text='Select End Date & Time', bd=7)
frame3.pack()
frame4 = LabelFrame(root, text='Total Hours', bd=7)
frame4.pack()
frame5 = LabelFrame(root, text='Earnings @ 5$/hr', bd=7)
frame5.pack()
frame6 = Frame(root, bd=7, padx=4, pady=5)
frame6.pack()

# variables declaration
wage = StringVar()
start_hr = StringVar()
start_hr.set("00")
start_min = StringVar()
start_min.set("00")
end_hr = StringVar()
end_hr.set("00")
end_min = StringVar()
end_min.set("00")
entryProject_Name = StringVar()
total_hrs_spent = StringVar()


# functions to  clear entries
def button_clear():
    entryProject_Name.delete(0, END)
    start_date.setvar("")
    end_date.setvar("")


# This function calculates Total hours worked and total Earnings
def calc_wage():
    global start_date_time
    global end_date_time
    global hours_spent
    global my_earnings
    s_date = start_date.get_date()
    user_start_time = str(str(start_date.get_date()) + " " + start_hr.get() + start_min.get())
    start_date_time = datetime.datetime.strptime(user_start_time, '%Y-%m-%d %H%M')
    e_date = end_date.get_date()
    user_end_time = str(str(end_date.get_date()) + " " + end_hr.get() + end_min.get())
    end_date_time = datetime.datetime.strptime(user_end_time, '%Y-%m-%d %H%M')
    
    print(end_date_time)
    if start_date_time > end_date_time:
        messagebox.showerror('Date Error', 'Start Date Cannot Be Later Than End Date')

    else:
        seconds_spent = (end_date_time - start_date_time).total_seconds()
        hours_spent = round(abs(seconds_spent) / 3600, 2)
        my_earnings = round(abs(hours_spent * 5), 2)
        wage.set(str("{:.2f}".format(my_earnings)))
        total_hrs_spent.set(str("{:.2f}".format(hours_spent)))


# This function creates and saves earnings to an Excel file
def save_to_excel():
    newprojectrow = [entryProject_Name.get(), start_date_time, end_date_time, hours_spent, my_earnings]
    if Path('earning.csv').is_file():
        with open("earning.csv", 'a+', newline='') as addproject:
            add_writer = csv.writer(addproject)
            # Add dictionary as wor in the csv
            add_writer.writerow(newprojectrow)
        addproject.close()
    else:
        with open("earning.csv", 'w') as createcsv:
            # Create a writer object from csv module
            new_writer = csv.writer(createcsv)
            # Add dictionary as wor in the csv
            new_writer.writerow(['Project Name', 'Start Date', 'End Date', 'Hours Spent', 'Earnings'])
            new_writer.writerow(newprojectrow)
        createcsv.close()


# Labels Used on the form to display
lbl_project_name = Label(frame1, font=('arial', 16, 'bold'), text="Name of Project:")
lbl_project_name.grid(row=0, column=0, padx=1, pady=4, )

lbl_start_date = Label(frame2, font=('arial', 16, 'bold'), text="Project Start Date: ")
lbl_start_date.grid(row=0, column=0, padx=1, pady=4)

lbl_start_time = Label(frame2, font=('arial', 16, 'bold'), text="Time (24H Clock): ", justify=LEFT)
lbl_start_time.grid(row=1, column=0, padx=1, pady=4)

lbl_end_date = Label(frame3, font=('arial', 16, 'bold'), text="Project End Date: ", justify=LEFT)
lbl_end_date.grid(row=0, column=0, padx=1, pady=4)

lbl_end_time = Label(frame3, font=('arial', 16, 'bold'), text="Time (24H Clock): ", justify=LEFT)
lbl_end_time.grid(row=1, column=0, padx=1, pady=4)

# Entry controls

entryProject_Name = Entry(frame1, font=('arial', 16, 'bold'), bd=5, width=44, justify=LEFT)
entryProject_Name.grid(row=0, column=1, sticky='w', padx=5)

start_date = DateEntry(frame2, font=('arial', 16, 'bold'), bd=5, width=44, justify=LEFT, date_pattern='dd/mm/yyyy')
start_date.grid(row=0, column=1, sticky='w', padx=5)

# Drop Down Options For Start Time
#create a list from 0 to 23 for hours
options_hours = []
for i in range (24):
    options_hours.append(str(i).zfill(2))
    
#create a list from 0 to 59 for minutes
options_mins =[]
for j in range (60):
    options_mins.append(str(j).zfill(2)) 
    
start_drop_hr = OptionMenu(frame2, start_hr, *options_hours)
start_drop_hr.grid(row=1, column=1)


start_drop_min = OptionMenu(frame2, start_min, *options_mins)
start_drop_min.grid(row=1, column=2)


end_date = DateEntry(frame3, font=('arial', 16, 'bold'), bd=5, width=44, justify=LEFT, date_pattern='dd/mm/yyyy')
end_date.grid(row=0, column=1, sticky='w', padx=5)

# Drop Down Options For  End Time

end_drop_hr = OptionMenu(frame3, end_hr, *options_hours)
end_drop_hr.grid(row=1, column=1)

end_drop_min = OptionMenu(frame3, end_min, *options_mins)
end_drop_min.grid(row=1, column=2)

# Controls to display calculated values
lbl_total_hrs = Label(frame4, font=('arial', 16, 'bold'), bd=5, width=44, justify=LEFT,
                      text='Total Hours: ')
lbl_total_hrs.grid(row=0, column=0, sticky='w', padx=1, pady=4)

lbl_my_hrs = Label(frame4, font=('arial', 16, 'bold'), bg='green', bd=5, width=44, justify=LEFT,
                   textvariable=total_hrs_spent)
lbl_my_hrs.grid(row=1, column=0, padx=1, pady=4)

lbl_wage = Label(frame5, font=('arial', 16, 'bold'), bd=5, width=44, justify=CENTER,
                 text='Earnings in Dollars: ')
lbl_wage.grid(row=0, column=0, sticky='w', padx=1, pady=4)

my_wage = Label(frame5, font=('arial', 16, 'bold'), bg='green', bd=5, width=44, justify=CENTER, textvariable=wage)
my_wage.grid(row=1, column=0, padx=1, pady=4)

# Buttons Used
#Button to clear feilds
btn_clear = Button(frame6, font=('arial', 16, 'bold'), text="Clear", justify=LEFT, command=button_clear)
btn_clear.grid(row=0, column=1)

#button to calulate earnings
cal = Button(frame6, font=('arial', 16, 'bold'), text="Calculate", justify=LEFT, command=calc_wage)
cal.grid(row=0, column=2)

#Button to save data into a csv file
save_to_excel = Button(frame6, font=('arial', 16, 'bold'), text="Save To Excel", justify=LEFT, command=save_to_excel)
save_to_excel.grid(row=0, column=3)

#Exit button to quit windows
exit_button = Button(frame6, font=('arial', 16, 'bold'), text="Exit", justify=LEFT, command=root.destroy)
exit_button.grid(row=0, column=4)

root.mainloop()


