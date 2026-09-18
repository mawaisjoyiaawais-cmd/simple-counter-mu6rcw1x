import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty

class CounterApp(App):
    # counter property jiska istemal hum apne app mein karenge
    counter = NumericProperty(0)

    def build(self):
        """UI ko banata hai aur widgets ko arrange karta hai."""
        # Main layout, vertical orientation mein
        main_layout = BoxLayout(orientation='vertical')

        # Counter dikhane ke liye label
        # Iska text 'on_counter' method se update hoga
        self.counter_label = Label(
            text=str(self.counter),
            font_size='150sp',
            size_hint=(1, 0.7)
        )
        main_layout.add_widget(self.counter_label)

        # Buttons ke liye horizontal layout
        button_layout = BoxLayout(size_hint=(1, 0.3))

        # Minus button
        minus_button = Button(
            text='-',
            font_size='50sp'
        )
        minus_button.bind(on_press=self.decrement)
        button_layout.add_widget(minus_button)

        # Plus button
        plus_button = Button(
            text='+',
            font_size='50sp'
        )
        plus_button.bind(on_press=self.increment)
        button_layout.add_widget(plus_button)

        # Reset button
        reset_button = Button(
            text='रीसेट',
            font_size='40sp'
        )
        reset_button.bind(on_press=self.reset)
        button_layout.add_widget(reset_button)

        main_layout.add_widget(button_layout)

        return main_layout

    def on_start(self):
        """App shuru hone par counter ki value load karta hai."""
        self.load_counter()

    def on_stop(self):
        """App band hone par counter ki value save karta hai."""
        self.save_counter()

    def on_counter(self, instance, value):
        """Jab bhi counter property badalti hai, label ka text update karta hai."""
        self.counter_label.text = str(int(value))

    def increment(self, instance):
        """Counter ko 1 se badhata hai."""
        self.counter += 1

    def decrement(self, instance):
        """Counter ko 1 se ghatata hai."""
        self.counter -= 1

    def reset(self, instance):
        """Counter ko 0 par reset karta hai."""
        self.counter = 0

    @property
    def data_filepath(self):
        """Data file ka path return karta hai."""
        # user_data_dir har platform (Android, iOS, Windows, etc.) par ek safe directory deta hai
        return os.path.join(self.user_data_dir, 'counter_data.json')

    def load_counter(self):
        """JSON file se counter ki value load karta hai."""
        try:
            if os.path.exists(self.data_filepath):
                with open(self.data_filepath, 'r') as f:
                    data = json.load(f)
                    self.counter = data.get('counter', 0)
        except Exception as e:
            print(f"Error loading data: {e}")
            self.counter = 0

    def save_counter(self):
        """Counter ki value ko JSON file mein save karta hai."""
        try:
            with open(self.data_filepath, 'w') as f:
                json.dump({'counter': self.counter}, f)
        except Exception as e:
            print(f"Error saving data: {e}")

if __name__ == '__main__':
    CounterApp().run()
