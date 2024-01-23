from winotify import Notification, audio
import os


icon_pom = os.path.realpath("media/pomodor.ico") 

def stop_pom_message():
    toast = Notification(app_id="Pomodoro", title="Start break", msg="Timer has expired",
                         duration="short", icon=icon_pom)
    toast.set_audio(audio.Mail, loop=False)

    toast.show()


def start_longrest():
    toastlong = Notification(app_id="Pomodoro", title="Start long break", msg="Timer has expired",
                             duration="short", icon=icon_pom)
    toastlong.set_audio(audio.Mail, loop=False)

    toastlong.show()


def stop_rest_message():
    rest_toast = Notification(app_id="Pomodoro", title="Vacation is over", msg="Start a tomato cycle",
                              duration="short", icon=icon_pom)

    rest_toast.set_audio(audio.Mail, loop=False)

    rest_toast.show()

if __name__ == "__main__":
    stop_pom_message()