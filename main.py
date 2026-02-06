from pydub import AudioSegment
from mutagen.flac import FLAC
from mutagen.id3 import ID3
from mutagen.id3 import APIC
from pathlib import Path
import os

    #TO DO
#ignore non-flac files
#remember inputs with a  text file or something
#optimization

def main():
    inputPath = input("input folder? ")
    outputPath = input("output folder? ")
    print("files and directories may be processed out of order...")
    for artistFolder in Path(inputPath).iterdir():
        if not os.path.exists(f"{outputPath}{os.sep}{artistFolder.name}"):
            os.mkdir(f"{outputPath}{os.sep}{artistFolder.name}")
            print(f"created directrory {outputPath}{os.sep}{artistFolder.name}")
        for albumFolder in artistFolder.iterdir():
            if not os.path.exists(f"{outputPath}{os.sep}{artistFolder.name}{os.sep}{albumFolder.name}"):
                os.mkdir(f"{outputPath}{os.sep}{artistFolder.name}{os.sep}{albumFolder.name}")
                print(f"created directory {outputPath}{os.sep}{artistFolder.name}{os.sep}{albumFolder.name}")
            for song in albumFolder.iterdir():
                if not os.path.exists(f"{outputPath}{os.sep}{artistFolder.name}{os.sep}{albumFolder.name}{os.sep}{song.stem}.mp3"):
                    print(f"processing {song}")
                    out = (f"{outputPath}{os.sep}{artistFolder.name}{os.sep}{albumFolder.name}{os.sep}{song.stem}.mp3")
                    convert(song, out)
                    print(out)
    print("all done :3")


def convert(songIn, songOut):
    song = AudioSegment.from_file(songIn) #.flac object for AudioSegment
    rawData = FLAC(songIn) #.flac object for mutagen
    albumArt = rawData.pictures[0] #rips album art

    data = { #rips metadata and stores it in this dictionary
        "title" : rawData.get("title", [''])[0],
        "artist" : rawData.get("artist", [''])[0],
        "album" : rawData.get("album", [''])[0],
        "date" : rawData.get("date", [''])[0],
        "track" : rawData.get("tracknumber", [''])[0],
    }
    song.export(f"{songOut}", format="mp3", bitrate="320k", tags=data) #export song with metadata tags
    art = ID3(f"{songOut}")
    art.add(APIC(
        encoding=3,
        mime=albumArt.mime,
        type=3,
        desc="Cover",
        data=albumArt.data
    ))
    art.save()

main()
