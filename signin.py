# signup.py
import tkinter as tk
import json


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
    login_frame.pack_forget()
    # Update the welcome label text with the logged-in username
    l1= tk.Label(welcome_frame,text=f'Hello, {username}' , font=('Times New Roman',20,'italic'),bg='aqua')
    l1.pack()
    welcome_frame.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()
    remember_me = remember_me_var.get()  # Get the value of the "Remember Me" checkbox

    # Check if username and password are correct
    for user in data['users']:
        if user['username'] == username and user['password'] == password:
            # Hide the login screen
            login_frame.pack_forget()
            # Update the welcome label text with the logged-in username
            l1= tk.Label(welcome_frame,text=f'Hello, {username}' , font=('Times New Roman',20,'italic'),bg='aqua')
            l1.pack()
            # Store login details and "Remember Me" option
            welcome_frame.pack()
            user['remember_me'] = remember_me
            save_data('logindata.json', data)
            return

    # Display an error message
    error_label.config(text="Invalid username or password")

def focus_next_entry(event):
    event.widget.tk_focusNext().focus()


def go_to_signup():
    from signup import signup_frame
    # Implement the function to navigate to the login page here
    login_frame.pack_forget()
    signup_frame.pack()

# Load data
data = load_data('logindata.json')
root=tk.Tk()
root.title('Sigin Window')
root.geometry('300x300')
root.wm_iconbitmap('D:\python\Gui\signin\login.ico')
root.config(background='aqua')
# Create login frame widget
login_frame = tk.Frame(root)
tk.Label(login_frame, text="Username:", font="sans-serif 10 bold").grid (row=1, column=1, pady=7, sticky='e')
username_entry = tk.Entry(login_frame)
username_entry.grid(row=1, column=2, sticky='w')
# Bind the <Return> event to the username entry
username_entry.bind('<Return>', focus_next_entry)
tk.Label(login_frame, text="Password:", font="sans-serif 10 bold").grid(row=2, column=1, pady=12, sticky='e')   
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=2, sticky='w')
# Bind the <Return> event to the password entry
password_entry.bind('<Return>', lambda event: login())
# Modify your login screen creation to include the "Remember Me" option
remember_me_var = tk.BooleanVar()
remember_me_checkbox = tk.Checkbutton(login_frame, text="Remember Me", variable=remember_me_var)
remember_me_checkbox.grid(row=3, column=1, columnspan=2, pady=10)   
login_button = tk.Button(login_frame, text="Login", command=login, font='roboto 10 bold' , pady=6)
    
login_button.grid(row=4, column=1, columnspan=2, padx=20, pady=10, sticky='ew')
error_label = tk.Label(login_frame, fg="red", font=('Times New Roman', 20, 'bold'))
error_label.grid(row=6, column=1, columnspan=2)  # Adjust columnspan as per your layout
# Create login link label

signin_link_label = tk.Label(login_frame, text="Don't have an account? Signup here.", fg="red", cursor="hand2")
signin_link_label.bind("<Button-1>", lambda event: go_to_signup())

signin_link_label.grid(row=5, column=1, columnspan=2, padx=20, pady=10)

# welcome frame widget
welcome_frame = tk.Frame(root)
# Check if "Remember Me" was selected in the previous login
remember_me_previous = data['users'][0].get('remember_me', False) if data['users'] else False
try:
    if remember_me_previous:
        open_gui(data['users'][0]['username'])  # Provide the username argument
    else:
        login_frame.pack()
except:
    login_frame.pack()
root.mainloop()
