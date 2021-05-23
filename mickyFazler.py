import tkinter as tk
from tkinter import ttk,messagebox,font,filedialog,colorchooser
import os

root=tk.Tk()
# root=tk.Toplevel()      #tk.Tk() both are same. But when we use on image tk.Tk() gives problem       like "image pyimage107 doesn't exist" and "Image does not exist"  if you use this it did not give problem.........By the way it's completly own explore
root.geometry("1200x800")
root.title("Untitled        Micky Text Editor")
root.wm_iconbitmap('icon.ico')




############################################## Start Main Menu  ###################################################
main_Menu=tk.Menu()

#All functions

#File Icons
new_icon=tk.PhotoImage(file="myicons/new.png")
open_icon=tk.PhotoImage(file="myicons/open.png")
save_icon=tk.PhotoImage(file="myicons/save.png")
save_as_icon=tk.PhotoImage(file="myicons/save_as.png")
exit_icon=tk.PhotoImage(file="myicons/exit.png")

# file
file=tk.Menu(main_Menu,tearoff=False)       # tearoff=False will remove the extra --- line



# Edit Icons
copy_icon=tk.PhotoImage(file="myicons/copy.png")
paste_icon=tk.PhotoImage(file="myicons/paste.png")
cut_icon=tk.PhotoImage(file="myicons/cut.png")
clear_icon=tk.PhotoImage(file="myicons/clear_all.png")
find_icon=tk.PhotoImage(file="myicons/find.png")


# Edit
edit=tk.Menu(main_Menu,tearoff=False)

# View Icon
tool_bar_icon=tk.PhotoImage(file="myicons/tool_bar.png")
status_bar_icon=tk.PhotoImage(file="myicons/status_bar.png")

# View
view=tk.Menu(main_Menu,tearoff=False)


#Color Theme Icon
light_default_icon = tk.PhotoImage(file='myicons/light_default.png')
light_plus_icon = tk.PhotoImage(file='myicons/light_plus.png')
dark_icon = tk.PhotoImage(file='myicons/dark.png')
red_icon = tk.PhotoImage(file='myicons/red.png')
monokai_icon = tk.PhotoImage(file='myicons/monokai.png')
night_blue_icon = tk.PhotoImage(file='myicons/night_blue.png')

#Color Theme
color_Theme=tk.Menu(main_Menu,tearoff=False)


def aboutFunc():
    messagebox.showinfo("Author","Fazle Rabbi \n https://web.facebook.com/mickyfazler")


# Cascase
main_Menu.add_cascade(label ="File",menu=file)
main_Menu.add_cascade(label ="Edit",menu=edit)
main_Menu.add_cascade(label ="View",menu=view)
main_Menu.add_cascade(label ="Color Theme",menu=color_Theme)
main_Menu.add_cascade(label ="About",command=aboutFunc)



# -------------------------------------&&&&&&&& End Main Menu &&&&&&&&&&& ----------------------------------



############################################## Start Toolbar ###################################################
# print(tk.font.families())       #Tkinter by default give this all font
# print(type(tk.font.families()))     #Tuple

tool_bar=ttk.Label(root)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# Creating Font Box  *******

font_tuple=tk.font.families()   #It's an tuple
selected_font_family=tk.StringVar()

font_box=ttk.Combobox(tool_bar,width=30,textvariable=selected_font_family,state="readonly")
font_box['values']=font_tuple
font_box.current(font_tuple.index("Arial"))  #Setting default        #In Current we need to give Arial font index.But we don't know Arial index.So we find Arial index like that "font_tuple.index('Arial')" .If you know Arial index then you can directly give Arial index instead of it       
font_box.grid(row=0,column=0,padx=5)

#End Font box***

# Size Box
selected_font_size=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=selected_font_size,state="readonly")
font_size['values']=tuple(range(8,81,4))
font_size.current(1)         #Here 4 is index not font_size
font_size.grid(row=0,column=1,padx=5)
# End Size Box

