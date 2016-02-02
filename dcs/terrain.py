# terrain module


class Terrain:
    def __init__(self, name: str):
        self.name = name
        self.center = {"lat": 0, "long": 0}  # WGS84 decimal
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}
        self.airports = {} # type dict[str,Airport]


class Caucasus(Terrain):
    def __init__(self):
        super(Caucasus, self).__init__("Caucasus")
        # caucasus center MGRS
        # 36TWQ9949898109
        self.center = {"lat": 45.12945, "long": 34.26527}
        self.bullseye_blue = {"x": -291014, "y": 617414}
        self.bullseye_red = {"x": 371700, "y": 11557}
        self.airports["Kobuleti"] = Airport(13, "Kobuleti", 133.0, {"x": -293933, "y": 540000}, "67X", 111.5)
        self.airports["Batumi"] = Airport(11, "Batumi", 131.0, {"x": -293933, "y": 540000}, "16X", 110.3)


class Nevada(Terrain):
    def __init__(self):
        super(Nevada, self).__init__("Nevada")
        # nttr center MGRS
        # 11SPE9400410022
        self.center = {"lat": 39.81806, "long": -114.73333}
        self.bullseye_blue = {"x": -409931.344, "y": -14024.097}
        self.bullseye_red = {"x": -288293.969, "y": -88022.641}


class Airport:
    def __init__(self, _id: int, name: str, frequency: float, pos: dict, tacan: str =None, ils=None):
        self.id = _id
        self.name = name
        self.tacan = tacan
        self.ils = ils
        self.frequency = frequency
        self.position = pos
