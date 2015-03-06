# -*- coding: utf-8 -*-

__author__ = 'jasonzhang'

import numbers

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class rootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(rootWidget, self).__init__(**kwargs)
        btn1 = Button(text="Hello world")
        self.add_widget(btn1)
        cb = customBtn()
        cb.bind(pressed=self.btn_pressed)
        self.add_widget(cb)
        self.add_widget(Button(text="Btn2"))

    def btn_pressed(self, instance, pos):
        print "pos: printed from root widget: {pos}".format(pos=pos)

class customBtn(Widget):
    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(customBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print "at {pos}".format(pos = pos)

class untitle(App):
    def build(self):
        return rootWidget()


if __name__ == "__main__":
    untitle().run()