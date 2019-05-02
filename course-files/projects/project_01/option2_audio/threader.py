import threading
import psonic


class SonicPiSample(object):
    def __init__(self, controller, sample):
        self.controller = controller
        self.sample = sample

    def start(self, **kwargs):
        threading.Thread(
            target=self.__start_sample, kwargs=kwargs
        ).start()

    def __start_sample(self, **kwargs):
        with self.controller.condition:
            self.controller.condition.wait() # wait for message
        self.sample(tempo=self.controller.tempo, **kwargs)


class SonicPiLoop(object):
    def __init__(self, controller, samples):
        if not isinstance(samples, list):
            samples = [samples]
        self.current_index = 0
        self.stop_event = None
        self.controller = controller
        self.samples = samples
    
    def __start_loop(self, **kwargs):
        while not self.stop_event.is_set():
            with self.controller.condition:
                self.controller.condition.wait() # wait for message
            # print('playing...')
            sample = self.get_current_sample()
            sample(tempo=self.controller.tempo, **kwargs)

    def get_current_sample(self):
        sample = self.samples[self.current_index]
        self.current_index += 1
        if self.current_index == len(self.samples):
            self.current_index = 0
        return sample

    def is_running(self):
        return self.stop_event and not self.stop_event.is_set()

    def stop(self):
        if self.is_running():
            self.stop_event.set()
    
    def start(self, **kwargs):
        self.stop_event = threading.Event()
        threading.Thread(
            target=self.__start_loop, kwargs=kwargs
        ).start()


class SonicPiController(object):
    def __init__(self, tempo=1, riff=None):
        self.tempo=tempo
        self.riff = riff
        self.condition = threading.Condition()
        self.stop_event = threading.Event()

    def __start_controller(self, **kwargs):
        while not self.stop_event.is_set():
            with self.condition:
                # print('notify..')
                self.condition.notifyAll() # notify
            self.riff(tempo=self.tempo, **kwargs)

    def start(self, **kwargs):
        threading.Thread(
            target=self.__start_controller, kwargs=kwargs
        ).start()

    def is_running(self):
        return self.stop_event and not self.stop_event.is_set()

    def stop(self):
        if self.is_running():
            #print('controller stopped')
            self.stop_event.set()