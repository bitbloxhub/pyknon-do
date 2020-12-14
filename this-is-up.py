import time
from pyknon.genmidi import Midi
from pyknon.music import Rest, Note, NoteSeq

music = []

for x in range(0,3,1):
    music.append(Note(x))

music.append(Rest())

for x in range(2,-1,-1):
    music.append(Note(x))

music.append(Rest())

music.append(Note(0))
music.append(Note(1))
music.append(Note(2))
music.append(Note(1))
music.append(Note(0))


print("the song is of length {length}".format(length=len(music)))

notes = NoteSeq(music)
print("notes are {notes}".format(notes=notes))
midi = Midi(tempo=90)
midi.seq_notes(notes)
midi.write("./pyknon-do-music/this-is-up-{ts}.mid".format(ts=time.time()))
