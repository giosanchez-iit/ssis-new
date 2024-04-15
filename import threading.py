import threading
import pynput

def print_key_value():
    def on_press(key):
        try:
            print('Key pressed: {0}'.format(key.char))
        except AttributeError:
            print('Key pressed: {0}'.format(key))

    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

print('Press any key to see the key value printed continuously.')

# Start the thread that prints the key value
key_thread = threading.Thread(target=print_key_value)
key_thread.start()

# Keep the main thread running to prevent the program from exiting
while True:
    pass