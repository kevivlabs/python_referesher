from pathlib import Path
from pathlib import PurePath

print(Path.cwd())
# pay attention to the functions some of them need to be called () others not
# iterate through path
for p in Path(".devcontainer").walk():
    print(p)
# for p in Path().iterdir():
# print(p)

# print attributes
my_dir = Path("testdirectory")
my_file = Path("file1.txt")
print(f"-----{my_file.name}---------")
print(f"-----{my_dir.name}---------")

# print extension
print(my_dir.suffix)
print(my_file.suffix)

# print file name without extension

print(my_dir.stem)
print(my_file.stem)

# join file path
new_file = my_dir / "new_file.txt"
print(new_file)
new_file = my_dir.joinpath("new_file.txt")
print(new_file)

# check if something exists

print(my_dir.exists())
print(my_file.exists())
print(new_file.exists())

# check parent - relative paths
print(my_dir.parent.parent)
print(my_file.parent)
print(new_file.parent)

# check absolute path

print(my_dir.absolute())
print(my_dir.absolute().parent)
p = Path(__file__).resolve()
print(p)
p = Path(__file__).resolve().parent
print(p)

# however doesnt with with ~ for home folder

p = Path("~/.config").resolve()
print(p)
# this is the output "/workspaces/python/.devcontainer/~/.config"

p = Path("~/.config").expanduser()
print(p)
# output:
# /home/vscode/.config
p = Path.home() / "dotfiles"
print(p)
