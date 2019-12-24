from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
Config.set('graphics', 'resizable', '1')


class ManyApp(App):
    def build(self):

        #---------------Главная сетка--------------
        bl = BoxLayout(
            orientation = 'vertical', 
            padding = [50]
        )
        bl2 = BoxLayout(
            orientation = 'vertical'
        )
        gl = GridLayout(
            cols = 2
        )
        bl3 = BoxLayout(
            orientation = 'vertical'
        )
        bl4 = BoxLayout(
            orientation = 'vertical'
        )
        #---------------Главная сетка--------------

        #----------Количество пользователей--------
        persons_text = Label(
            text="Количество кушающих:"
        )
        self.persons = Label(
            text = "2",
            size_hint = [1/8, 1],

        )
        persons_slider = Slider(
            min = 2, 
            max = 8,
            step = 1, 
            value = 2,
        )
        def slider_change(instance, value):
            self.persons.text = str(value)
        persons_slider.bind(
            value = slider_change
            )
        #----------Количество пользователей--------

        #---------------Сумма счета----------------
        sum_lbl = Label(
            text = "Сумма счета:"
        )
        self.sum_form = TextInput(

        )
        #---------------Сумма счета----------------

        #----------------Результат-----------------
        butt = Button(
            text = "Подсчитать",
            on_press = self.s4et
        )
        self.itog = Label(
            text = "Каждый должен заплатить по:"
        )
        #----------------Результат-----------------

        #---------------Инструкция-----------------
        ins_but = Button(
            text = "Инструкция",
            on_press = self.ins,
        )

        self.ins_lbl = Label(size_hint = [1, 2])
        
        #---------------Инструкция-----------------

        bl.add_widget(Label(
            text = "Распределитель счета в ресторане",
            font_size = 18,
            max_lines = 2
        ))

        bl.add_widget(bl2)
        bl2.add_widget(persons_text)
        bl2.add_widget(gl)
        gl.add_widget(persons_slider)
        gl.add_widget(self.persons)

        bl.add_widget(bl3)
        bl3.add_widget(sum_lbl)
        bl3.add_widget(self.sum_form)

        bl.add_widget(bl4)
        bl4.add_widget(self.itog)
        bl4.add_widget(butt)

        bl.add_widget(ins_but)
        bl.add_widget(self.ins_lbl)

        return bl    

    def s4et(self, instance):
        self.itog.text = "Каждый должен заплатить по: " + str(float(self.sum_form.text) / float(self.persons.text)) + " у.е."
    
    def ins(self, instance):
        self.ins_lbl.text = "1. С помощью слайдера, укажите количество\nперсон, на которых будем делить счет.\n2. В поле 'Сумма счета:' введите сумму\nсчета, который вам принес официант.\n3. Нажмите кнопку 'Подсчитать' и в поле\nнад кнопкой появиться результат."

if __name__ == "__main__":
    ManyApp().run()
