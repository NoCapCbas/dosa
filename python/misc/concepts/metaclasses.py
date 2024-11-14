
class TrackerMeta(type):
    subclasses = []

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if cls.__name__ != "BaseClass":
            TrackerMeta.subclasses.append(cls)

class BaseClass(metaclass=TrackerMeta):
    pass

class SubClassOne(BaseClass):
    pass

class SubClassTwo(BaseClass):
    pass

print("Tracked subclasses:", TrackerMeta.subclasses)
