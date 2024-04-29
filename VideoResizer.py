import subprocess as sp
import re
import tkinter as tk
import time
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

print("Welcome to the Aspyct Resizer.\nThis program will automatically crop the pesky black bars out of videos.\nBefore we begin, please ensure that you have ffmpeg installed and added to the PATH variable.\nWould you like to proceed [y/n]: ")
choice = input("")

if choice == 'y' or choice == 'Y':
    in_video_file = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
    out_video_file = f'{in_video_file}_cropped.mp4'
    # ffmpeg -hide_banner -i testvideo.mp4 -vf cropdetect=skip=0 -t 1 -f null
    cropdetect_output = sp.run(['ffmpeg', '-hide_banner', '-i', in_video_file, '-vf', 'cropdetect=skip=0', '-t', '1', '-f', 'null', 'pipe:'], stderr=sp.PIPE, universal_newlines=True).stderr

    crop_str = re.search('crop=.*', cropdetect_output).group(0)  # Find the first match of "crop=", and return all characters from "crop=" up to new line.

    sp.run(['ffmpeg', '-hide_banner', '-i', in_video_file, '-vf', crop_str+',setsar=1', out_video_file])
    print(f"\n\nCropping completed successfully! There should be a file title \"{out_video_file}\" in the same directory as the input file.")
    print("Exiting program now")
    time.sleep(8)
    exit()
elif choice == 'n' or choice == 'N':
    print("why are you here then?????")
    print("Closing the program")
    time.sleep(4)
    exit()
else:
    print("Invalid choice. Program will now close.")
    time.sleep(4)
    exit()



