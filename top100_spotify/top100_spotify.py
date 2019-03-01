import csv
import plotly.plotly as py
import plotly.graph_objs as go


class Song(object):

    def __init__(self, name, artist, danceability, energy, loudness, \
                 speechiness, acousticness, liveness, valence, tempo, duration):

        self._name = name
        self._artist = artist
        self._danceability = danceability
        self._energy = energy
        self._loudness = loudness
        self._speechiness = speechiness
        self._acousticness = acousticness
        self._liveness = liveness
        self._valence = valence
        self._tempo = tempo
        self._duration = duration

    @property
    def danceability(self):
        return self._danceability

    @property
    def energy(self):
        return self._energy

    @property
    def loudness(self):
        return self._loudness

    @property
    def speechiness(self):
        return self._speechiness

    @property
    def acousticness(self):
        return self._acousticness

    @property
    def liveness(self):
        return self._liveness

    @property
    def valence(self):
        return self._valence

    @property
    def tempo(self):
        return self._tempo

    @property
    def duration(self):
        return self._duration


    @danceability.setter
    def danceability(self, value):
        if 0 < float(value) < 1.2:
            raise ValueError("Danceability values allowed are range [0, 1.2]")
        self._danceability = value

    @energy.setter
    def energy(self, value):
        if 0 < float(value) < 1:
            raise ValueError("Energy values allowed are from [0, 1]")
        self._energy = value

    @loudness.setter
    def loudness(self, value):
        if -25 < float(value) < 0:
            raise ValueError("Loudness values allowed are from range [-25, 0]")
        self._loudness = value

    @speechiness.setter
    def speechiness(self, value):
        if 0 < float(value) < 1:
            raise ValueError("Speechiness values allowed are from range [0, 1]")
        self._speechiness = value

    @acousticness.setter
    def acousticness(self, value):
        if 0 < float(value) < 1:
            raise ValueError("Acousticness values allowed are from range [0, 1]")
        self._acousticness = value

    @liveness.setter
    def liveness(self, value):
        if 0 < float(value) < 1:
            raise ValueError("Liveness values allowed are from range [0, 1]")
        self._liveness = value

    @valence.setter
    def valence(self, value):
        if 0 < float(value) < 1:
            raise ValueError("Valence values allowed are from range [0, 1]")
        self._valence = value

    @tempo.setter
    def tempo(self, value):
        if 0 < float(value) < 300:
            raise ValueError("Tempo values allowed are from range [0, 300]")
        self._tempo = value

    @duration.setter
    def duration(self, value):
        if 1000 < float(value) < 999999:
            raise ValueError("Duration values allowed are from range [1000, 999999]")
        self._tempo = value

    def __str__(self):
        return 'Artist: ' + str(self._artist) + ' Name: ' + str(self._name)


songs = []

with open('featuresdf.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        songs.append(Song(row[1], row[2], row[3], row[4], row[6], row[7], row[8], row[11], row[12], row[13], row[14]))


for song in songs:
   print(song)

y_danceablity = []
for song in songs:
    try:
        y_danceablity.append(float(song.danceability))
    except ValueError:
        pass

y_valence = []
for song in songs:
    try:
        y_valence.append(float(song.valence))
    except ValueError:
        pass

y_duration = []
for song in songs:
    try:
        y_duration.append(float(song.duration)/1000)
    except ValueError:
        pass

y_tempo = []
for song in songs:
    try:
        y_tempo.append(float(song.tempo))
    except ValueError:
        pass


data = [go.Histogram(x=y_danceablity, name="denceability", marker=dict(color='#EB89B5'))]

#py.plot(data, filename='danceability histogram')

data = [go.Histogram(x=y_tempo, name="tempo", marker=dict(color='#EB89B5'))]

#py.plot(data, filename='tempo histogram')

data = [go.Histogram(x=y_duration, name="duration", marker=dict(color='#EB89B5'))]

#py.plot(data, filename='duration histogram')








