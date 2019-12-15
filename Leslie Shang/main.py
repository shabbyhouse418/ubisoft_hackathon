import recommdation
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time

class FileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        recommdation.run(r'/Users/michaeltan/Library/Application Support/DefaultCompany/TestGame/data')

if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    filePath = r'/Users/michaeltan/Library/Application Support/DefaultCompany/TestGame'
    observer.schedule(event_handler,filePath,False)
    observer.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()