# Button Start********************

## bold button 
bold_icon = tk.PhotoImage(file='myicons/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

## italic button 
italic_icon = tk.PhotoImage(file='myicons/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

## underline button 
underline_icon = tk.PhotoImage(file='myicons/underline.png')
underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column=4, padx=5)

## font color button 
font_color_icon = tk.PhotoImage(file='myicons/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5,padx=5)


## align left 
align_left_icon = tk.PhotoImage(file='myicons/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

## align center 
align_center_icon = tk.PhotoImage(file='myicons/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

## align right 
align_right_icon = tk.PhotoImage(file='myicons/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

# Button End********************


# -------------------------------------&&&&&&&& End Toolbar &&&&&&&&&&& ----------------------------------

############################################## Start Text Editor  ###################################################

text_editor=tk.Text()
text_editor.config(wrap="word",relief=tk.FLAT)        #wrap="words" means if we go new line then it goes with the whole word . 
text_editor.focus_set()         #Giving focus sothat when we open the code it automatically focus on text editor

# Scroll Bar
scroll_bar=tk.Scrollbar(root)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Change font       If you write this function at the top then it will give problem like "can't invoke "bind" command: application has been destroyed"  Because at the top we can't access any variable and we don't know does font box,font size exist or not . 

current_font_family=selected_font_family.get()         #Specially use it on change_bold_Func to change font family and size
current_font_size=selected_font_size.get()

def change_font_family_Func(root):      #Here you also can give event=None like lower
    global current_font_family
    current_font_family=selected_font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size_Func(event=None):       #Here you also can give root like upper
    global current_font_size
    current_font_size=selected_font_size.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font_family_Func)             #When we will change font this "change_font_Func" function will call
font_size.bind("<<ComboboxSelected>>", change_font_size_Func)             #When we will change font this "change_font_Func" function will call






# Buttons functionality
# print(tk.font.Font(font=text_editor["font"]).actual())        # It gives lots of thing about our text.Like it bold or normal (weight)  and here it's a dictionary did you notice


# Bold button functionality        Turn normal<>bold
def change_bold_Func():
    text_property=tk.font.Font(font=text_editor["font"])
    if text_property.actual()["weight"] == "normal":             #IF normal then turn into bold         weight means bold or normal
        # print("if",current_font_size,current_font_family)
        text_editor.configure(font=(current_font_family,current_font_size,"bold"))
    else:             
        # print("Else")                                  #IF bold then turn into normal
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
    # print("Bold button")
bold_btn.configure(command=change_bold_Func)





# Bold button functionality        Turn roman<(normal)>italic
def change_italic_Func():
    text_property=tk.font.Font(font=text_editor["font"])
    if text_property.actual()["slant"] == "roman":             #IF roman(normal) then turn into italic         slant means italic or roman
        # print("if",current_font_size,current_font_family)
        text_editor.configure(font=(current_font_family,current_font_size,"italic"))
    else:             
        # print("Else")                                  #IF bold then turn into normal
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
    # print("Bold button")
italic_btn.configure(command=change_italic_Func)





# Bold button functionality        Turn roman<(normal)>italic
def change_underline_Func():
    text_property=tk.font.Font(font=text_editor["font"])
    if text_property.actual()["underline"] == 0:             #IF roman(normal) then turn into italic         slant means italic or roman
        # print("if",current_font_size,current_font_family)
        text_editor.configure(font=(current_font_family,current_font_size,"underline"))
    else:             
        # print("Else")                                  #IF bold then turn into normal
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
    # print("Bold button")
underline_btn.configure(command=change_underline_Func)



#Change font color
def change_font_color():
    font_color_var=tk.colorchooser.askcolor()
    # print(font_color_var)     It give RGB value and hexadecimanl value and it's a tuple.It's is easy to work with hexadecimal value.hexadecimal value is on 1 index 
    text_editor.configure(fg=font_color_var[1])

font_color_btn.configure(command=change_font_color)




# Align functionality 

# Align LEft
def align_left_Func():
    text_content=text_editor.get(1.0,"end")             #First storing text into variable
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)                  #Deleting text Editor text 
    text_editor.insert(tk.INSERT,text_content,"left")       # Inserting the same text into text Editor
align_left_btn.configure(command=align_left_Func)



# Align Right
def align_right_Func():
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"right")
align_right_btn.configure(command=align_right_Func)


# Align Center
def align_center_Func():
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"center")
align_center_btn.configure(command=align_center_Func)



# Align functionality  End

# -------------------------------------&&&&&&&& End Text Editor &&&&&&&&&&& ----------------------------------

############################################## Start  Status Bar  or Bottom bar###################################################

status_bar=ttk.Label(root,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)



existing_file_character=""



does_text_changed=False


# print("change1",len(text_editor.get(1.0,tk.END)))
def change_status_bar_Func(event=None):     #"event=None" sothat we can give keyboard shortcut
    global does_text_changed,existing_file_character            # Remember global must be the first 
    
    # print("change2",len(text_editor.get(1.0,tk.END)))
    current_file_character=text_editor.get(1.0,"end").replace(" ","").replace("\n","").replace("\t","")
    # print(current_file_character,"cur")
    # print("Current")
    # print("chan1 ",existing_file_character)
    # print("chan2 ",current_file_character)
    changed=not (existing_file_character == current_file_character)
    # print(changed)
    # changed=! (existing_file_character == current_file_character)         # It did not work.I want to invert True<>False.I don't know why Mind it
    # print(changed)
    
    if ((does_existing_file_opened and changed) or ( does_existing_file_opened==False and len(current_file_character) != 0)):  #If you open any existing file then our text editor value change according our new opened file text.So if you Try to close the opened file without changing our exit function will told us to save.
        # print("Changed text baby")
        # print(does_text_changed)
        does_text_changed=True
        len_words=len(text_editor.get(1.0,"end").split())
        # print(len_words)
        characters=len(text_editor.get(1.0,"end").replace(" ","").replace("\n","").replace("\t",""))
        status_bar.config(text=f"Characters: {characters} len_words: {len_words}")
        # print("main")
   
        if (does_existing_file_opened==False and len(current_file_character) != 0):
            # print(current_file_character,"if")
            root.title("*Untitled        Micky Text Editor")
        elif (does_existing_file_opened and changed):
            root.title("*"+os.path.basename(url)+"          Micky Text Editor")


        # print("End Calling")

    else:                     
        if(does_existing_file_opened==False and len(current_file_character) == 0):
            does_text_changed=False     #Just think If we write something on blank then does_text_changed=True  and then if we remove all the text and close the window it will ask for save because does_text_changed=True so we make it False
            # print(current_file_character,"else")
            # print("else")
            root.title("Untitled        Micky Text Editor")
        # elif (text_editor.edit_modified() and does_existing_file_opened and not changed):
        elif (does_existing_file_opened and not changed):
            root.title(os.path.basename(url)+"          Micky Text Editor")


    text_editor.edit_modified(False)        # If we did not do it then this function or if we edit this function will run only none time
    # if (text_editor.edit_modified() and does_existing_file_opened==False and current_file_character != 0):
    #     print(current_file_character,"if")
    #     root.title("*Untitled        Micky Text Editor")
    # else:
    #     print(current_file_character,"else")
    #     root.title("Untitled        Micky Text Editor")


text_editor.bind("<<Modified>>",change_status_bar_Func)         #If we modify anything on textEditor then this function will run

# -------------------------------------&&&&&&&& End  Status Bar &&&&&&&&&&& ----------------------------------

############################################## Start Main menu functionality  ###################################################   Our all command here because we did not use object oriented programming.So if you call any function it must be defined before call

#new Variable
url=""

#new file functionality
def new_file_Func(event=None):          # It will just remove all the text from textEditor
    global url,does_existing_file_opened,does_text_changed,existing_file_character
    
    # copied from on_closing_Func()
    current_file_character=text_editor.get(1.0,"end").replace(" ","").replace("\n","").replace("\t","")         # copied from upper
    changed=not (existing_file_character == current_file_character)
    if (len(current_file_character) != 0 and does_existing_file_opened==False ) or (does_existing_file_opened and changed):
        a=messagebox.askyesnocancel("Quit", "Do you want to save")          
        if a==True:     # if click yes
            does_saved=save_file_Func()
            if does_saved==True:        
                url=""
                text_editor.delete(1.0,tk.END)
                root.title("Untitled        Micky Text Editor")
                does_existing_file_opened=False

        elif a==False:       
            url=""
            text_editor.delete(1.0,tk.END)
            root.title("Untitled        Micky Text Editor")
            does_existing_file_opened=False
        
        else:           
            pass   
    
    else:
        url=""
        text_editor.delete(1.0,tk.END)
        root.title("Untitled        Micky Text Editor")
        does_existing_file_opened=False



does_existing_file_opened=False
# existing_file_character=0
# Open file functionality
def open_file_Func(event=None):
    global url,does_existing_file_opened,existing_file_character

    # copied from on_closing_Func()
    current_file_character=text_editor.get(1.0,"end").replace(" ","").replace("\n","").replace("\t","")         # copied from upper
    changed=not (existing_file_character == current_file_character)
    if (len(current_file_character) != 0 and does_existing_file_opened==False ) or (does_existing_file_opened and changed):
        a=messagebox.askyesnocancel("Quit", "Do you want to save")          
        if a==True:     # if click yes
            does_saved=save_file_Func()
            if does_saved==True:        
                url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File Baby",filetypes=(("Text File Baby","*.txt"),("All files Baby","*.*")))
                # print(url)
                try:
                    with open(url,"r") as f:
                        text_editor.delete(1.0,tk.END)
                        text_editor.insert(1.0,f.read())
                        # print(f.read())
                    root.title(os.path.basename(url)+"          Micky Text Editor")
                    does_existing_file_opened=True
                    existing_file_character=text_editor.get(1.0,"end").replace(" ","").replace("\n","").replace("\t","")
                    # print(existing_file_character,"dav")
                except Exception as e:
                    print("Exception1")         # when open dialoge appear you did not select any file   


        elif a==False:       
            url=""
            text_editor.delete(1.0,tk.END)
            root.title("Untitled        Micky Text Editor")
            does_existing_file_opened=False
        
    else:           
        url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File Baby",filetypes=(("Text File Baby","*.txt"),("All files Baby","*.*")))
        # print(url)
        try:
            with open(url,"r") as f:
                text_editor.delete(1.0,tk.END)
                text_editor.insert(1.0,f.read())
                # print(f.read())
            root.title(os.path.basename(url)+"          Micky Text Editor")
            does_existing_file_opened=True
            existing_file_character=text_editor.get(1.0,"end").replace(" ","").replace("\n","").replace("\t","")
            # print(existing_file_character,"dav")
        except Exception as e:
            print("Exception1")         # when open dialoge appear you did not select any file   

# Save file functionality
def save_file_Func(event=None):
    global url,does_existing_file_opened,does_text_changed,existing_file_character

    content=text_editor.get(1.0,tk.END)
    # print(url)
    try:
        if url:         #If we open an existing file and write something
            with open(url,"w",encoding="utf-8") as f:
                f.write(content)
                f.close()
        else:           #If we create a completly new file
            url=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("Text File Baby","*.txt"),("All files Baby","*.*")))
            url.write(content)
            url.close()
            # print(url)
            # print(url.name)         #We will get the directory            It's completly own explore
            url=url.name
            root.title(os.path.basename(url)+"          Micky Text Editor")

        does_existing_file_opened=True              # If you create new file and change if you don't do that then still show "*untitled" rather that "*filename"  
        existing_file_character=text_editor.get(1.0,"end").replace(" ","").replace("\n","").replace("\t","")   
        does_text_changed=False
        # print("save",existing_file_character)
        change_status_bar_Func()            # Otherwise it will not update status bar or only give name instead of *name
        return True             # I used on on_closing_Func
    except Exception as e:
        print("Exception2")

