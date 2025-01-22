import os
import subprocess

def git_pull(repo_path):
    if os.path.isdir(os.path.expanduser(repo_path)):
        try:
            subprocess.run(['git', '-C', os.path.expanduser(repo_path), 'pull'], check=True)
            print(f'Succesfully pulled updates in {repo_path}')
        except subprocess.CalledProcessError as e:
            print(f'Error pulling updates in {repo_path}: {e}')
    else:
        print(f'Error: {repo_path} is not a valid directory')

repository_path = '~/Desktop/Tesi/code/continual_drive_learn/'
git_pull(repository_path)
