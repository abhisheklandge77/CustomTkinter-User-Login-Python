import customtkinter as ctk
from tkinter import messagebox
from userinfopage import userWindow
from services import loginUser

def goToSignupPage():
    loginWindow.destroy()
    import signuppage

def clearLoginForm():
    loginEmail.delete(0, ctk.END)
    loginPassword.delete(0, ctk.END)

def onLoginBtnClick():
    emailVal = loginEmail.get()
    passwordVal = loginPassword.get()
    
    if(emailVal == '' or passwordVal == ''):
        messagebox.showerror(title="Error", message="All fields are required !")
    else:
        try:
            payload = {
                "email": emailVal,
                "password": passwordVal
            }
            response = loginUser(payload)
            clearLoginForm()
            if(response  == "Invalid Credentials !"):
                messagebox.showerror(title="Error", message="Invalid Credentials !")
            else:
                messagebox.showinfo(title="Success", message="Login Successful")
                loginWindow.destroy()
                userWindow(response)
        except:
            messagebox.showerror(title="Error", message="Login Failed")


loginWindow = ctk.CTk()

loginWindow.title("Python Curricular Activity")
loginWindow.geometry("600x550")

headingLabel = ctk.CTkLabel(loginWindow, text="Login", font=ctk.CTkFont(size=30, weight="bold"))
headingLabel.pack(padx=10, pady=(40, 20))

loginEmail = ctk.CTkEntry(loginWindow, placeholder_text="Email", width=250)
loginEmail.pack(pady=15)

loginPassword = ctk.CTkEntry(loginWindow, placeholder_text="Password", show=["*"], width=250)
loginPassword.pack(pady=15)

loginBtn = ctk.CTkButton(loginWindow, text="Login", width=250, command=onLoginBtnClick)
loginBtn.pack(pady=(15,0))

signUpLink = ctk.CTkButton(loginWindow, text="Don't have an account? Sign up here", font=ctk.CTkFont(size=12, underline=True), text_color="#fff", fg_color="#2b2b2b", hover_color="#2b2b2b", command=goToSignupPage,  anchor="center")
signUpLink.pack(pady=(10,0))

loginWindow.mainloop()