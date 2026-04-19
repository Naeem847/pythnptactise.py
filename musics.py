import time
import sys


def print_lyrics():
    lyrics = [
        "Arz kiya hai...",
    "Dil ki baat kehne aaye hain...",
    "Mohabbat ke rang laaye hain...",
    "... (add remaining lines here)"
   ]
    
    delays =[1.0, 0.1, 1.12, 0.9, 0.8 ] 
    print("Arz kiya hy?.............:\n")
    time.sleep(1.4)
    for i, line in enumerate(lyrics):
        for char in line:
          sys.stdout.write(char)
          sys.stdout.flush() 
          time.sleep(0.1)
        print()
        time.sleep(delays[i])

print_lyrics()       
          
