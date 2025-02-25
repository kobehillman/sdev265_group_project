import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from subprocess import call
import sqlite3
from CTkToolTip import CTkToolTip


# ATTN KOBE:
## RANDOM PASSWORD GEN - STRING OF NUMBERS AND LETTERS "STRONG" PASSWORD"

# DESCRIPTION FOR PASSWORD

#







##


def sign_out():

    users = sqlite3.connect('appdata.db')
    mycursor = users.cursor()

    command = "update users set LoggedIn = 0 where LoggedIn = 1"
    mycursor.execute(command)
    users.commit()
    users.close()

    messagebox.showinfo("Sign Out", "Signing out...")

    app.destroy()

    call(['python', 'login.py'])


def cursor_on_hover(button):
    button.configure(cursor='hand2')


def reset_cursor_on_leave(button):
    button.configure(cursor='none')


def fetch_current_user(database):

   try:

    users = sqlite3.connect(database)
    mycursor = users.cursor()

    command = "select * from users where LoggedIn = 1"
    mycursor.execute(command)

    result = mycursor.fetchone()

    logged_in_user = result[1]

    return logged_in_user

   except:
       logged_in_user = "current_user"

       return logged_in_user




def exit_button(window):
    users = sqlite3.connect("appdata.db")
    mycursor = users.cursor()

    command = "update users set LoggedIn = 0 where LoggedIn = 1"
    mycursor.execute(command)
    users.commit()
    users.close()

    window.destroy()


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


