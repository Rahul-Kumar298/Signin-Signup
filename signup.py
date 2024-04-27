import tkinter as tk 
import json
from tkinter import messagebox


def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'users': []}  # Initialize 'users' key if the file doesn't exist
    return data
def save_data(filename, data):
    with open(filename, 'w') as file:  # Use 'w' mode to overwrite the file
        json.dump(data, file, indent=4)

def open_gui(username):
    signup_frame.pack_forget()
    # Update the welcome label text with the logged-in username
    l1= tk.Label(welcome_frame,text=f'Hello, {username}' , font=('Times New Roman',20,'italic'),bg='aqua')
    l1.pack()
    welcome_frame.pack()


def signin():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    remember_me = remember_me_var.get()  # Get the value of the "Remember Me" checkbox
     # Check if username and password are not blank
    if not username or not password:
        messagebox.showerror("Error", "Username and Password cannot be blank.")
        return

    # Check if username and password are correct
    for user in data['users']:
        if user['username'] == username:
            messagebox.showinfo("Already Signed in", "Please login instead of signing in")
            return  # No need to continue if the user is already signed in

    # Check if password matches the confirm password
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match. Please enter the password correctly.")
        return  # Exit the function if passwords don't match

    # Add the user to the users list
    data['users'].append({'username': username, 'password': password, 'remember_me': remember_me})
    messagebox.showinfo("Successfully signed in", f"Your username and password are: {username} and {password} respectively.")


    # Save the data
    save_data('logindata.json', data)
    signup_frame.pack_forget()

    #  Update the welcome label text with the logged-in username
    l1= tk.Label(welcome_frame,text=f'Hello, {username}' , font=('Times New Roman',20,'italic'),bg='aqua')
    l1.pack()
    welcome_frame.pack()

def focus_next_entry(event):
    event.widget.tk_focusNext().focus()


def go_to_login():
    from signin import login_frame
    # Implement the function to navigate to the login page here
    signup_frame.pack_forget()
    login_frame.pack()

# Load data
data = load_data('logindata.json')
root=tk.Tk()
root.title('Sigup Window')
root.geometry('300x300')

root.wm_iconbitmap('D:\python\Gui\signin\sign_up.ico')
# Create login frame widget
# login_frame = create_login_frame(root)
# signup_frame = create_signup_frame(root)
signup_frame = tk.Frame(root)
tk.Label(signup_frame, text="Username:", font="sans-serif 10 bold").grid (row=1, column=1, pady=7, sticky='e')
username_entry = tk.Entry(signup_frame)
username_entry.grid(row=1, column=2, sticky='w')
# Bind the <Return> event to the username entry
username_entry.bind('<Return>', focus_next_entry)
tk.Label(signup_frame, text="Password:", font="sans-serif 10 bold").grid(row=2, column=1, pady=12, sticky='e')   
password_entry = tk.Entry(signup_frame, show="*")
password_entry.grid(row=2, column=2, sticky='w')
# Bind the <Return> event to the password entry
password_entry.bind('<Return>', focus_next_entry)
tk.Label(signup_frame, text="Confirm Password:", font="sans-serif 10 bold").grid(row=3, column=1, pady=12, sticky='e')   
confirm_password_entry = tk.Entry(signup_frame)
confirm_password_entry.grid(row=3, column=2, sticky='w')
# Bind the <Return> event to the password entry
confirm_password_entry.bind('<Return>', lambda event: signin())    
signup_button = tk.Button(signup_frame, text="signup", command=signin, font='roboto 10 bold' , pady=6)
# Modify your login screen creation to include the "Remember Me" option
remember_me_var = tk.BooleanVar()
remember_me_checkbox = tk.Checkbutton(signup_frame, text="Remember Me", variable=remember_me_var)
remember_me_checkbox.grid(row=4, column=1, columnspan=2, pady=10)       
signup_button.grid(row=5, column=1, columnspan=2, padx=20, pady=10, sticky='ew')
# Create login link label

signin_link_label = tk.Label(signup_frame, text="Already have an account, Signin here.", fg="red", cursor="hand2")
signin_link_label.bind("<Button-1>", lambda event: go_to_login())

signin_link_label.grid(row=6, column=1, columnspan=2, padx=20, pady=10)

# welcome frame widget
welcome_frame = tk.Frame(root)


# Check if "Remember Me" was selected in the previous login
remember_me_previous = data['users'][0].get('remember_me', False) if data['users'] else False
try:
    if remember_me_previous:
        open_gui(data['users'][0]['username'])  # Provide the username argument
    else:
        signup_frame.pack()
except:
    signup_frame.pack()
root.mainloop()