# Save AS file functionality
def save_as_file_Func(event=None):
    global url
    content=text_editor.get(1.0,tk.END)
    try:
        url=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("Text File Baby","*.txt"),("All files Baby","*.*")))
        url.write(content)
        url.close()
        root.title(os.path.basename(url)+"          Micky Text Editor")
    except Exception as e:
        print("Exception3")
# Exit file functionality
# def exit_file_Func(event=None):
#     global url, does_text_changed
#     # print("exit",len(text_editor.get(1.0,tk.END)))
#     # print(does_text_changed)
#     try:
#         if does_text_changed:
#             mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
#             if mbox is True:        #If we click yes
#                 if url:             #If its an existing opened file
#                     content = text_editor.get(1.0, tk.END)
#                     with open(url, 'w', encoding='utf-8') as f:
#                         f.write(content)
#                         root.destroy()      #It will destroy after saving file
#                 else:           #If it's now created file
#                     content = text_editor.get(1.0, tk.END)
#                     url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
#                     url.write(content)
#                     url.close()
#                     root.destroy()      #It will destroy after saving file
#             elif mbox is False:     #If we click no
#                 # print("Don't save")
#                 root.destroy()
            
#         else:
#             # print("Please type something")
#             root.destroy()
#     except:
#         print("Exception4")



