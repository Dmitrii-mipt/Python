import tkinter as tk
from info import Info


class Clicker:
    def __init__(self, parent):
        self.parent = parent
        self.additional_buttons = {}
        self.info = {}
        self.current_clicks = 0
        self.button = tk.Button(parent, text='Click the button!', width=25, height=7, bg='yellow', fg='red', relief=tk.RAISED, command=self.inc)
        self.button.grid(row=0, column=2)
        self.info['auto clicker'] = Info('auto clicker', 15, per_second=1)
        self.info['clicker'] = Info('clicker', 10, quantity=1)
        self.info['multiply clicker'] = Info('multiply clicker', 30, quantity=1)
        self.additional_buttons['clicker'] = tk.Button(parent, text='Plus one click' + '\n Count per click: %d' % self.info['clicker'].quantity +
            '\n Purchase price: %d' % self.info['clicker'].cost, command=lambda: self.purchase('clicker'))
        self.additional_buttons['auto clicker'] = tk.Button(parent, text='Auto clicks plus one' + '\n Count per second: %d' % self.info['auto clicker'].quantity +
            '\n Purchase price: %d' % self.info['auto clicker'].cost, command=lambda: self.purchase('auto clicker'))
        self.additional_buttons['multiply clicker'] = tk.Button(parent, text='Multiply by two clicks' + '\n Count per click: %d' % self.info['multiply clicker'].quantity +
        '\n Purchase price: %d' % self.info['multiply clicker'].cost, command=lambda: self.purchase('multiply clicker'))
        self.current_click_label = tk.Label(parent, text='Count of clicks: 0')
        self.current_click_label.grid(row=1, column=2)
        for name in self.info:
            if name == 'auto clicker':
                column = 3
                row = 1
            elif name == 'clicker':
                column = 1
                row = 1
            elif name == 'multiply clicker':
                row = 2
                column = 2
            self.additional_buttons[name].grid(row=row, column=column)
        self.update()

    def inc(self):
        self.current_clicks += self.info['clicker'].quantity
        self.current_click_label.config(text='Count of clicks: %d' % self.current_clicks)
        self.button.config(bg='yellow', fg='red')

    def update(self):
        for info in self.info.values():
            self.current_clicks += info.per_second * info.quantity
        self.current_click_label.config(text='Count of clicks: %d' % self.current_clicks)
        self.parent.after(1000, self.update)

    def purchase(self, name):
        if self.current_clicks >= self.info[name].cost:
            self.current_clicks -= self.info[name].cost
            self.info[name].cost *= 1.5
            self.current_click_label.config(text='%d' % self.current_clicks)
            if name == 'clicker':
                self.info[name].quantity += 1
                self.info['multiply clicker'].quantity = self.info[name].quantity
                self.additional_buttons[name].config(text='Plus one click' + '\n Count per click: %d' % self.info[name].quantity +
                                                   '\n Purchase price: %d' % self.info[name].cost)
                self.additional_buttons['multiply clicker'].config(text='Multiply by two clicks' + '\n Count per click: %d' % self.info['multiply clicker'].quantity +
                                                                   '\n Purchase price: %d' % self.info['multiply clicker'].cost)
            elif name == 'auto clicker':
                self.info[name].quantity += 1
                self.additional_buttons[name].config(text='Auto clicks plus one' + '\n Count per second: %d' % self.info[name].quantity +
                                                     '\n Purchase price: %d' % self.info[name].cost)
            elif name == 'multiply clicker':
                self.info[name].quantity *= 2
                self.info['clicker'].quantity = self.info[name].quantity
                self.info['clicker'].quantity = self.info[name].quantity
                self.additional_buttons[name].config(text='Multiply by two clicks' + '\n Count per click: %d' % self.info[name].quantity +
                                                     '\n Purchase price: %d' % self.info[name].cost)
                self.additional_buttons['clicker'].config(text='Plus one click' + '\n Count per click: %d' % self.info['clicker'].quantity +
                                                          '\n Purchase price: %d' % self.info['clicker'].cost)
            self.button.config(bg='yellow', fg='red')

