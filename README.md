# Mazer
A small maze creator you can use to absolutely cripple file system races

# How to use it 
The script contains a bunch of global variables you can set
1. `mazedir` - the directory to store your maze in
2. `maze_depth` - the depth of each segment in the maze (Each directory is nested inside another)
3. `maze_link` - the path to the symlink to use
4. `maze_paths` - the number of paths to have in the maze

- The maze is traversed path by path with each being a set of nested directories
- Given a path `a/` in maze with a depth of 3, we expect the deepest folder in the path to be `a/0/1/2`
- In the deepest folder of each path is a `root` symlink which also is a path that recursively points upwards to the `mazedir` directory
- If you plan to use other symlinks in the path using the maze, lower the `maze_link` value
- `maze_depth` is set to its absolute maximum so it is advised to leave as is
- By default the maze and its link will be placed in current working directory and the link will point to the directory that the maze is contained in
- To test out whether the maze works time the symlink using the maze

```bash
./mazer.py
time ls -lLa maze_link
```

- against one using a regular symlink

```bash
ln -s . curr
time ls -lLa curr
```
- The link using the maze should take significantly longer