# Paste file functionality
def paste_file_Func():          #Copy,Cut,clear function like this.But we use lambda function for short our code
    text_editor.event_generate("<Control v>")



def find_file_Func(event=None):
    global does_Matched
    def find_Func():
        global does_Matched
        word = find_input.get()
        if len(word)==0:
            messagebox.showerror("Warning","Type something?")
            find_dialogue.destroy()
            find_file_Func()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)           # It will give you starting index where this "word" started
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)                             #You can give any tag name instead of "match"
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')      #You can give any tag name instead of "match"       settings textColor or foreground and background color
        if matches==0:
            messagebox.showerror("Warning","Did not match?")
            find_dialogue.destroy()
            find_file_Func()


    
    def replace_Func():
        # global find_input
        word = find_input.get()
        replace_text = replace_input.get()
        if len(word)==0 or len(replace_text)==0:
            messagebox.showerror("Warning","Please Type Somemting")
            find_dialogue.destroy()
            find_file_Func()


        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        if content==new_content:
            messagebox.showerror("Warning",f"Can't find{word}")
            find_dialogue.destroy()
            find_file_Func()
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)
        messagebox.showinfo("Changed",f'"{word}" replace with "{replace_text}"')


    find_dialogue = tk.Toplevel()                #Means it will crate a another window
    find_dialogue.geometry('450x250+500+200')       #Meaning of "500 + 200" Tkinter window is appearing at a different position (200 shifted on Y-axis and 500 shifted on X-axis)   own explore
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)           #WE can't resize the window

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find_Func)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace_Func)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()        #Sothat our window did not close





