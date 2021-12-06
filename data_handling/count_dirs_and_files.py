import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    dirs, files = 0, 0

    for _, directories, filenames in os.walk(directory):
        dirs += len(directories)
        files += len(filenames)

    return dirs, files