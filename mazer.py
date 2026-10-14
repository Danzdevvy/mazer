#!/bin/python
import os
import string
import shutil

mazedir = "maze"
maze_depth = 1364 
maze_link = "../maze_link"
maze_paths = 19

print(f'[+] Making maze in {os.path.abspath(mazedir)}')
print()

if os.path.exists(mazedir):
    shutil.rmtree(mazedir)

os.mkdir(mazedir)
maze = mazedir

for i in range(maze_paths):
    maze += f'/{i}_end'
    maze_seg = f"{i}/"
    os.mkdir(f'{mazedir}/{maze_seg}')
    wayback = '../'
    for n in range(maze_depth):
       maze_seg += f"{str(1)}/"
       wayback = '../' + wayback
       os.mkdir(f'{mazedir}/{maze_seg}')

    maze_seg += f'root'
    os.symlink(wayback, f'{mazedir}/{maze_seg}', target_is_directory=True)
    os.symlink(maze_seg, f'{mazedir}/{i}_end', target_is_directory=False)
    print(f'[+] Segment {i} done')

print()
maze += '/..'
if os.path.lexists(maze_link):
    print("[+] Removed original link")
    os.remove(maze_link)

os.symlink(os.path.abspath(f'{mazedir}/../')+f"/{maze}", maze_link, target_is_directory=True)
print('[+] Maze done')
print(f'[+] {os.path.abspath(maze_link)} is a symlink to the current directory through the maze thus slows down resolution')