# Toolbar and status bar functionality

show_hide_statusbar = tk.BooleanVar()
show_hide_statusbar.set(True)       #By default statusBar will be show
show_hide_toolbar = tk.BooleanVar()
show_hide_toolbar.set(True)         #By default toolBar will be show

def show_hide_toolbar_Func():
    global show_hide_toolbar
    if show_hide_toolbar:
        tool_bar.pack_forget()          #It will hide toolbar
        show_hide_toolbar = False 
    else :                          #ToolBar in the top so we need to pack al the thing 
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_hide_toolbar = True 


def show_hide_statusbar_Func():
    global show_hide_statusbar
    if show_hide_statusbar:
        status_bar.pack_forget()
        show_hide_statusbar = False 
    else :                      #WE no need to pack all the thing because status bar at the bottom.WE just need to pack it
        status_bar.pack(side=tk.BOTTOM)
        show_hide_statusbar = True 


def on_closing_Func(event=None):           # when will click x to close the programme  
    global does_text_changed,existing_file_character
    current_file_character=text_editor.get(1.0,"end").replace(" ","").replace("\n","").replace("\t","")         # copied from upper
    changed=not (existing_file_character == current_file_character)
    if (len(current_file_character) != 0 and does_existing_file_opened==False ) or (does_existing_file_opened and changed):
            # print("1",text_editor.edit_modified())
            # print("2",does_existing_file_opened)
            # print("2",does_existing_file_opened)

        a=messagebox.askyesnocancel("Quit", "Do you want to save")          # yes=True,No=False,calcel=None
        if a==True:     # if click yes
            does_saved=save_file_Func()
            if does_saved==True:        # That means you savd.....When your saved window location appear and you close it without saving ....To prevent that .....Talent FAZLE
                root.destroy()

        elif a==False:        # if click no
            root.destroy()
        # print(a)
        
        else:               # if you give cancel
            pass        
    else:       # If you don't type anything or did not overwrite on opened file it will close
        root.destroy()
        

   

