import customtkinter
from datetime import datetime
from settings import time_rest, time_pom, pomodor, long_rest, size_cycle, app_conf
from time_push import start_longrest, stop_pom_message, stop_rest_message
from PIL import Image
import json

# customtkinter.get_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

tick = 0
after_id = ''
temp = 0
img = Image.open("media/setting.png")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Pomodoro(demo)")
        self.geometry(f"{376}x{275}")
        self.resizable(width=False, height=False)

        # add icon
        self.iconbitmap("media/pomodor.ico")

        # create vidgets
        self.time_lable = customtkinter.CTkLabel(self, font=("Arial Rounded MT Bold", 60), text="00:00",
                                                 text_color="#dc143c", )
        self.time_lable.grid(row=0, column=0)
        self.time_lable.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

        # pomodoro time
        self.btnstart = customtkinter.CTkButton(self, text="Start focusing", font=("Arial Rounded MT Bold", 20),
                                                width=140, corner_radius=8, command=self.start_time)
        self.btnstart.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        self.btnstop = customtkinter.CTkButton(self, text="Stop", font=("Arial Rounded MT Bold", 20), width=140,
                                               corner_radius=8, command=self.stop_tick)
        self.btnreset = customtkinter.CTkButton(self, text="Reset", font=("Arial Rounded MT Bold", 20), width=140,
                                                corner_radius=8, command=self.tick_reset)
        self.btncontin = customtkinter.CTkButton(self, text="Continue", font=("Arial Rounded MT Bold", 20), width=140,
                                                 corner_radius=8, command=self.tick_continue)

        # rest time
        self.btnrest = customtkinter.CTkButton(self, text="Start rest", font=("Arial Rounded MT Bold", 20), width=140,
                                               corner_radius=8, command=self.start_rest)
        self.btnstoprest = customtkinter.CTkButton(self, text="Stop rest", font=("Arial Rounded MT Bold", 20),
                                                   width=140, corner_radius=8, command=self.stop_tickrest)
        self.btnreset_rest = customtkinter.CTkButton(self, text="Reset", font=("Arial Rounded MT Bold", 20), width=140,
                                                     corner_radius=8, command=self.rest_tick_reset)
        self.btncontin_rest = customtkinter.CTkButton(self, text="Continue", font=("Arial Rounded MT Bold", 20),
                                                      width=140, corner_radius=8, command=self.continue_rest)
        self.leble_pomcheck = customtkinter.CTkLabel(self, text=f"Today: {pomodor} pom",
                                                     font=("Arial Rounded MT Bold", 15),
                                                     text_color="#FF7F50")
        # create settings button
        self.btnsetting = customtkinter.CTkButton(self, text="",
                                                  image=customtkinter.CTkImage(light_image=img, dark_image=img),
                                                  fg_color="transparent", hover_color="#37BCB3", width=25, height=25, command=self.view_settings)
        self.btnsetting.place(anchor=customtkinter.NW)

    # timer function
    def tick(self):
        global tick, after_id, temp, pomodor
        after_id = self.after(1000, self.tick)
        f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
        self.time_lable.configure(text=str(f_temp))
        temp += 1

        if f_temp[:2] == time_pom:
            temp = 0
            pomodor += 1
            self.stop_pom()

    def tick_rest(self):
        global tick, after_id, temp, time_rest
        after_id = self.after(1000, self.tick_rest)
        f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
        self.time_lable.configure(text=str(f_temp))
        temp += 1

        if f_temp[:2] == time_rest:
            temp = 0
            time_rest = app_conf["time_rest"]
            self.stop_rest()

    def start_time(self):
        self.time_lable.configure(text_color="#dc143c")
        self.tick()
        self.btnstart.place_forget()
        self.btnstop.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

    def stop_tick(self):
        self.leble_pomcheck.configure(text=f"Today: {pomodor} pom")
        self.leble_pomcheck.place(relx=0, rely=0.915)
        self.btnstop.place_forget()
        self.btnreset.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        self.btncontin.place(relx=0.5, rely=0.67, anchor=customtkinter.CENTER)
        self.after_cancel(after_id)

    def stop_tickrest(self):
        self.btnstoprest.place_forget()
        self.btnreset_rest.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        self.btncontin_rest.place(relx=0.5, rely=0.67, anchor=customtkinter.CENTER)
        self.after_cancel(after_id)

    def rest_tick_reset(self):
        global temp
        self.btnreset_rest.place_forget()
        self.btncontin_rest.place_forget()
        self.btnrest.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        self.time_lable.configure(text="00:00")
        temp = 0

    def tick_reset(self):
        global temp
        self.leble_pomcheck.place_forget()
        self.btnreset.place_forget()
        self.btncontin.place_forget()
        self.btnstart.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        self.time_lable.configure(text="00:00")
        temp = 0

    def tick_continue(self):
        self.leble_pomcheck.place_forget()
        self.btncontin.place_forget()
        self.btnreset.place_forget()
        self.btnstop.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

        self.tick()

    def stop_pom(self):
        self.leble_pomcheck.configure(text=f"Today: {pomodor} pom")
        self.leble_pomcheck.place(relx=0, rely=0.915)

        global time_rest, long_rest 
        self.after_cancel(after_id)
        self.btnstop.place_forget()
        self.btnrest.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

        if pomodor % size_cycle == 0 and pomodor >= 0:
            time_rest = long_rest
            start_longrest()
        else:
            stop_pom_message()

    def start_rest(self):
        self.leble_pomcheck.place_forget()
        self.time_lable.configure(text_color="#9acd32")
        self.tick_rest()
        self.btnrest.place_forget()
        self.btnstoprest.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

    def continue_rest(self):
        self.btncontin_rest.place_forget()
        self.btnreset_rest.place_forget()
        self.btnstoprest.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        self.tick_rest()

    def stop_rest(self):
        self.after_cancel(after_id)
        self.btnstoprest.place_forget()
        self.btnstart.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        stop_rest_message()
    
    
    def view_settings(self):
        setting = Settings()
        setting.mainloop()
    


