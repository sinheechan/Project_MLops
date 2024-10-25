# collect_files을 감시하면서 12시마다 자료 업데이트
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os
import getdata_from_db


class Target:
    watchDir = os.getcwd()
    watchDir = 'C:/sinheechan.github.io-master/Project_MLops/collect_files' # watcher.py 감시 디렉토리

    def __init__(self):
        self.observer = Observer()

    def run(self):
        print('Watcher가 정상 실행되었습니다.')
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDir, 
                               recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error가 발생하여 Stop을 실행합니다.")
            self.observer.join()

class Handler(FileSystemEventHandler):


    # Case 1.파일이 움직일 때 실행
    '''
    def on_moved(self, event): 
        print(event)
    
    '''
    # Case 2.파일, 디렉터리가 생성되면 실행

    def on_created(self, event):
        print(event)
        getdata_from_db.insert_data()
        print("Insert가 완료되었습니다.")

    # Case 3.파일, 디렉터리가 삭제되면 실행 
       
    '''
    def on_deleted(self, event):
        print(event)
    '''
    # Case 4. 파일,디렉터리가 수정되면 실행

    '''
    def on_modified(self, event):
        print(event)
    '''

if __name__ == "__main__":
    w = Target()
    w.run()