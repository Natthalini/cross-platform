from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    def check_data(self):
        id_card = self.ids.id_card.text
        phone_number = self.ids.phone_number.text

        if len(id_card) == 13 and len(phone_number) == 10:
            self.ids.btn_regis.disabled = False
            self.ids.btn_regis.text = 'บันทึกข้อมูล'
        else:
            self.ids.btn_regis.disabled = True
            self.ids.btn_regis.text = 'กรุณากรอกข้อมูลให้ครบ'
            

class RegistrationApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm

if __name__ == '__main__':
    RegistrationApp().run()