class Settings(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Settings")
        self.geometry(f"{275}x{175}")
        self.resizable(width=False, height=False)
        self.iconbitmap("media/setting.ico")

        # make pomodor size
        self.pomsize = customtkinter.CTkLabel(self, text="pomodor size:", font=("ArialRoundedMT Bold", 15), )
        self.pomsize.place(anchor=customtkinter.NW)

        #make save buttun
        self.btn_save = customtkinter.CTkButton(self, text="Save", font=("Arial Rounded MT Bold", 15), 
                                                width=50, height=25,  corner_radius=8, hover_color="#dc143c", 
                                                command=self.save_values)
        self.btn_save.place(relx=0.4, rely=0.85 )

        # time value
        self.slider_pom_check = customtkinter.CTkLabel(self, text=time_pom)
        self.slider_pom_check.place(anchor=customtkinter.NW, relx=0.36, rely=0.009)

        # make rest size
        self.restsize = customtkinter.CTkLabel(self, text="short rest size:", font=("Arial Rounded MT Bold", 15))
        self.restsize.place(anchor=customtkinter.NW, rely=0.2)

        # time value
        self.slider_rest_check = customtkinter.CTkLabel(self, text=time_rest)
        self.slider_rest_check.place(anchor=customtkinter.NW, relx=0.37, rely=0.209)

        # make long rest size
        self.long_restsize = customtkinter.CTkLabel(self, text="long rest size:", font=("Arial Rounded MT Bold", 15))
        self.long_restsize.place(anchor=customtkinter.NW, rely=0.4)

        # time value
        self.slider_longrest_check = customtkinter.CTkLabel(self, text=long_rest)
        self.slider_longrest_check.place(anchor=customtkinter.NW, relx=0.35, rely=0.409)

        # make pomodor cycle size
        self.pomcycle = customtkinter.CTkLabel(self, text="pomodor cycle size:", font=("Arial Rounded MT Bold", 15))
        self.pomcycle.place(anchor=customtkinter.NW, rely=0.6)

        #time value
        self.pomcycle_check = customtkinter.CTkLabel(self, text=size_cycle)
        self.pomcycle_check.place(anchor=customtkinter.NW, relx=0.49, rely=0.609)

        # make time pomodor slider
        self.pomslider = customtkinter.CTkSlider(self, from_=10, to=59, command=self.size_pom_check, number_of_steps=49,
                                                 width=100, button_color="#dc143c", button_hover_color="#630a0a")
        self.pomslider.place(anchor=customtkinter.N, relx=0.7, rely=0.04)
        self.pomslider.set(int(time_pom))

        # make rest slider
        self.restslder = customtkinter.CTkSlider(self, from_=5, to=10, number_of_steps=5, width=100,
                                                 command=self.size_rest_check)
        self.restslder.place(anchor=customtkinter.N, relx=0.7, rely=0.24)
        self.restslder.set(int(time_rest))

        # make long rest slider
        self.long_restslider = customtkinter.CTkSlider(self, from_=10, to=30, number_of_steps=20, width=100,
                                                       command=self.size_longrest_check)
        self.long_restslider.place(anchor=customtkinter.N, relx=0.7, rely=0.44)
        self.long_restslider.set(int(long_rest))

        # make cycle slider
        self.cycle_clider = customtkinter.CTkSlider(self, from_=3, to=5, number_of_steps=2, width=80,
                                                    command=self.size_cycle_check, button_color="#dc143c", button_hover_color="#630a0a")
        self.cycle_clider.place(anchor=customtkinter.N, relx=0.8, rely=0.64)
        self.cycle_clider.set(size_cycle)   


    # display value
    def size_pom_check(self, values):
        global time_pom
        self.slider_pom_check.configure(text=int(values))
        time_pom = str(int(values))

    def size_rest_check(self, values):
        global time_rest
        self.slider_rest_check.configure(text=int(values))

        if values == 10:
            time_rest = str(int(values))
        else:
            time_rest = "0" + str(int(values))

    def size_longrest_check(self, values):
        global long_rest
        self.slider_longrest_check.configure(text=int(values))
        long_rest = str(int(values))

    def size_cycle_check(self, values):
        global size_cycle
        self.pomcycle_check.configure(text=int(values))
        size_cycle = int(values)
    
    def save_values(self):
        app_conf["time_rest"] = time_rest
        app_conf["time_pom"] = time_pom
        app_conf["long_rest"] = long_rest
        app_conf["size_cicle"] = size_cycle

        with open("config/configur.json", "w") as f:
            json.dump(app_conf, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    app = App()
    app.mainloop()
