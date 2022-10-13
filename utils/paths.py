from pathlib import Path

path = Path()
for file in path.glob('*'):
    print(file)

path = Path('bc')
path.mkdir()
path.rmdir()

