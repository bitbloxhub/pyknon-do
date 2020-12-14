import time
from pyknon.genmidi import Midi
from pyknon.music import Rest, Note, NoteSeq

def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

numfib = 10
music = []

for x in fib_to(numfib):
    music.append(Note(x))

print("the song is of length {length}".format(length=len(music)))

notes = NoteSeq(music)
print("notes are {notes}".format(notes=notes))
midi = Midi(tempo=90)
midi.seq_notes(notes)
midi.write("./pyknon-do-music/fib-{ts}.mid".format(ts=time.time()))
