#!/usr/bin/env python
__author__ = "Alexander Kissiedu, Isaac Armah-Mensah & Elliot Attipoe"
__copyright__ = "Copyright 2021, The DigiCap Project"
__license__ = "GPL"
__version__ = "1.0.2"

# Modules Used
from tkinter import *
from tkcalendar import DateEntry
from tkinter.ttk import *
from datetime import *
import csv
from pathlib import Path

''' Setting up the window
Start tkinter and create a window.
'''
# Setting global variable for use by any function

# Creating a Window CLass
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


        # widget can take all window
        self.pack(fill=BOTH, expand=1)
        '''
        Creating Buttons for Windows
        '''
        # create New project button, link it to clickcreateProjectButton()
        self.createProjectButton = Button(self, text="Start New Project", command=self.clickcreateProjectButton)
        #Set position of New project button using grid
        self.createProjectButton.grid(column=0, row=0, sticky=W, padx=5, pady=5)

        # create end project button, link it to clickendProjectButton()
        self.endProjectButton = Button(self, text="End Project", command=self.clickendProjectButton)
        #Set position of end project button using grid
        self.endProjectButton.grid(column=1, row=0, sticky=W, padx=5, pady=5)

        # create end project button, link it to clickcalculateButton()
        self.calculateButton = Button(self, text="Calculate Earning", command=self.clickcalculateButton)
        # Set position of end project button using grid
        self.calculateButton.grid(column=2, row=0, sticky=W, padx=5, pady=5)

        # Button for closing
        self.exit_button = Button(self, text="Exit", command=root.destroy)
        self.exit_button.grid(column=4, row=0, sticky=W, padx=5, pady=5)

        #Button for creating new project with start date
        self.createButton = Button(self, text="Create New Project", command=self.clickcreateButton)

        #Button for updating existing project with stop date
        self.endButton = Button(self, text="End", command=self.clickendButton)


        '''
        Creating Labels for Windows
        '''

        #Stop Date and Time Labels
        self.End_date = Label(self, text="End Date")
        self.End_hour = Label(self, text="End Hour")
        self.End_minute = Label(self, text="End Minute")
        self.End_Start_Label = Label(self, text="Start Date and Time")
        self.End_Project_Label = Label(self, text="Select Project to End")
        self.End_end_Label = Label(self, text="End Date and Time")
        self.endmessage = Label(self, text="Select End Date and Time")
        self.endedproject = Label(self, text="Project Already Ended")

        '''
        Creating Entries for Windows
        '''
        self.end_start = Entry(self, textvariable=end_start_value, state='readonly')
        self.end_of_End = Entry(self, textvariable=end_end_value, state='readonly')

        '''
        Creating Frames for Windows
        '''
        self.TableMargin1 = Frame(self, width=500)
        # self.TableMargin.grid(row=6, column=0, columnspan=6, sticky=NSEW)
        self.TableMargin2 = Frame(self, width=500)
        self.TableMargin3 = Frame(self, width=500)

        #Frame, label and Entry for Date and time
        self.startdateframe = Frame(self, width=500)
        self.startdateframe.grid(row=6, column=0, columnspan=5, sticky=NSEW)
        self.start_date = Label(self.startdateframe, text="Start Date")
        self.start_hour = Label(self.startdateframe, text="Start Hour")
        self.Start_minute = Label(self.startdateframe, text="Start Minute")
        self.startDateEntry = DateEntry(self.startdateframe, width=10, locale='en_US', date_pattern='mm-dd-y')
        self.start_hour_entry = Combobox(self.startdateframe, textvariable=start_hours,width=4)
        for x in range(24):
            self.start_hour_entry['values'] = tuple(list(self.start_hour_entry['values']) + [str(x).zfill(2)])
        self.start_minute_entry = Combobox(self.startdateframe, textvariable=start_minutes,width=4)
        for y in range(0, 60, 1):
            self.start_minute_entry['values'] = tuple(list(self.start_minute_entry['values']) + [str(y).zfill(2)])

        '''Project Name and Entry Frame'''
        self.projectframe = Frame(self, width=500)
        self.projectframe.grid(row=5, column=0, columnspan=5, sticky=NSEW)
        self.project_name = Label(self.projectframe, text="Project Name")
        self.project_name_entry = Entry(self.projectframe, textvariable=projectnameentry)

        '''Frame for grouping End Dates'''
        self.enddateframe = Frame(self, width=500)
        self.enddateframe.grid(row=7, column=0, columnspan=5, sticky=NSEW)
        self.end_date = Label(self.enddateframe, text="End Date")
        self.end_hour = Label(self.enddateframe, text="End Hour")
        self.end_minute = Label(self.enddateframe, text="End Minute")
        self.endDateEntry = DateEntry(self.enddateframe, width=10, locale='en_US', date_pattern='mm-dd-y')
        self.end_hour_entry = Combobox(self.enddateframe, textvariable=end_hours,width=4, state='readonly')
        for i in range(24):
            self.end_hour_entry['values'] = tuple(list(self.end_hour_entry['values']) + [str(i).zfill(2)])
        self.end_hour_entry.set(datetime.now().strftime('%H'))

        self.end_minute_entry = Combobox(self.enddateframe, textvariable=end_minutes,width=4, state='readonly')

        for j in range(0, 60, 1):
            self.end_minute_entry['values'] = tuple(list(self.end_minute_entry['values']) + [str(j).zfill(2)])
        self.end_minute_entry.set(datetime.now().strftime('%M'))

        self.end_start = Entry(self,textvariable=end_start_value,state='readonly')
        self.end_of_End = Entry(self, textvariable=end_end_value, state='readonly')

        self.end_project = Combobox(self, width=12, textvariable=endproject, state='readonly')

        '''Frame for Grouping Calculate Buttons'''
        self.calculateProject = Frame(self, width=100)
        self.pearninglabel = Label(self.calculateProject, text="Select Project")
        self.pearningCombo = Combobox(self.calculateProject, width=12, textvariable=projectearning, state='readonly')

        # Button for Calculating Total Earning
        self.calculateTotal = Frame(self, width=100)
        self.totalearning = Button(self.calculateTotal, text="Total Earning", command=self.clicktotalearningButton)

        self.clear()

     # Function menu for calculating earnings
     def clickcalculateButton(self):
        self.clear()
        self.pearningCombo = Combobox(self.calculateProject, width=12, textvariable=projectearning, state='readonly')

        # Get project from csv into combo box
        with open('earning.csv', newline='') as earning_file:
            data = csv.DictReader(earning_file)
            for row in data:
                self.pearningCombo['values'] = tuple(list(self.pearningCombo['values']) + [str(row['ProjectName'])])
        self.pearningCombo.set("Select Project")
        self.calculateProject.grid(row=2, column=0, sticky=W)
        self.pearninglabel.pack(side=LEFT, padx=5, pady=5)
        self.pearningCombo.pack(side=LEFT, padx=5, pady=5)
        self.pearningCombo.bind('<<ComboboxSelected>>', self.cal)

        self.calculateTotal.grid(row=2, column=2, sticky=W)
        # self.calButton.pack(side=LEFT, padx=5, pady=5)
        self.totalearning.pack(side=RIGHT, padx=5, pady=5)
        

        # Calculation field using treeview

        self.columns = ("ProjectName", "StartDatetime", "EndDatetime", "HoursSpent", "Earning")

        self.TableMargin1 = Frame(self, width=500)
        self.TableMargin1.grid(row=6, column=0, columnspan=6, sticky=NSEW)
        self.scrollbarx = Scrollbar(self.TableMargin1, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.TableMargin1, orient=VERTICAL)
        self.tree = Treeview(self.TableMargin1,
                             columns=("ProjectName", "StartDatetime", "EndDatetime", "HoursSpent", "Earning"),
                             height=400,
                             selectmode="extended", yscrollcommand=self.scrollbary.set,
                             xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('ProjectName', text="Project Name", anchor=CENTER)
        self.tree.heading('StartDatetime', text="Start Date", anchor=CENTER)
        self.tree.heading('EndDatetime', text="End Date", anchor=CENTER)
        self.tree.heading('HoursSpent', text="Hours Spent", anchor=CENTER)
        self.tree.heading('Earning', text="Earning", anchor=CENTER)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=YES, minwidth=0, width=150)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=120, anchor=CENTER)
        self.tree.column('#5', stretch=NO, minwidth=0, width=120, anchor=CENTER)
        self.tree.pack()
        for col in self.columns:
            self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(_col, False))
        with open('earning.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                ProjectName = row['ProjectName']
                StartDatetime = row['StartDatetime']
                EndDatetime = row['EndDatetime']
                StartDatetime_value = datetime.strptime(row['StartDatetime'], "%Y-%m-%d %H:%M:%S")
                if EndDatetime == "":
                    t = datetime.now()
                    datenow = datetime(t.year, t.month, t.day, t.hour, t.minute, t.second)
                    HoursSpent = "{:.2f}".format((datenow - StartDatetime_value).total_seconds() / 3600.0)
                    Earning = "00.00"
                    EndDatetime = "On Going"
                else:
                    EndDatetime_value = datetime.strptime(row['EndDatetime'], "%Y-%m-%d %H:%M:%S")
                    HoursSpent = round(abs(EndDatetime_value - StartDatetime_value).total_seconds() / 3600.0, 2)
                    Earning = "{:.2f}".format(HoursSpent * 5)
                self.tree.insert("", 0, values=(ProjectName, StartDatetime, EndDatetime, HoursSpent, Earning))

   # Function menu for creating new project
    def clickcreateProjectButton(self):
        self.clear()
        self.clear_text()
        self.projectframe.grid(row=5, column=0, columnspan=5, sticky=NSEW)
        self.startdateframe.grid(row=6, column=0, columnspan=5, sticky=NSEW)
        self.project_name.pack(side=LEFT, padx=5, pady=5)
        self.project_name_entry.pack(side=LEFT, padx=5, pady=5)
        self.start_date.pack(side=LEFT, padx=5, pady=5)
        self.startDateEntry.pack(side=LEFT, padx=5, pady=5)
        self.start_hour.pack(side=LEFT, padx=5, pady=5)
        self.start_hour_entry.pack(side=LEFT, padx=5, pady=5)
        self.Start_minute.pack(side=LEFT, padx=5, pady=5)
        self.start_minute_entry.pack(side=LEFT, padx=5, pady=5)
        self.createButton.grid(column=0, row=9, sticky=W, padx=5, pady=5)

    #  # Function menu for ending existing project
    def clickendProjectButton(self):
        self.clear()
        self.end_project = Combobox(self, width=12, textvariable=endproject, state='readonly')
        self.end_project.bind('<<ComboboxSelected>>', self.end)
        with open('earning.csv', newline='') as earning_file:
            data = csv.DictReader(earning_file)
            for row in data:
                self.end_project['values'] = tuple(list(self.end_project['values']) + [str(row['ProjectName'])])
        self.end_project.set("Select Project")
        self.end_project.grid(column=1, row=2, sticky=W, padx=5, pady=5)
        self.End_Project_Label.grid(column=0, row=2, sticky=W, padx=5, pady=5)
        self.endButton.grid(column=1, row=4, sticky=E, padx=5, pady=5)

    #Event Function for calculating task earning on select trigger
    def cal(self, event):
        self.clear()
        self.calculateProject.grid(row=2, column=0, sticky=W)
        self.calculateTotal.grid(row=2, column=2, sticky=W)
        self.pearninglabel.pack(side=LEFT, padx=5, pady=5)
        self.pearningCombo.pack(side=LEFT, padx=5, pady=5)
        self.totalearning.pack(side=RIGHT, padx=5, pady=5)
        self.columns = ("ProjectName", "StartDate", "EndDate", "Hours_Spent", "Earning")
        self.TableMargin2= Frame(self, width=500)
        self.TableMargin2.grid(row=6, column=0, columnspan=6, sticky=NSEW)
        self.scrollbarx = Scrollbar(self.TableMargin2, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.TableMargin2, orient=VERTICAL)
        self.tree = Treeview(self.TableMargin2,
                             columns=self.columns,
                             height=400,
                             selectmode="extended", yscrollcommand=self.scrollbary.set,
                             xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('ProjectName', text="Project Name", anchor=CENTER)
        self.tree.heading('StartDate', text="Start Date", anchor=CENTER)
        self.tree.heading('EndDate', text="End Date", anchor=CENTER)
        self.tree.heading('Hours_Spent', text="Hours Spent", anchor=CENTER)
        self.tree.heading('Earning', text="Earning", anchor=CENTER)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=YES, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=120, anchor=CENTER)
        self.tree.column('#5', stretch=NO, minwidth=0, width=120, anchor=CENTER)
        self.tree.pack()

        with open('earning.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                ProjectName = row['ProjectName']
                StartDatetime = row['StartDatetime']
                EndDatetime = row['EndDatetime']
                StartDatetime_value = datetime.strptime(row['StartDatetime'], "%Y-%m-%d %H:%M:%S")
                if row['ProjectName']== self.pearningCombo.get():
                    if EndDatetime == "":
                        t = datetime.now()
                        datenow = datetime(t.year, t.month, t.day, t.hour, t.minute, t.second)
                        HoursSpent = "{:.2f}".format((datenow - StartDatetime_value).total_seconds() / 3600.0)
                        Earning = "00.00"
                        EndDatetime = "On Going"
                    else:
                        EndDatetime_value = datetime.strptime(row['EndDatetime'], "%Y-%m-%d %H:%M:%S")
                        HoursSpent = round(abs(EndDatetime_value - StartDatetime_value).total_seconds() / 3600.0, 2)
                        Earning = "{:.2f}".format(HoursSpent * 5)
                    self.tree.insert("", 0, values=(ProjectName, StartDatetime, EndDatetime, HoursSpent, Earning))


        for col in self.columns:
            self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(_col, False))





    #Function for Calculating Total Earnings.
    def clicktotalearningButton(self):
        # Calculation field using treeview
        self.clear()
        self.columns = ("TotalProject", "StartDate", "EndDate", "TotalHours", "TotalEarning")
        self.TableMargin3 = Frame(self, width=500)
        self.TableMargin3.grid(row=6, column=0, columnspan=6, sticky=NSEW)
        self.scrollbarx = Scrollbar(self.TableMargin3, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.TableMargin3, orient=VERTICAL)
        self.tree = Treeview(self.TableMargin3,
                             columns=self.columns,
                             height=400,
                             selectmode="extended",
                             yscrollcommand=self.scrollbary.set,
                             xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('TotalProject', text="Total Projects", anchor=CENTER)
        self.tree.heading('StartDate', text="Start Date", anchor=CENTER)
        self.tree.heading('EndDate', text="End Date", anchor=CENTER)
        self.tree.heading('TotalHours', text="Total Hours", anchor=CENTER)
        self.tree.heading('TotalEarning', text="Total Earning", anchor=CENTER)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=YES, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=120, anchor=CENTER)
        self.tree.column('#5', stretch=NO, minwidth=0, width=120, anchor=CENTER)
        self.tree.pack()

        with open('earning.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            totalearning, totalproject, totalhours =0, 0, 0
            minStartDatetime=[]
            maxEndDatetime = []
            for row in reader:
                StartDatetime = row['StartDatetime']
                EndDatetime = row['EndDatetime']
                if EndDatetime == "":
                    row['EndDatetime']=row['StartDatetime']
                StartDatetime_value = datetime.strptime(row['StartDatetime'], "%Y-%m-%d %H:%M:%S")
                EndDatetime_value = datetime.strptime(row['EndDatetime'], "%Y-%m-%d %H:%M:%S")
                HoursSpent = round(abs(EndDatetime_value - StartDatetime_value).total_seconds() / 3600.0, 2)
                Earning = "{:.2f}".format(HoursSpent * 5)
                totalearning+=float(Earning)
                totalhours+=float(HoursSpent)
                totalproject+=1
                minStartDatetime.append(row['StartDatetime'])
                maxEndDatetime.append(row['EndDatetime'])
            print(StartDatetime)
            self.tree.insert("", 0, values=(totalproject, min(minStartDatetime), max(maxEndDatetime),  round(abs(totalhours),2), totalearning))

        #Enable sorting for tree view
        for col in self.columns:
            self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(_col, False))


        self.pearningCombo.set("Select Project")
        self.calculateProject.grid(row=2, column=0, sticky=W)
        self.pearninglabel.pack(side=LEFT, padx=5, pady=5)
        self.pearningCombo.pack(side=LEFT, padx=5, pady=5)
        self.calculateTotal.grid(row=2, column=2, sticky=W)
        self.totalearning.pack(side=RIGHT, padx=5, pady=5)

    #Function to allow user to sort columns in treeview.
    def treeview_sort_column(self, col, reverse):
        l = [(self.tree.set(k, col), k) for k in self.tree.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            self.tree.move(k, '', index)

        # reverse sort next time
        self.tree.heading(col, command=lambda _col=col: self.treeview_sort_column(_col, not reverse))


   #Function for setting default values for entries
    def clear_text(self):
        self.project_name_entry.delete(0,'end')
        self.startDateEntry.set_date(datetime.now())
        self.start_hour_entry.set(datetime.now().strftime('%H'))
        self.end_hour_entry.set(datetime.now().strftime('%H'))
        self.start_minute_entry.set(datetime.now().strftime('%M'))
        self.end_minute_entry.set(datetime.now().strftime('%M'))
        self.endDateEntry.set_date(datetime.now())
        self.end_hour_entry.set(datetime.now().strftime('%H'))
        self.end_minute_entry.set(datetime.now().strftime('%M'))
   
   #Function for clearing buttons, frame, combobox, entry and label from window.
    def clear(self):
        self.TableMargin1.grid_forget()
        self.TableMargin2.grid_forget()
        self.TableMargin3.grid_forget()
        self.projectframe.grid_forget()
        self.startdateframe.grid_forget()
        self.enddateframe.grid_forget()
        self.project_name.pack_forget()
        self.project_name_entry.pack_forget()
        self.start_date.pack_forget()
        self.startDateEntry.pack_forget()
        self.start_hour.pack_forget()
        self.start_hour_entry.pack_forget()
        self.end_hour_entry.pack_forget()
        self.Start_minute.pack_forget()
        self.start_minute_entry.pack_forget()
        self.end_minute_entry.pack_forget()
        self.createButton.grid_forget()
        self.endButton.grid_forget()
        self.End_Start_Label.grid_forget()
        self.end_start.grid_forget()
        self.endmessage.grid_forget()
        self.end_date.pack_forget()
        self.endDateEntry.pack_forget()
        self.end_hour.pack_forget()
        self.end_hour_entry.pack_forget()
        self.end_minute.pack_forget()
        self.end_minute_entry.pack_forget()
        self.end_project.grid_forget()
        self.endedproject.grid_forget()
        self.End_Project_Label.grid_forget()
        self.End_end_Label.grid_forget()
        self.end_of_End.grid_forget()
        self.calculateProject.grid_forget()
        self.calculateTotal.grid_forget()
        self.totalearning.pack_forget()
        self.pearningCombo.pack_forget()
        self.pearninglabel.pack_forget()

    #Function to create a new project. If csv file does not exist new one is created.
    def clickcreateButton(self):
        self.startdatetime = str(str(self.startDateEntry.get_date()) + " " + start_hours.get() + ":" + start_minutes.get())
        self.startdatetime = datetime.strptime(self.startdatetime, '%Y-%m-%d %H:%M')
        self.newprojectrow = [projectnameentry.get(), self.startdatetime,""]

        # Open file in append mode
        if Path('earning.csv').is_file():
            with open("earning.csv", 'a+', newline='') as addproject:
                # Create a writer object from csv module
                add_writer = csv.writer(addproject)
                # Add dictionary as wor in the csv
                add_writer.writerow(self.newprojectrow)
            addproject.close()
        else:
            with open("earning.csv", 'w') as createcsv:
                # Create a writer object from csv module
                new_writer = csv.writer(createcsv)
                # Add dictionary as wor in the csv
                new_writer.writerow(['ProjectName','StartDatetime','EndDatetime'])
                new_writer.writerow(self.newprojectrow)
            createcsv.close()


        self.clear()

    #Function to select end date for project. If project is already ended you cant change date.
    def clickendButton(self):
        self.enddatetime = str(str(self.endDateEntry.get_date()) + " " + end_hours.get() + ":" + end_minutes.get())
        self.enddatetime = datetime.strptime(self.enddatetime, '%Y-%m-%d %H:%M')
        # read
        with open("earning.csv") as earningfile:
            reader = csv.DictReader(earningfile)
            data = list(reader)

        # modify
        for row in data:
            if row['ProjectName'] == self.end_project.get():
                row['EndDatetime'] = self.enddatetime

        # overwrite old file
        with open("earning.csv", "w") as earningfile:
            new_writer = csv.DictWriter(earningfile,fieldnames=['ProjectName', 'StartDatetime', 'EndDatetime'])
            new_writer.writeheader()
            for row in data:
                new_writer.writerow(row)
        self.clear()


    #Event Function for filling start date and end date when a project name is seleted
    def end(self,event):
        #open csv file
        with open('earning.csv', newline='') as earning_file:
            data = csv.DictReader(earning_file)
            for row in data:
                if row['ProjectName']==self.end_project.get():
                    self.End_Start_Label.grid(column=0, row=3, sticky=W, padx=5, pady=5)
                    self.end_start.grid(column=1, row=3, sticky=W, padx=5, pady=5)
                    end_start_value.set(str(row['StartDatetime']))
                    if not row['EndDatetime']:
                        #remove entry and label from window on selecting
                        self.endedproject.grid_forget()
                        self.End_end_Label.grid_forget()
                        self.end_of_End.grid_forget()

                        #Enable Labels and entry to set project end time
                        self.enddateframe.grid(row=7, column=0, columnspan=5, sticky=NSEW)
                        self.endmessage.grid(row=6, columnspan=4)
                        self.end_date.pack(side=LEFT, padx=5, pady=5)
                        self.endDateEntry.pack(side=LEFT, padx=5, pady=5)
                        self.end_hour.pack(side=LEFT, padx=5, pady=5)
                        self.end_hour_entry.pack(side=LEFT, padx=5, pady=5)
                        self.end_minute.pack(side=LEFT, padx=5, pady=5)
                        self.end_minute_entry.pack(side=LEFT, padx=5, pady=5)
                        self.endButton.grid(column=0, row=9, sticky=W, padx=5, pady=5)

                    else:
                        #remove entry and label from window on selecting
                        self.enddateframe.grid_forget()
                        self.endmessage.grid_forget()
                        self.end_date.pack_forget()
                        self.endDateEntry.pack_forget()
                        self.end_hour.pack_forget()
                        self.end_hour_entry.pack_forget()
                        self.end_minute.pack_forget()
                        self.end_minute_entry.pack_forget()
                        self.endButton.grid_forget()
                        #Enable Labels and entry for already ended project time
                        self.End_end_Label.grid(column=0, row=4, sticky=W, padx=5, pady=5)
                        self.end_of_End.grid(column=1, row=4, sticky=W, padx=5, pady=5)
                        self.endedproject.grid(column=1, row=5, sticky=W, padx=5, pady=5)
                        end_end_value.set(str(row['EndDatetime']))



# initialize tkinter
root = Tk()
#Declare Global strings
projectnameentry, end_start_value, end_end_value = StringVar(), StringVar(), StringVar()
start_hours, end_hours, start_minutes, end_minutes = StringVar(), StringVar(), StringVar(), StringVar()
endproject, projectearning, startprojectbetween, endprojectbetween, search = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

app = Window(root)

# set window title
root.wm_title("Time Tracking Program")

#Define Windows size
width = 700
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
# Style().configure(  '.',              # every class of object
#             relief = 'flat',  # flat ridge for separator
#             borderwidth = 0,  # zero width for the border
#                 )
#Disable resizing windows
root.resizable(0, 0)


# show window
root.mainloop()
