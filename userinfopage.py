import customtkinter as ctk
from updateuserpage import updateUserWindow
from tkinter import messagebox
from services import deleteUser

def onLogoutBtnClick():
    userInfoWindow.destroy()
    import loginpage

def onUpdateBtnClick():
    updateUserWindow(userDetails)

def onDeleteBtnClick():
    if(messagebox.askyesno(title="Confirm", message="Are you sure you want to delete this account ?")):
        try:
            response = deleteUser(userDetails)
            if(response  == "User Deletiton Failed !"):
                messagebox.showerror(title="Error", message="User Deletiton Failed !")
            else:
                messagebox.showinfo(title="Success", message="User Deleted Successfully")
                userInfoWindow.destroy()
                import loginpage
        except:
            messagebox.showerror(title="Error", message="User Deletiton Failed !")


def userWindow(userData):
    global userInfoWindow
    global userDetails
    userDetails = userData
    print("userData:",userData)

    userInfoWindow = ctk.CTk()

    userInfoWindow.title("Python Curricular Activity")
    userInfoWindow.geometry("600x550")


    logotBtn = ctk.CTkButton(userInfoWindow, text="Logout", width=120, fg_color="transparent", border_color="#fff", border_width=1, command=onLogoutBtnClick)
    logotBtn.pack(pady=(15,0))

    headingLabel = ctk.CTkLabel(userInfoWindow, text="User Info", font=ctk.CTkFont(size=30, weight="bold"))
    headingLabel.pack(padx=10, pady=(40, 20))

    userInfoFrame = ctk.CTkFrame(userInfoWindow, width=350, height=400)
    userInfoFrame.pack(fill="both")

    nameLabel = ctk.CTkLabel(userInfoFrame, text=("Name: "+ userData[1]), font=ctk.CTkFont(size=20, weight="bold"))
    nameLabel.pack(padx=10, pady=(30, 10))

    emailLabel = ctk.CTkLabel(userInfoFrame, text=("Email: "+ userData[2]), font=ctk.CTkFont(size=20, weight="bold"))
    emailLabel.pack(padx=10, pady=(10,10))

    addressLabel = ctk.CTkLabel(userInfoFrame, text=("Address: "+ userData[3]), font=ctk.CTkFont(size=20, weight="bold"))
    addressLabel.pack(padx=10, pady=(10,30))

    updateBtn = ctk.CTkButton(userInfoWindow, text="Update", fg_color="#04ba28", hover_color="#03a323", width=150, command=onUpdateBtnClick)
    updateBtn.place(x=145, y=350)

    deleteBtn = ctk.CTkButton(userInfoWindow, text="Delete", fg_color="#fc0000", hover_color="#db0404", width=150, command=onDeleteBtnClick)
    deleteBtn.place(x=320, y=350)

    userInfoWindow.mainloop()