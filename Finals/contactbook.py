from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox
from datetime import datetime
import pytz

#set colors/ color value reference
color1 = "#ffffff"
color2 = "#000000"
color3 = "#EEEEDF"
color4 = "#47473C"
color5 = "#8B8B22"

#set font/font size
font1 = ("Roboto", 20, "bold")
font2 = ("Ivy", 10, "bold")
font3 = ("Ivy", 8, "bold")
font4 = ("Century Gothic", 12, "bold")

#login window layout
window_login = Tk()

height = 230
width = 450
x = (window_login.winfo_screenwidth()//2)-(width//2)
y = (window_login.winfo_screenheight()//2)-(height//2)

window_login.title('Login - Contact Information Book')
window_login.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window_login.resizable(width = False, height = False)
window_login.config(background = color3)

#----------------------------------------------------------------------------------------------------#
#to function log in button 

def log_in():
    username = ent_user.get() #getting the username input
    password = ent_code.get() #getting the password input
    
    #condition 
    #required / username and password set
    if username == 'admin_ira' and password == 'trojan123': 
        
        #login window close
        window_login.withdraw()
        
        #main window layout 
        #open main window
        main = Toplevel(window_login)
        height = 450
        width = 1060
        x = (main.winfo_screenwidth()//2)-(width//2)
        y = (main.winfo_screenheight()//2)-(height//2)
        
        main.title("Con-Info-Book")
        main.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        main.resizable(width = False, height = False)
        
        #main icon
        icon_main = PhotoImage(file='icon_main.png')
        main.iconphoto(False, icon_main)
        
        #timezone
        timezone = pytz.timezone('Asia/Manila')
        
        #--------------------------------------------------------------------------------------------#
        #functions of buttons in left frame
        
        #to insert a contact
        def to_insert():
            #get all input data
            Firstname = ent_fname.get()
            Lastname = ent_lname.get()
            Birthdate = ent_dob.get()
            Age = ent_age.get()
            Gender = box_gender.get()
            Phone = ent_phone.get()
            Email = ent_email.get()
            City = ent_city.get()
            Province = ent_prov.get()
            Country = ent_count.get()
            
            data = [Firstname, Lastname, Birthdate, Age, Gender, Phone, Email, City, Province, Country]
            
            #condition if the user has input in all fields
            if Firstname == '' or Lastname == '' or Birthdate == '' or Age == '' or Gender == '' or Phone == '' or Email == '' or City == '' or Province == '' or Country == '':
                messagebox.showwarning('Oops', 'Some fields are not filled yet. Please fill all fields.')
            
            else:
                add(data)
                messagebox.showinfo('Success', 'Data has been successfully inserted.')
                
                ent_fname.delete(0, 'end')
                ent_lname.delete(0, 'end')
                ent_dob.delete(0, 'end')
                ent_age.delete(0, 'end')
                box_gender.delete(0, 'end')
                ent_phone.delete(0, 'end')
                ent_email.delete(0, 'end')
                ent_city.delete(0, 'end')
                ent_prov.delete(0, 'end')
                ent_count.delete(0, 'end')
                
                show()
        
        #to update a contact
        def to_update():
            try:
                #select a contact
                tree_data = tree.focus()
                tree_dictionary = tree.item(tree_data)
                tree_list = tree_dictionary['values']
                
                #from the tree list set it into strings
                Firstname = str(tree_list[0])
                Lastname = str(tree_list[1])
                Birthdate = str(tree_list[2])
                Age = str(tree_list[3])
                Gender = str(tree_list[4])
                Phone = str(tree_list[5])
                Email = str(tree_list[6])
                City = str(tree_list[7])
                Province = str(tree_list[8])
                Country = str(tree_list[9])
                
                #strings insert in the entries
                ent_fname.insert(0, Firstname)
                ent_lname.insert(0, Lastname)
                ent_dob.insert(0, Birthdate)
                ent_age.insert(0,Age)
                box_gender.insert(0, Gender)
                ent_phone.insert(0, Phone)
                ent_email.insert(0, Email)
                ent_city.insert(0, City)
                ent_prov.insert(0, Province)
                ent_count.insert(0, Country)
                
                #to save updated data
                def confirm():
                    new_fname = ent_fname.get()
                    new_lname = ent_lname.get()
                    new_dob = ent_dob.get()
                    new_age = ent_age.get()
                    new_gender = box_gender.get()
                    new_phone = ent_phone.get()
                    new_email = ent_email.get()
                    new_city = ent_city.get()
                    new_prov = ent_prov.get()
                    new_count = ent_count.get()
                    
                    data = [new_phone, new_fname, new_lname, new_dob, new_age, new_gender, new_phone, new_email, new_city, new_prov, new_count]
                    
                    update(data)
                    
                    messagebox.showinfo('Success', 'Data has been updated successfully.')
                    
                    ent_fname.delete(0, 'end')
                    ent_lname.delete(0, 'end')
                    ent_dob.delete(0, 'end')
                    ent_age.delete(0, 'end')
                    box_gender.delete(0, 'end')
                    ent_phone.delete(0, 'end')
                    ent_email.delete(0, 'end')
                    ent_city.delete(0, 'end')
                    ent_prov.delete(0, 'end')
                    ent_count.delete(0, 'end')
                    
                    for widget in table_frame.winfo_children():
                        widget.destroy()
                        
                    btn_confirm.destroy()
                    
                    show()

                btn_confirm = Button(left_frame, text = "Confirm", width = 40,  height = 1, bg = color5, fg = color1, font = font2, command = confirm)
                btn_confirm.place(x = 10, y = 327)
                
            except IndexError:
                messagebox.showerror('Error', 'Select the contact from the table.')
        
        #to delete a contact
        def to_delete():
            try:
                #select 
                tree_data = tree.focus()
                tree_dictionary = tree.item(tree_data)
                tree_list = tree_dictionary['values']
                tree_phone = str(tree_list[2])
                
                remove(tree_phone)
                
                messagebox.showinfo('Success', 'Data has been deleted.')
                
                for widget in table_frame.winfo_children():
                    widget.destroy()
                
                show()
                
            except IndexError:
                messagebox.showerror('Error', 'Select the contact from the table.')  

        #to search a contact
        def to_search():
            phone = ent_search.get()
            
            data = search(phone)
            
            def delete_command():
                tree.delete(*tree.get_children())
                
            delete_command()
            
            for item in data:
                tree.insert('', 'end', values = item)
                
            ent_search.delete(0, 'end')
        
        #to reset inputs in Entries/combobox/spinbox
        def reset():
            for widget in left_frame.winfo_children():
                if isinstance(widget, Entry):
                    widget.delete(0, 'end')
                if isinstance(widget, ttk.Combobox):
                    widget.delete(0, 'end')
                if isinstance(widget, Spinbox):
                    widget.delete(0, 'end')
        
        #to logout
        def logout():
            window_login.deiconify()
            main.destroy()
        
        
        #--------------------------------------------------------------------------------------------#
        
        #Frames/structure
        
        #upper frame for inside title and image
        upper_frame = Frame(main, width = 1060, height = 50, bg = color2)
        upper_frame.grid(row = 0, column = 0, padx = 0, pady = 2)
        
        #main image
        title_image = PhotoImage(file = 'icon_main.png')
        l_title_image = Label(upper_frame, image = title_image, bg = color2)
        l_title_image.place(x = 340, y = 6)

        #main title
        title = Label(upper_frame, text = "Contact Information Book", height = 1, font = font1, bg = color2, fg = color1)
        title.place(x = 390, y = 5)
        
        
        #left frame 
        left_frame = Frame(main, width = 350, height = 700, bg = color3)
        left_frame.grid(row = 1, column = 1, padx = 0, pady = 2)
        left_frame.place(x = 0, y = 50)
        
        #left frame widgets
        #for contact's firstname
        lab_fname = Label(left_frame, text = "First Name:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_fname.place(x = 20, y = 20)
        ent_fname = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_fname.place(x = 100, y = 20)
        
        #for contact's lastname
        lab_lname = Label(left_frame, text = "Last Name:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_lname.place(x = 20, y = 50)
        ent_lname = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_lname.place(x = 100, y = 50)
        
        #for contact's date of birth
        lab_dob = Label(left_frame, text = "Birthdate:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_dob.place(x = 20, y = 80)
        ent_dob = Entry(left_frame, width = 20, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_dob.insert(0, 'mm/dd/yyyy')
        ent_dob.place(x = 100, y = 80)
        
        #for contact's age
        lab_age = Label(left_frame, text = "Age:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_age.place(x = 230, y = 80)
        ent_age = Spinbox(left_frame, width = 5, from_ = 1, to = 100)
        ent_age.place(x = 270, y = 80)
        
        #for contact's gender
        lab_gender = Label(left_frame, text = "Gender:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_gender.place(x = 20, y = 110)
        box_gender = ttk.Combobox(left_frame, width = 32)
        box_gender['values'] = ['', 'Female', 'Male', 'Prefer Not to Say']
        box_gender.place(x = 100, y = 110)
        
        #for contact's phone number
        lab_phone = Label(left_frame, text = "Phone No. :", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_phone.place(x = 20, y = 140)
        ent_phone = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_phone.place(x = 100, y = 140)
        
        #for contact's email add
        lab_email = Label(left_frame, text = "Email:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_email.place(x = 20, y = 170)
        ent_email = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_email.place(x = 100, y = 170)
        
        #for contact's address (city)
        lab_city = Label(left_frame, text = "City:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_city.place(x = 20, y = 200)
        ent_city = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_city.place(x = 100, y = 200)

        #for contact's address (province)
        lab_prov = Label(left_frame, text = "Province:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_prov.place(x = 20, y = 230)
        ent_prov = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_prov.place(x = 100, y = 230)

        #for contact's address (vountry)
        lab_count = Label(left_frame, text = "Country:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_count.place(x = 20, y = 260)
        ent_count = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_count.place(x = 100, y = 260)

        #left frame buttons
        #insert
        btn_insert = Button(left_frame, text = "Insert", width = 10,  height = 1, bg = color4, fg = color1, font = font2, command = to_insert)
        btn_insert.place(x = 10, y = 295)

        #update/edit
        btn_edit = Button(left_frame, text = "Edit", width = 10,  height = 1, bg = color4, fg = color1, font = font2, command = to_update)
        btn_edit.place(x = 130, y = 295)

        #delete
        btn_delete = Button(left_frame, text = "Delete", width = 10,  height = 1, bg = color4, fg = color1, font = font2, command = to_delete) 
        btn_delete.place(x = 250, y = 295)
        
        #reset
        btn_reset = Button(left_frame, text = "Reset", width = 10,  height = 1, bg = color4, fg = color1, font = font2, command = reset)
        btn_reset.place(x = 180, y = 360)

        #logout
        btn_logout = Button(left_frame, text = "Log Out", width = 10,  height = 1, bg = color4, fg = color1, font = font2, command = logout)
        btn_logout.place(x = 70, y = 360)
        
        
        #right frame
        right_frame = Frame(main, width = 710, height = 50, bg = color3)
        right_frame.grid(row = 1, column = 2, padx = 0, pady = 2)
        right_frame.place(x = 350, y = 50)
        
        #right frame widget
        #date&time
        lab_date = Label(right_frame, width = 25, height = 1, font = font4, bg = color3, fg = color4, anchor = NW)
        lab_date.place(x = 20, y = 10)

        lab_time = Label(right_frame, width = 25, height = 1, font = font4, bg = color3, fg = color4, anchor = NW)
        lab_time.place(x = 140, y = 10)
        
        #funtion for current date and clock
        def date_clock():
            raw_time = datetime.now(timezone)
            date_now = raw_time.strftime("%d/%m/%Y")
            time_now = raw_time.strftime("%H:%M:%S %p")
            lab_date.config(text = date_now)
            lab_time.config(text = time_now)
            lab_time.after(1000, date_clock)

        date_clock()
        
        # searchbar and button
        ent_search = Entry(right_frame, width = 35, justify = "left", font = font3, highlightthickness = 1, relief = "solid")
        ent_search.place(x = 270, y = 13)
        btn_search = Button(right_frame, text = "Search", width = 10, height = 1, bg = color4, fg = color1, font = font3, command = to_search)
        btn_search.place(x = 500, y = 10)
        
        #frame for table
        table_frame= Frame(main, width = 710, height = 350, bg = color1)
        table_frame.grid(row = 1, column = 2, padx = 0, pady = 2)
        table_frame.place(x = 350, y = 100)
        
        #to show all data / view
        def show():
            global tree
            #header of the table
            listheader = ['Firstname', 'Lastname', 'Birthdate', 'Age', 'Gender', 'Phone No.', 'Email', 'City', 'Province', 'Country']
            
            list = view()
            
            tree = ttk.Treeview(table_frame, columns = listheader, show = "headings")
            tree.place(x = 0, y = 0, width = 690, height = 330)
            
            #style
            style = ttk.Style()
            
            #some style for table
            style.theme_use("default")
                
            #scrollbar
            scrollbary = ttk.Scrollbar(table_frame, orient = VERTICAL)
            scrollbarx = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
            
            scrollbary.configure(command = tree.yview)
            scrollbary.place(x = 690, y = 0, width=22, height=330)
            
            scrollbarx.configure(command = tree.xview)
            scrollbarx.place(x = 2, y = 330, width=710, height=22)
            
            tree.configure(yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set, selectmode=BROWSE)
            
            #tree head
            tree.heading(0, text = 'FIRSTNAME', anchor = NW)
            tree.heading(1, text = 'LASTNAME', anchor = NW)
            tree.heading(2, text = 'BIRTHDAY', anchor = NW)
            tree.heading(3, text = 'AGE', anchor = NW)
            tree.heading(4, text = 'GENDER', anchor = NW)
            tree.heading(5, text = 'PHONE NO.', anchor = NW)
            tree.heading(6, text = 'EMAIL', anchor = NW)
            tree.heading(7, text = 'CITY', anchor = NW)
            tree.heading(8, text = 'PROVINCE', anchor = NW)
            tree.heading(9, text = 'COUNTRY', anchor = NW)
            
            #tree columns
            tree.column(0, width = 120, anchor = NW)
            tree.column(1, width = 120, anchor = NW)
            tree.column(2, width = 100, anchor = NW)
            tree.column(3, width = 60, anchor = NW)
            tree.column(4, width = 120, anchor = NW)
            tree.column(5, width = 120, anchor = NW)
            tree.column(6, width = 150, anchor = NW)
            tree.column(7, width = 120, anchor = NW)
            tree.column(8, width = 120, anchor = NW)
            tree.column(9, width = 120, anchor = NW)
            
            for item in list:
                tree.insert ('', 'end', values = item)
            
        show()
        
        #view button
        btn_view = Button(right_frame, text = "View", width = 10,  height = 1, bg = color4, fg = color1, font = font3, command = show)
        btn_view.place(x = 590, y = 10)
        
        #to run the main window
        main.mainloop()
        
    
    #error if not met the required username and password
    elif username != 'admin_ira' and password != 'trojan123':
        messagebox.showerror('Invalid!', "Invalid Entry.")
        
    elif username != 'admin_ira':
        messagebox.showerror('Invalid!', "Invalid Username.")
    
    elif password != 'trojan123':
        messagebox.showerror('Invalid!', "Invalid Password.")

#------------------------------------------------------------------------#
#set contents/widgets of the log in window

#login image
img = PhotoImage(file = 'img_login.png')
lab_img = Label(window_login, image = img, bg = color3)
lab_img.place(x = 20, y = 60)

#login title frame
log_frame = Frame(window_login, width = 250, height = 200, bg = color3)
log_frame.place(x = 160, y = 25)

#login title/heading
lab_heading = Label(log_frame, text = 'Log In', font = font4, fg = color2, bg = color3)
lab_heading.place(x = 100, y = 5)

#log in username label and entry
lab_user = Label(log_frame, text = 'Username:', font = font2, fg = color2, bg = color3)
lab_user.place(x = 10, y = 50)
ent_user = Entry(log_frame, width = 20, fg = color2, bg = color3, font = font2)
ent_user.place(x = 90, y = 50)

#log in password label and entry
lab_code = Label(log_frame, text = 'Password:', font = font2, fg = color2, bg = color3)
lab_code.place(x = 10, y = 90)
ent_code = Entry(log_frame, width = 20, fg = color2, bg = color3, font = font2, show = "*")
ent_code.place(x = 90, y = 90)

#button of login
btn_login = Button(log_frame, text = "Log In", width = 10,  height = 1, bg = color4, fg = color1, font = font3, command = log_in)
btn_login.place(x = 90, y = 130)

#run login window 
window_login.mainloop()