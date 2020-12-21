#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson06
# Unit test support for Mailroom Part 4 (longsa_utils.py)
# Steve Long 2020-11-04 | v4
#
# Requirements:
# =============
#
#   Internal: Separate utility functions from unit testing.
#
# Assumptions:
# ============
#
#   It's OK to create a separate module.
#
# Implementation:
# ===============
#
#   Import into test_mailroom4.py.
#
# Dependencies:
# =============
#
#   None
#
# Script Usage:
# =============
#
#   Call individual functions from module.
#
# Issues:
# =======
#
#   None.
#
# History:
# ========
# 000/2020-11-04/sal/Created and completed.
#
# =============================================================================

import pathlib


def purge_file(path):
    """
    Delete document or folder and all its content.
    Entry: A Path
    Exit: Contents of folder deleted. Returns True if successful.
    Throws: TypeError, FileExistsError, NotADirectoryError, FileNotFoundError
    """
    success = False
    if (isinstance(path, pathlib.PurePath)):
        if (path.exists()):
            if (path.is_dir()):
                file_paths = [fp for fp in path.iterdir()]
                success = True
                if (len(file_paths) > 0):
                    success = True
                    for fp in file_paths:
                        success = success and purge_file(fp)
                if (success):
                    try:
                        print("removing folder {}".format(str(path.name)))
                        path.rmdir()
                    except (FileNotFoundError, OSError) as ex:
                        success = False
                        raise(ex)
            elif (path.is_file()):
                try:
                    print("removing document {}".format(str(path.name)))
                    path.unlink()
                    success = True
                except FileNotFoundError as ex:
                    success = False
                    raise(ex)
            else:
                print("{} is neither a document nor a folder"
                      .format(str(path.name)))
                success = True
        else:
            raise(FileExistsError("{} does not exist".format(path)))
    else:
        success = False
        raise(TypeError("{} is not a Path".format(path)))
    return success


def purge_folder_content(path):
    """
    Delete contents of a folder.
    Entry: A Path
    Exit: Contents of folder deleted. Returns True if successful.
    Throws: TypeError, FileExistsError, NotADirectoryError, FileNotFoundError
    """
    success = False
    if (isinstance(path, pathlib.PurePath)):
        if (path.exists()):
            if (path.is_dir()):
                file_paths = [fp for fp in path.iterdir()]
                success = True
                if (len(file_paths) > 0):
                    success = True
                    for fp in file_paths:
                        success = success and purge_file(fp)
            else:
                success = False
                raise(NotADirectoryError("{} not a folder".format(path)))
        else:
            success = False
            raise(FileExistsError("{} does not exist".format(path)))
    else:
        success = False
        raise(TypeError("{} is not a Path".format(path)))
    return success
