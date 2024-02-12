import os 
import sys
from tkinter import *
import shutil
from tkinter import  filedialog, messagebox as m
from datetime import datetime
from customtkinter import *
from customtkinter import CTkImage as i
from PIL import Image

root=CTk()

def ask_for_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        organize_files(directory_path)

def organize_files(directory_path):
    try:
        files = os.listdir(directory_path)
        special_order = {'Images': ['jpg', 'png', 'gif','jpeg','bmp'],
                         'Documents': ['doc', 'pdf', 'txt','docx','pptx','xlsx'],
                         'Icons':['ico'],
                         'Videos': ['mp4', 'avi', 'mkv'],
                         'Zip':['zip'],
                         'Txt':['txt'],
                         'C Language':['c','o'],
                         'C++ Language':['cpp'],
                         'Python Language':['py'],
                         'HTML CSS JS':['html','css','js','htm','xhtml'],
                         'Applications':['exe'],
                         'Java':['class','java'],
                         'Others': []}

        for file_name in files:
            file_path = os.path.join(directory_path, file_name)

            if os.path.isfile(file_path):
                file_type = get_file_type(file_name, special_order)
                target_folder = get_target_folder(file_type, directory_path)

                target_path = os.path.join(directory_path, target_folder, file_name)
                os.makedirs(os.path.join(directory_path, target_folder), exist_ok=True)

                if not os.path.exists(target_path):
                    shutil.move(file_path, target_path)
                else:
                    handle_duplicate(file_path, target_path)

        m.showinfo("Success", "Congratulations Your Files Organized Successfully!")

    except Exception as e:
        m.showerror("Error", f"An error occurred: {str(e)}")

def get_file_type(file_name, special_order):
    file_extension = file_name.split('.')[-1].lower()

    for category, extensions in special_order.items():
        if file_extension in extensions:
            return category

    return 'Others'

def get_target_folder(file_type, directory_path):
    if file_type != 'Others':
        return file_type
    else:
        return 'Others'

def handle_duplicate(source_path, target_path):
    base, extension = os.path.splitext(target_path)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_target_path = f"{base}_{timestamp}{extension}"

    shutil.move(source_path, new_target_path)
    print(base)
    print(extension)
    print(timestamp)

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Running as a script, use the current working directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def switch():
    if(m.askyesno("--File Organizer App--","--Want dark  mode!--")):
        set_appearance_mode('dark')
    elif(m.askquestion("--File Organizer App--","--Want light mode!--")):
        set_appearance_mode('light')
        root.configure(bg_color="white")
    
        

def main():
    #root = CTk()
    root.title("--File Organizer--")
    root.geometry("650x450")
    # root.minsize(500,400)
    # root.maxsize(600,400)
    root.overrideredirect(True)
    # root.wm_manage(CTkLabel)
    #root.wm_iconbitmap("file2.ico")
    set_appearance_mode("light")
    set_default_color_theme("TrojanBlue")
    #set_default_color_theme("GhostTrain")
   
    def moveapp(e):
        root.geometry(f"+{e.x_root}+{e.y_root}")
   
    t_bar=CTkFrame(master=root,border_width=3,cursor="arrow",border_color=("orange","black"))
    t_bar.pack(fill=X,expand=1,side=TOP,anchor=N)
    t_bar.bind("<B1-Motion>",moveapp)
    
    photo = i(light_image=Image.open(resource_path('filer.png')),dark_image=Image.open(resource_path('filer.png')),size=(80,80)) #wXh
    
    t_l=CTkLabel(master=t_bar,image=photo,font=("Helvetica", 20, "bold"),text="",bg_color=("orange","black"),fg_color=("orange","black"))
    t_l.pack(side=LEFT)

    t_b=CTkButton(master=t_bar,text=" X ",command=root.destroy,cursor="hand2",hover_color=("red","blue"),corner_radius=4)
    t_b.pack(side=RIGHT,padx=2)
    
    t_o=CTkSwitch(master=t_bar,border_color="black",text_color="grey",text="switch mode",command=switch,font=("Comicsans",15),progress_color="yellow",onvalue=1,offvalue=1,border_width=3,switch_width=40,width=5,height=2)
    t_o.pack(pady=2)
    
        
    Label1=CTkLabel(master=t_bar,text="Welcome the File Organizer App",font=("helvetica", 20,"bold"),fg_color=("#9932CC","#AA0"))
    Label1.pack(pady=20,padx=10)
     
    label = CTkLabel(master=root, text="Click the button to organize files.",fg_color=("purple","black"),font=("helvetica", 14,"bold"),cursor="ibeam")
    label.pack(pady=10,padx=10)
    
    disc=CTkLabel(master=root,text="Disclaimer we will sort your files in folders in the same directory in a order ",wraplength=250,fg_color="red",font=("helvetica", 15, "bold"))
    disc.pack(pady=10,padx=5)
    
    organize_button = CTkButton(master=root,corner_radius=4,font=("Comicsans",12), text="Organize Files",command=ask_for_directory,cursor="hand2",width=10,border_color="yellow")
    organize_button.pack(pady=20,padx=10)
    
    e_button = CTkButton(master=root, text="Close App",font=("Comicsans",12),command=root.destroy,cursor="hand2",width=10,border_color="orange",corner_radius=4,fg_color="red")
    e_button.pack(pady=20,padx=10)
   
    s1=CTkLabel(master=root,text="Muhammad Hasnat Rasool",fg_color=("green","blue"),font=("helvetica", 20 ))
    s1.pack(side='bottom',anchor="s",fill="x")
    # root.configure(bg_color="yellow")   
    # root.configure(fg_color="yellow")   
    root.mainloop()

if __name__ == "__main__":
    main()