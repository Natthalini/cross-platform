from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen


class Scr_bmi(Screen):
    def cal_bmi(self):
        #ค่า  bmi = น้ำหนัก กก // (ส่วนสูง เมตร * ส่วนสูง เมตร)
        weight= float(self.ids.txt_weight.text) #self=รับค่าพารามิเตอร์
        height= float(self.ids.txt_height.text) #self=รับค่าพารามิเตอร์
        height = height/100 #ไม่รับค่าพารามิเตอร์
        bmi = weight/(height*height) #สูตรการคำนวณ
        self.ids.lbl_bmi.text=str(bmi) #self=รับค่าพารามิเตอร์ ids การอ้างอิงวิจเจ๊ต   กำหนดให้  img 
        if bmi > 35:
            self.ids.lbl_bmi.color="#990033"
            self.ids.img_bmi.source="pic/5.png"     
        elif bmi > 30:
            self.ids.lbl_bmi.color="#CC6600"
            self.ids.img_bmi.source="pic/4.png"
        elif bmi > 25:
            self.ids.lbl_bmi.color="##FFFF00"
            self.ids.img_bmi.source="pic/3.png"
        elif bmi > 25:
            self.ids.lbl_bmi.color="#66FF00"
            self.ids.img_bmi.source="pic/2.png"
        else:
            self.ids.lbl_bmi.color="#33FF33"
            self.ids.img_bmi.source="pic/1.png"

class Scr_Knowledge(Screen): #หน้าจอที่1
    pass

class UI(ScreenManager): #ทำหน้าที่จัดการหน้าจอต่างๆ
    pass
    
class bmiApp(App):
    def build(self):
        return UI()
    
if __name__=="__main__":
    bmiApp().run()