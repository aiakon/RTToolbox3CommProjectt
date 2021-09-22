from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import NoTransition
import socket
import threading


class LoginWindow(Screen):

    def client_socket(self):
        global datalist, sm, s
        client = self.manager.get_screen('client')
        host = self.ipv4.text
        port = int(self.port.text)
        datalog = ''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(b'Hello, world')
            sm.current = "client"
            while True:
                s.sendall(b'Hello, world')
                data = s.recv(1024)
                datastr = data.decode("utf-8")
                datalist = [i.strip() for i in datastr.split("+")]
                print(datalist)
                # print(datalist[1])
                datalog = datalog + "\n" + datalist[0]

                client.ids.textinput2.text = datalog

                client.ids.textinput1.text = datalist[1]

                client.ids.prog1.value = int(datalist[2])
                client.ids.label1.text = f"%{datalist[2]}"

                client.ids.prog2.value = int(datalist[3])
                client.ids.label2.text = f"%{datalist[3]}"

                client.ids.prog3.value = int(datalist[4])
                client.ids.label3.text = f"%{datalist[4]}"

                client.ids.prog4.value = int(datalist[5])
                client.ids.label4.text = f"%{datalist[5]}"

                client.ids.prog5.value = int(datalist[6])
                client.ids.label5.text = f"%{datalist[6]}"

                client.ids.prog6.value = int(datalist[7])
                client.ids.label6.text = f"%{datalist[7]}"

                # s.sendall("data".encode('utf-8'))

                # print(datalist)
                # print('Received', repr(data))

    def make_connection(self):
        x = threading.Thread(target=self.client_socket, daemon=True)
        x.start()

    def deneme(self):
        # s.sendall(b'Hello, world')
        pass


class ClientWindow(Screen):

    def command_mode(self):
        sm.current = 'command'

    def baslat(self):
        s.sendall(b'baslat')

    def duraklat(self):
        s.sendall(b'duraklat')

    def durdur(self):
        s.sendall(b'durdur')

    def denememe(self):
        global datalist

        print(self)

        self.ids.prog1.value = int(datalist[2])
        self.ids.label1.text = f"%{datalist[2]}"

        self.ids.prog2.value = int(datalist[3])
        self.ids.label2.text = f"%{datalist[3]}"

        self.ids.prog3.value = int(datalist[4])
        self.ids.label3.text = f"%{datalist[4]}"

        self.ids.prog4.value = int(datalist[5])
        self.ids.label4.text = f"%{datalist[5]}"

        self.ids.prog5.value = int(datalist[6])
        self.ids.label5.text = f"%{datalist[6]}"

        self.ids.prog6.value = int(datalist[7])
        self.ids.label6.text = f"%{datalist[7]}"

        print(datalist)


class CommandWindow(Screen):

    def client_mode(self):
        s.sendall(b'cclient')
        sm.current = 'client'

    def master_mode(self):
        s.sendall(b'mmaster')
        sm.current = 'client'

    def j1up(self):
        s.sendall(b'J1+')

    def j1down(self):
        s.sendall(b'J1-')

    def j2up(self):
        s.sendall(b'J2+')

    def j2down(self):
        s.sendall(b'J2-')

    def j3up(self):
        s.sendall(b'J3+')

    def j3down(self):
        s.sendall(b'J3-')

    def j4up(self):
        s.sendall(b'J4+')

    def j4down(self):
        s.sendall(b'J4-')

    def j5up(self):
        s.sendall(b'J5+')

    def j5down(self):
        s.sendall(b'J5-')

    def j6up(self):
        s.sendall(b'J6+')

    def j6down(self):
        s.sendall(b'J6-')


class MyApp(App):

    def build(self):
        global sm

        Window.size = (360, 780)
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(ClientWindow(name='client'))
        sm.add_widget(CommandWindow(name='command'))
        return sm


if __name__ == '__main__':
    MyApp().run()
