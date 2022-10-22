import threading
from time import sleep

class CheckBB():
    def __init__(self):
        self.tag = 1
        self.check_aa = None

    def start(self):
        check_aa = CheckAA(self)
        the = threading.Thread(target=check_aa.test)
        the.start()
        for i in range(40):
            print(i)
            check_aa.aa_tag = i
            sleep(1)

        print(self.check_aa)

    def clear(self):
        self.check_aa = None
        


class CheckAA():
    def __init__(self,parent):
        self.aa_tag = 1
        self.parent = parent

    def test(self):
        print("test 111")
        for i in range(30):
            print("test 222")
            print("222 aa_tag : ",self.aa_tag)
            sleep(1)
            self.parent.clear()
        


if __name__ == '__main__':
    check_bb = CheckBB()
    check_bb.start()