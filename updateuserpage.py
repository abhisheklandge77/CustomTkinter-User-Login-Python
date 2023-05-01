import customtkinter as ctk
from tkinter import messagebox
from services import updateUser

def clearUpdateForm():
    userName.delete(0, ctk.END)
    email.delete(0, ctk.END)
    address.delete(0, ctk.END)

def onUpdateUserBtnClick():
    emailVal = email.get()
    userNameVal = userName.get()
    
    if(emailVal == '' or userNameVal == ''):
        messagebox.showerror(title="Error", message="All fields are required !")
    else:
        try:
            payload = {
                "id": userDetails[0],
                "userName": userNameVal,
                "email": emailVal,
            }
            response = updateUser(payload)
            clearUpdateForm()
            if(response  == "Updation Failed !"):
                messagebox.showerror(title="Error", message="Updation Failed !")
            else:
                messagebox.showinfo(title="Success", message="User Updated Successfully")
                updateUserInfoWindow.destroy()
                # userWindow(response)
        except:
            messagebox.showerror(title="Error", message="Updation Failed !")


def updateUserWindow(userData):
    global updateUserInfoWindow
    global email
    global userName
    global address
    global userDetails

    userDetails = userData

    updateUserInfoWindow = ctk.CTk()

    updateUserInfoWindow.title("Python Curricular Activity")
    updateUserInfoWindow.geometry("600x550")

    headingLabel = ctk.CTkLabel(updateUserInfoWindow, text="Update User Info", font=ctk.CTkFont(size=30, weight="bold"))
    headingLabel.pack(padx=10, pady=(40, 20))

    userName = ctk.CTkEntry(updateUserInfoWindow, placeholder_text="User Name", width=250)
    userName.pack(pady=15)
    userName.insert(0, userData[1])

    email = ctk.CTkEntry(updateUserInfoWindow, placeholder_text="Email", width=250)
    email.pack(pady=15)
    email.insert(0, userData[2])

    address = ctk.CTkEntry(updateUserInfoWindow, placeholder_text="Address", width=250)
    address.pack(pady=15)
    address.insert(0, userData[3])

    updateBtn = ctk.CTkButton(updateUserInfoWindow, text="Update", width=250, command=onUpdateUserBtnClick)
    updateBtn.pack(pady=(15,0))

    updateUserInfoWindow.mainloop()
