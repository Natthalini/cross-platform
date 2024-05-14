from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen


class Scr_2(Screen):
    def convert(self,*args):
        #self=รับค่าพารามิเตอร์
        num= int(self.ids.txt_number.text) 
        # รับค่าจาก id txt_number แปลงเป็นตัวเลข เก็บไว้ที่ตัวแปร num
        #แสดงผลที่ไหน lbl_output.text = bin (ค่าตัวแปรที่ต้องการ)
        if args[0].text=="base2": #เลือกฐาน 2 
            self.ids.lbl_output.text= bin(num)[2:] #bin คือรับค่าฐาน2
        elif  args[0].text=="base8":
            self.ids.lbl_output.text= oct(num)[2:] #bin คือรับค่าฐาน8
        elif  args[0].text=="base16":
            self.ids.lbl_output.text= hex(num)[2:] #bin คือรับค่าฐาน16
       
class Scr_1(Screen): #หน้าจอที่1
    pass

class UI(ScreenManager): #ทำหน้าที่จัดการหน้าจอต่างๆ
    pass

class convertApp(App):
    def build(self):
        return UI()
    
if __name__=="__main__":
    convertApp().run()
    