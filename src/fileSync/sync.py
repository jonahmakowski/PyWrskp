import os
import shutil
import time
from datetime import datetime

pid = os.getpid()
print(f"PID of the current process: {pid}")

not_sync = ['/.obsidian', '/.trash', '.DS_Store']


def in_exclude(file):
    for exclusion in not_sync:
        if exclusion in file:
            return False
    return True


def sync_folders(folder1, folder2, prev_folder1, prev_folder2):
    """
    Synchronizes the contents of two folders in both directions.

    Args:
        folder1 (str): Path to the first folder.
        folder2 (str): Path to the second folder.
        prev_folder1 (list): List of files previously synced in folder 1.
        prev_folder2 (list): List of files previously synced in folder 2.
    """
    # Sync from folder1 to folder2
    sync_from_to(folder1, folder2, prev_folder2)

    # Sync from folder2 to folder1
    sync_from_to(folder2, folder1, prev_folder1)

    return folder1_last, folder2_last


def sync_from_to(source, destination, before_dest):
    """
    Synchronizes the contents of a source folder to a destination folder.

    Args:
        source (str): Path to the source folder.
        destination (str): Path to the destination folder.
        before_dest (list): List of files previously synced.
    """
    for root, dirs, files in os.walk(source):
        for file in files:
            src_path = os.path.join(root, file)
            dst_path = os.path.join(destination, os.path.relpath(src_path, source))
            print('\t\tPotentially Syncing {} to {}'.format(src_path, dst_path))
            if in_exclude(src_path):
                # Create the destination directory if it doesn't exist
                dst_dir = os.path.dirname(dst_path)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)

                try:
                    # Copy the file if it doesn't exist or is newer in the source
                    if not os.path.exists(dst_path):
                        if dst_path not in before_dest:
                            shutil.copy2(src_path, dst_path)
                            print(f"Copied: {src_path} -> {dst_path}")
                        else:
                            os.remove(src_path)
                            print(f"Removed: {src_path}")
                    elif os.path.getmtime(src_path) > os.path.getmtime(dst_path):
                        shutil.copy2(src_path, dst_path)
                        print(f"Copied: {src_path} -> {dst_path}")
                except OSError as e:
                    print(f"Error copying {src_path}: {e}")
                    continue


def get_current(folder):
    """Returns a list of all files in a directory, including those in subdirectories."""
    result = []
    for root, _, files in os.walk(folder):
        result.extend([os.path.join(root, file) for file in files])
    return result


if __name__ == "__main__":
    folder1 = "/Users/jonahmakowski/Desktop/Obsidian"
    #folder1 = "/Users/jonahmakowski/Documents/Obsidian Synology-iCloud Sync/Notes"
    folder2 = "/Users/jonahmakowski/Library/Mobile Documents/iCloud~md~obsidian/Documents/Notes"
    while True:
        folder1_last = get_current(folder1)
        folder2_last = get_current(folder2)
        time.sleep(10)
        sync_folders(folder1, folder2, folder1_last, folder2_last)
        print('Completed File Sync at {}'.format(datetime.now()))