root.protocol("WM_DELETE_WINDOW", on_closing_Func)           # when will click x to close the programme this function(on_closing_Func) will run 



# File command
file.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl+N",command=new_file_Func)  #compound=tk.LEFT will give your image left    #accelerator will add text at the right
file.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl+O",command=open_file_Func) 
file.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="Ctrl+S",command=save_file_Func) 
file.add_command(label="Save As",image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+S",command=save_as_file_Func)

# file.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Ctrl+Q",command=exit_file_Func) 
file.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Ctrl+Q",command=on_closing_Func) 

# Edit Command

edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+C",command=lambda:text_editor.event_generate("<Control c>")) 
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator="Ctrl+V",command=paste_file_Func) 
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator="Ctrl+X",command=lambda:text_editor.event_generate("<Control x>")) 
edit.add_command(label="Clear All",image=clear_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+X",command=lambda:text_editor.delete(1.0,tk.END)) 
edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator="Ctrl+F",command=find_file_Func) 


# View's CheckButton

view.add_checkbutton(label="Tool Bar",image=tool_bar_icon,compound=tk.LEFT,variable = show_hide_toolbar,command=show_hide_toolbar_Func)
view.add_checkbutton(label="Status Bar",image=status_bar_icon,compound=tk.LEFT,variable = show_hide_statusbar, command=show_hide_statusbar_Func)

# Color Theme Radio Button

selected_theme=tk.StringVar()         #There  will store which icon we chosen
selected_theme.set('Light Default')
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)



color_dict = {
    'Light Default' : ('#000000', '#ffffff'),      #(TextColor,Background Color)
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}


#Change Color Theme functionality
## color theme 
def change_theme_Func():
    chosen_theme = selected_theme.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(bg=bg_color, fg=fg_color) 


count=0
for i in color_dict:
    color_Theme.add_radiobutton(label=i,image=color_icons[count],variable=selected_theme,compound=tk.LEFT,command=change_theme_Func)
    count+=1

# -------------------------------------&&&&&&&& End Main menu functionality &&&&&&&&&&& ----------------------------------

root.config(menu=main_Menu) 



#### bind shortcut keys 
root.bind("<Control-n>", new_file_Func)
root.bind("<Control-o>", open_file_Func)
root.bind("<Control-s>", save_file_Func)
root.bind("<Control-Alt-s>", save_as_file_Func)
# root.bind("<Control-q>", exit_file_Func)
root.bind("<Control-q>", on_closing_Func)       
root.bind("<Control-f>", find_file_Func)


root.mainloop()