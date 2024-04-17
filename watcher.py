import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os
import getdata_from_db

class Target:
    watchDir = os.getcwd()
    watchDir = 'C:\\Users\\leesc\\PycharmProjects\\Mlops-api-server\\collect_files'
    #watchDir에 감시하려는 디렉토리를 명시한다.

    def __init__(self):
        self.observer = Observer()   #observer객체를 만듦

    def run(self):
        print('Watcher is Started.')
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDir, 
                                                       recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")
            self.observer.join()

class Handler(FileSystemEventHandler):
#FileSystemEventHandler 클래스를 상속받음.
#아래 핸들러들을 오버라이드 함
    #파일, 디렉터리가 move 되거나 rename 되면 실행
    '''
    def on_moved(self, event):
        print(event)
    '''
    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        print(event)
        getdata_from_db.insert_data()
        print("Insert func completed")
    '''
    def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
        print(event)
    def on_modified(self, event): #파일, 디렉터리가 수정되면 실행
        print(event)
    '''
if __name__ == "__main__": #본 파일에서 실행될 때만 실행되도록 함
    w = Target()
    w.run()