class Main(ctk.CTk):

    def show_frames(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.wm_title('Main | Password Manager')
        self.geometry('1000x600')
        self._set_appearance_mode('dark')
        self.resizable(False, False)
        self.wm_iconbitmap('appicon.ico')
        self.eval("tk::PlaceWindow . center")
        self.protocol("WM_DELETE_WINDOW", lambda: exit_button(self))
        self.configure(fg_color='#212c56')

        # CREATES AND PLACES FRAME FOR PAGES ON THE RIGHT SIDE
        container = ctk.CTkFrame(self, height=500, width=900, fg_color="#212c56")
        container.place(x=100, y=100)

        self.frames = {}

        for F in (HomePage, StoredPasswordsPage, SettingsPage, FavoritesPage, GeneratePasswordPage, ProfilePage, AddPasswordPage):
            frame = F(container, self)
            frame.configure(height=500, width=900)

            self.frames[F] = frame
            frame.place(x=0, y=0)

        self.show_frames(HomePage)

        # ----------------- TOOLBAR BASE ----------------------- #
        toolbar_top = ctk.CTkFrame(self, height=60, width=60, fg_color='#151c36')
        toolbar_top.place(x=15, y=60)

        toolbar_middle = ctk.CTkFrame(self, height=300, width=60, fg_color='#151c36')
        toolbar_middle.place(x=15, y=140)

        toolbar_bottom = ctk.CTkFrame(self, height=60, width=60, fg_color='#151c36')
        toolbar_bottom.place(x=15, y=460)

        separator_line = ctk.CTkFrame(self, height=600, width=2, fg_color="#151c36")
        separator_line.place(x=90, y=0)

        tool_button_divider_home = ctk.CTkFrame(self, height=2, width=60, fg_color='#333a55')
        tool_button_divider_home.place(x=15, y=200)

        tool_button_divider_favorites = ctk.CTkFrame(self, height=2, width=60, fg_color='#333a55')
        tool_button_divider_favorites.place(x=15, y=260)

        tool_button_divider_stored_passwords = ctk.CTkFrame(self, height=2, width=60, fg_color='#333a55')
        tool_button_divider_stored_passwords.place(x=15, y=320)

        tool_button_divider_generate_passwords = ctk.CTkFrame(self, height=2, width=60, fg_color='#333a55')
        tool_button_divider_generate_passwords.place(x=15, y=380)

        # ----------------- TOOLBAR ICONS ----------------------- #
        home_icon = ctk.CTkImage(Image.open('toolbar_icons/home_icon.png'))
        home_icon._size = 40, 40

        favorite_icon = ctk.CTkImage(Image.open('toolbar_icons/star_icon.png'))
        favorite_icon._size = 40, 40

        stored_password_icon = ctk.CTkImage(Image.open('toolbar_icons/stored_passwords_icon.png'))
        stored_password_icon._size = 40, 40

        generate_password_icon = ctk.CTkImage(Image.open('toolbar_icons/generate_icon.png'))
        generate_password_icon._size = 40, 40

        user_icon = ctk.CTkImage(Image.open('toolbar_icons/user_icon.png'))
        user_icon._size = 40, 40

        add_icon = ctk.CTkImage(Image.open('toolbar_icons/add_icon.png'))
        add_icon._size = 40, 40

        toolbar_logo = ctk.CTkImage(Image.open('main_menu_logo.png'))
        toolbar_logo._size = 50, 50

        # ----------------- TOOLBAR IMAGE HOLDERS & BUTTONS ----------------------- #
        home_icon_button = ctk.CTkButton(toolbar_middle, height=60, width=60, image=home_icon, fg_color='transparent', text='', hover=False, command=lambda: self.show_frames(HomePage))
        home_icon_button.place(x=0, y=3)

        favorite_icon_button = ctk.CTkButton(toolbar_middle, height=60, width=60, image=favorite_icon, fg_color='transparent', text='', hover=False, command=lambda: self.show_frames(FavoritesPage))
        favorite_icon_button.place(x=0, y=63)

        stored_passwords_icon_button = ctk.CTkButton(toolbar_middle, height=60, width=60, image=stored_password_icon, fg_color='transparent', text='', hover=False, command=lambda: self.show_frames(StoredPasswordsPage))
        stored_passwords_icon_button.place(x=0, y=123)

        generate_password_icon_button = ctk.CTkButton(toolbar_middle, height=60, width=60, image=generate_password_icon, fg_color='transparent', text='', hover=False, command=lambda: self.show_frames(GeneratePasswordPage))
        generate_password_icon_button.place(x=0, y=183)

        user_icon_button = ctk.CTkButton(toolbar_middle, height=40, width=40, image=user_icon, fg_color='transparent', text='', hover=False, command=lambda: self.show_frames(ProfilePage))
        user_icon_button.place(x=2, y=248)

        add_icon_button = ctk.CTkButton(toolbar_bottom, height=40, width=40, image=add_icon, fg_color='transparent', text='', hover=False, command=lambda: self.show_frames(AddPasswordPage))
        add_icon_button.place(x=2, y=6)

        toolbar_logo_label = ctk.CTkLabel(toolbar_top, text='', image=toolbar_logo)
        toolbar_logo_label.place(x=5, y=5)

        # ----------------- TOOLBAR MISC FUNCTIONALITY ----------------------- #
        home_icon_button.bind('<Enter>', lambda event: cursor_on_hover(home_icon_button))
        home_icon_button.bind('<Leave>', lambda event: reset_cursor_on_leave(home_icon_button))

        add_icon_button.bind('<Enter>', lambda event: cursor_on_hover(add_icon_button))
        add_icon_button.bind('<Leave>', lambda event: reset_cursor_on_leave(add_icon_button))

        favorite_icon_button.bind('<Enter>', lambda event: cursor_on_hover(favorite_icon_button))
        favorite_icon_button.bind('<Leave>', lambda event: reset_cursor_on_leave(favorite_icon_button))

        stored_passwords_icon_button.bind('<Enter>', lambda event: cursor_on_hover(stored_passwords_icon_button))
        stored_passwords_icon_button.bind('<Leave>', lambda event: reset_cursor_on_leave(stored_passwords_icon_button))

        generate_password_icon_button.bind('<Enter>', lambda event: cursor_on_hover(generate_password_icon_button))
        generate_password_icon_button.bind('<Leave>', lambda event: reset_cursor_on_leave(generate_password_icon_button))

        user_icon_button.bind('<Enter>', lambda event: cursor_on_hover(user_icon_button))
        user_icon_button.bind('<Leave>', lambda event: reset_cursor_on_leave(user_icon_button))

        # ----------------- TOP BAR --------------------- #

        top_bar = ctk.CTkFrame(self, height=90, width=900, fg_color='#212c56')
        top_bar.place(x=99, y=5)

        settings_icon = ctk.CTkImage(Image.open('toolbar_icons/settings_icon.png'))
        settings_icon._size = 35, 35

        settings_icon_button = ctk.CTkButton(top_bar, image=settings_icon, fg_color='transparent', text='', hover=False, command=lambda: self.show_frames(SettingsPage))
        settings_icon_button.place(x=740, y=25)

        settings_icon_button.bind('<Enter>', lambda event: cursor_on_hover(settings_icon_button))
        settings_icon_button.bind('<Leave>', lambda event: reset_cursor_on_leave(settings_icon_button))

        settings_text = ctk.CTkLabel(top_bar, text='Settings', font=('Helvetica', 10))
        settings_text.place(x=790, y=65)

        sign_out_icon = ctk.CTkImage(Image.open('toolbar_icons/sign_out_icon.png'))
        sign_out_icon._size = 33, 33

        sign_out_icon_button = ctk.CTkButton(top_bar, image=sign_out_icon, command= sign_out, fg_color='transparent', text='', hover=False, height=30, width=30)
        sign_out_icon_button.place(x=840, y=25)

        sign_out_text = ctk.CTkLabel(top_bar, text='Sign Out', font=('Helvetica', 10))
        sign_out_text.place(x=840, y=65)

        sign_out_icon_button.bind('<Enter>', lambda event: cursor_on_hover(sign_out_icon_button))
        sign_out_icon_button.bind('<Leave>', lambda event: reset_cursor_on_leave(sign_out_icon_button))

        greeting_label = ctk.CTkLabel(top_bar, text='Hello,', font=("Great Vibes", 26, "bold"), width=200)
        greeting_label.place(x=40, y=10)

        current_user = fetch_current_user('appdata.db')

        current_user_label = ctk.CTkLabel(top_bar, text=current_user, font=("Lucida Sans", 20), width=200)
        current_user_label.place_configure(x=100, y=40)

        profile_picture = ctk.CTkImage(Image.open('profile_picture.png'))
        profile_picture._size = 100, 100

        profile_picture_label = ctk.CTkLabel(top_bar, text='', image=profile_picture, )
        profile_picture_label.place(x=0, y=0)

        # -------------------- TOOLTIPS ------------------- #
        home_tooltip = CTkToolTip(home_icon_button, message='Home', delay=0.1)

        favorites_tooltip = CTkToolTip(favorite_icon_button, message='Favorites', delay=0.1)

        stored_passwords_tooltip = CTkToolTip(stored_passwords_icon_button, message='Stored Passwords', delay=0.1)

        generate_password_tooltip = CTkToolTip(generate_password_icon_button, text_color='green', message='Generate Password', delay=0.1)

        user_tooltip = CTkToolTip(user_icon_button, message='My Account', delay=0.1)

        add_tooltip = CTkToolTip(add_icon_button, message='Add New Password', delay=0.1)


class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color='#212c56')

        button = ctk.CTkButton(self, text='Home Page')
        button.place(x=50, y=100)

        separator_line = ctk.CTkFrame(self, height=500, width=2, fg_color="#151c36")
        separator_line.place(x=600, y=0)

        frame = ctk.CTkScrollableFrame(self, height=460, width=565, fg_color="#151c36", scrollbar_button_color='#333a55', scrollbar_button_hover_color='#3e4769')
        frame.place(x=0, y=10)


class StoredPasswordsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color='#212c56')

        button = ctk.CTkButton(self, text='Stored Passwords')
        button.place(x=50, y=100)


class SettingsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color='#212c56')
        button = ctk.CTkButton(self, text='Settings')
        button.place(x=50, y=100)


class FavoritesPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color='#212c56')
        button = ctk.CTkButton(self, text="Favorites")
        button.place(x=50, y=100)


class GeneratePasswordPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color='#212c56')
        button = ctk.CTkButton(self, text="Generate Password")
        button.place(x=50, y=100)


class ProfilePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color='#212c56')
        button = ctk.CTkButton(self, text="Profile Page")
        button.place(x=50, y=100)


class AddPasswordPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color='#212c56')
        button = ctk.CTkButton(self, text="Add Password Page")
        button.place(x=50, y=100)


if __name__ == '__main__':
    app = Main()
    app.mainloop()
