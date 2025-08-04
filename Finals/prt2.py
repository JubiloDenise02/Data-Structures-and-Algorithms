from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import pytz

#set colors/ color value reference
color1 = "#ffffff"
color2 = "#000000"
color3 = "#EEEEDF"
color4 = "#47473C"

#set font/font size
font1 = ("Roboto", 20, "bold")
font2 = ("Ivy", 10, "bold")
font3 = ("Ivy", 8, "bold")
font4 = ("Century Gothic", 12, "bold")
font5 = ("Century Gothic", 8, "bold")


window_login = Tk()

height = 230
width = 450
x = (window_login.winfo_screenwidth()//2)-(width//2)
y = (window_login.winfo_screenheight()//2)-(height//2)

window_login.title('Login - Contact Information Book')
window_login.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window_login.resizable(width = False, height = False)
window_login.config(background = color3)

def sign_in():
    username = ent_user.get()
    password = ent_code.get()
    
    if username == 'admin' and password == '1234':
        
        screen = Toplevel(window_login)
        
        height = 450
        width = 1060
        x = (screen.winfo_screenwidth()//2)-(width//2)
        y = (screen.winfo_screenheight()//2)-(height//2)
        
        #create window
        screen.title("Con-Info-Book")
        screen.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        screen.resizable(width = False, height = False)
        
        #timezone
        timezone = pytz.timezone('Asia/Manila')
        
        #window icon
        icon = PhotoImage(file='icon.png')
        screen.iconphoto(False, icon)


        #functions/codings

        #to insert a data
        def to_insert():
            Firstname = ent_fname.get()
            Lastname = ent_lname.get()
            Age = ent_age.get()
            Birthdate = ent_dob.get()
            Gender = box_gender.get()
            Phone = ent_phone.get()
            Email = ent_email.get()
            City = ent_city.get()
            Province = ent_prov.get()
            Country = ent_count.get()
            
            data = [Firstname, Lastname, Age, Birthdate, Gender, Phone, Email, City, Province, Country]
            
            if Firstname == '' or Lastname == '' or Birthdate == '' or Gender == '' or Phone == '' or Email == '' or City == '' or Province == '' or Country == '':
                messagebox.showwarning('Oops', 'Some fields are not filled yet. Please fill all fields.')
            
            else:
                add(data)
                messagebox.showinfo('Success', 'Data has been successfully inserted.')
                
                ent_fname.delete(0, 'end')
                ent_lname.delete(0, 'end')
                ent_age.delete(0, 'end')
                ent_dob.delete(0, 'end')
                box_gender.delete(0, 'end')
                ent_phone.delete(0, 'end')
                ent_email.delete(0, 'end')
                ent_city.delete(0, 'end')
                ent_prov.delete(0, 'end')
                ent_count.delete(0, 'end')
                
                show()
            
        #to update 
        def to_update():
            try:
                tree_data = tree.focus()
                tree_dictionary = tree.item(tree_data)
                tree_list = tree_dictionary['values']
                
                Firstname = str(tree_list[0])
                Lastname = str(tree_list[1])
                Age = str(tree_list[2])
                Birthdate = str(tree_list[3])
                Gender = str(tree_list[4])
                Phone = str(tree_list[5])
                Email = str(tree_list[6])
                City = str(tree_list[7])
                Province = str(tree_list[8])
                Country = str(tree_list[9])
                
                ent_fname.insert(0, Firstname)
                ent_lname.insert(0, Lastname)
                ent_age.insert(0,Age)
                ent_dob.insert(0, Birthdate)
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
                    new_age = ent_age.get()
                    new_dob = ent_dob.get()
                    new_gender = box_gender.get()
                    new_phone = ent_phone.get()
                    new_email = ent_email.get()
                    new_city = ent_city.get()
                    new_prov = ent_prov.get()
                    new_count = ent_count.get()
                    
                    data = [new_phone, new_fname, new_lname, new_age, new_dob, new_gender, new_phone, new_email, new_city, new_prov, new_count]
                    
                    update(data)
                    
                    messagebox.showinfo('Success', 'Data has been updated successfully.')
                    
                    ent_fname.delete(0, 'end')
                    ent_lname.delete(0, 'end')
                    ent_age.delete(0, 'end')
                    ent_dob.delete(0, 'end')
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
                    
                btn_confirm = Button(right_frame, text = "Confirm", width = 10,  height = 1, bg = color4, fg = color1, font = font3, command = confirm)
                btn_confirm.place(x = 20, y = 10)
                
            except IndexError:
                messagebox.showerror('Error', 'Select the contact from the table.')
        
        #to remove
        def to_delete():
            try:
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

        #to search
        def to_search():
            phone = ent_search.get()
            
            data = search(phone)
            
            def delete_command():
                tree.delete(*tree.get_children())
                
            delete_command()
            
            for item in data:
                tree.insert('', 'end', values = item)
                
            ent_search.delete(0, 'end')    


        #Frames/structure
        upper_frame = Frame(screen, width = 1060, height = 50, bg = color2)
        upper_frame.grid(row = 0, column = 0, padx = 0, pady = 2)

        left_frame = Frame(screen, width = 350, height = 700, bg = color3)
        left_frame.grid(row = 1, column = 1, padx = 0, pady = 2)
        left_frame.place(x = 0, y = 50)

        right_frame = Frame(screen, width = 710, height = 50, bg = color3)
        right_frame.grid(row = 1, column = 2, padx = 0, pady = 2)
        right_frame.place(x = 350, y = 50)

        table_frame= Frame(screen, width = 710, height = 350, bg = color1)
        table_frame.grid(row = 1, column = 2, padx = 0, pady = 2)
        table_frame.place(x = 350, y = 100)
        
        #upperframe widgets
        title_image = PhotoImage(file = 'icon.png')
        l_title_image = Label(upper_frame, image = title_image, bg = color2)
        l_title_image.place(x = 340, y = 6)

        title = Label(upper_frame, text = "Contact Information Book", height = 1, font = font1, bg = color2, fg = color1)
        title.place(x = 390, y = 5)

        #lowerframe widgets/design
        #date&time
        lab_date = Label(left_frame, width = 25, height = 1, font = font4, bg = color3, fg = color4, anchor = NW)
        lab_date.place(x = 60, y = 370)

        lab_time = Label(left_frame, width = 25, height = 1, font = font4, bg = color3, fg = color4, anchor = NW)
        lab_time.place(x = 190, y = 370)

        def clock():
            raw_time = datetime.now(timezone)
            date_now = raw_time.strftime("%d/%m/%Y")
            time_now = raw_time.strftime("%H:%M:%S %p")
            lab_date.config(text = date_now)
            lab_time.config(text = time_now)
            lab_time.after(1000, clock)

        clock()

        #to show all data / view
        def show():
            global tree
            #header of the table
            listheader = ['Firstname', 'Lastname', 'Age', 'Birthdate', 'Gender', 'Phone No.', 'Email', 'City', 'Province', 'Country']
            
            list = view()
            
            tree = ttk.Treeview(table_frame, columns = listheader, show = "headings", )
            tree.place(x = 0, y = 0, width = 690, height = 330)
            
            #table heading style
            style = ttk.Style()
            style.configure("Treeview.Heading", font = font5 )
            
            #scrollbar
            scrollbary = ttk.Scrollbar(table_frame, orient = VERTICAL)
            scrollbarx = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
            
            scrollbary.configure(command = tree.yview)
            scrollbary.place(x = 690, y = 2, width=22, height=350)
            
            scrollbarx.configure(command = tree.xview)
            scrollbarx.place(x = 2, y = 330, width=710, height=22)
            
            tree.configure(yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set, selectmode='extended')
            
            #tree head
            tree.heading(0, text = 'FIRSTNAME', anchor = NW)
            tree.heading(1, text = 'LASTNAME', anchor = NW)
            tree.heading(2, text = 'AGE', anchor = NW)
            tree.heading(3, text = 'BIRTHDATE', anchor = NW)
            tree.heading(4, text = 'GENDER', anchor = NW)
            tree.heading(5, text = 'PHONE NO.', anchor = NW)
            tree.heading(6, text = 'EMAIL', anchor = NW)
            tree.heading(7, text = 'CITY', anchor = NW)
            tree.heading(8, text = 'PROVINCE', anchor = NW)
            tree.heading(9, text = 'COUNTRY', anchor = NW)
            
            #tree columns
            tree.column(0, width = 120, anchor = NW)
            tree.column(1, width = 120, anchor = NW)
            tree.column(2, width = 60, anchor = NW)
            tree.column(3, width = 100, anchor = NW)
            tree.column(4, width = 100, anchor = NW)
            tree.column(5, width = 120, anchor = NW)
            tree.column(6, width = 150, anchor = NW)
            tree.column(7, width = 120, anchor = NW)
            tree.column(8, width = 120, anchor = NW)
            tree.column(2, width = 120, anchor = NW)
            
            for item in list:
                tree.insert ('', 'end', values = item)
            
        show()

        #labels/entry/optionbox
        lab_fname = Label(left_frame, text = "First Name:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_fname.place(x = 20, y = 20)
        ent_fname = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_fname.place(x = 100, y = 20)

        lab_lname = Label(left_frame, text = "Last Name:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_lname.place(x = 20, y = 50)
        ent_lname = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_lname.place(x = 100, y = 50)

        lab_age = Label(left_frame, text = "Age:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_age.place(x = 20, y = 80)
        ent_age = Spinbox(left_frame, width = 5, from_ = 1, to = 100)
        ent_age.place(x = 100, y = 80)

        lab_dob = Label(left_frame, text = "Birthdate:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_dob.place(x = 150, y = 80)
        ent_dob = DateEntry(left_frame, selectmode = 'day')
        ent_dob.place(x = 220, y = 80)

        lab_gender = Label(left_frame, text = "Gender:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_gender.place(x = 20, y = 110)
        box_gender = ttk.Combobox(left_frame, width = 32)
        box_gender['values'] = ['', 'Female', 'Male', 'Prefer Not to Say']
        box_gender.place(x = 100, y = 110)

        lab_phone = Label(left_frame, text = "Phone No. :", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_phone.place(x = 20, y = 140)
        ent_phone = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_phone.place(x = 100, y = 140)

        lab_email = Label(left_frame, text = "Email:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_email.place(x = 20, y = 170)
        ent_email = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_email.place(x = 100, y = 170)

        lab_city = Label(left_frame, text = "City:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_city.place(x = 20, y = 200)
        ent_city = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_city.place(x = 100, y = 200)

        lab_prov = Label(left_frame, text = "Province:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_prov.place(x = 20, y = 230)
        ent_prov = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_prov.place(x = 100, y = 230)

        lab_count = Label(left_frame, text = "Country:", width = 25, height = 1, font = font2, bg = color3, anchor = NW)
        lab_count.place(x = 20, y = 260)
        ent_count = Entry(left_frame, width = 35, justify = "left", highlightthickness = 1, relief = "solid", bg = color3)
        ent_count.place(x = 100, y = 260)

        #buttons
        btn_insert = Button(left_frame, text = "Insert", width = 10,  height = 1, bg = color4, fg = color1, font = font2, command = to_insert)
        btn_insert.place(x = 10, y = 290)

        btn_update = Button(left_frame, text = "Update", width = 10,  height = 1, bg = color4, fg = color1, font = font2, command = to_update)
        btn_update.place(x = 130, y = 290)

        btn_delete = Button(left_frame, text = "Delete", width = 10,  height = 1, bg = color4, fg = color1, font = font2, command = to_delete) 
        btn_delete.place(x = 250, y = 290)

        btn_exit = Button(left_frame, text = "Exit", width = 10,  height = 1, bg = color4, fg = color1, font = font2, command = screen.destroy)
        btn_exit.place(x = 10, y = 330)

        btn_about = Button(left_frame, text = "About", width = 10,  height = 1, bg = color4, fg = color1, font = font2) # command = about)
        btn_about.place(x = 130, y = 330)

        # btn_reset = Button(left_frame, text = "Reset", width = 10,  height = 1, bg = color4, fg = color1, font = font2, command = to_reset)
        # btn_reset.place(x = 250, y = 330)

        btn_search = Button(right_frame, text = "Search", width = 10, height = 1, bg = color4, fg = color1, font = font3, command = to_search)
        btn_search.place(x = 500, y = 10)
        ent_search = Entry(right_frame, width = 35, justify = "left", font = font3, highlightthickness = 1, relief = "solid")
        ent_search.place(x = 270, y = 13)

        btn_view = Button(right_frame, text = "View", width = 10,  height = 1, bg = color4, fg = color1, font = font3, command = show)
        btn_view.place(x = 590, y = 10)

        #run
        screen.mainloop()

    elif username != 'admin' and password != '1234':
        messagebox.showerror('Invalid!', "Invalid Entry.")
    
    elif password != '123':
        messagebox.showerror('Invalid!', "Invalid Password.")


img = PhotoImage(file = 'img1.png')
lab_img = Label(window_login, image = img, bg = color3)
lab_img.place(x = 20, y = 60)

log_frame = Frame(window_login, width = 250, height = 200, bg = color3)
log_frame.place(x = 160, y = 25)

lab_heading = Label(log_frame, text = 'Log In', font = font4, fg = color2, bg = color3)
lab_heading.place(x = 100, y = 5)

ent_user = Entry(log_frame, width = 30, fg = color2, bg = color3, font = font2)
ent_user.place(x = 30, y = 50)
ent_user.insert(0,'Username' )

ent_code = Entry(log_frame, width = 30, fg = color2, bg = color3, font = font2)
ent_code.place(x = 30, y = 90)
ent_code.insert(0,'Password' )

btn_login = Button(log_frame, text = "Log In", width = 10,  height = 1, bg = color4, fg = color1, font = font3, command = sign_in)
btn_login.place(x = 90, y = 130)

window_login.mainloop()