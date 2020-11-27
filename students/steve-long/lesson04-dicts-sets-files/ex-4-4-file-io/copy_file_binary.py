#!/usr/bin/env python3
# ==============================================================================
# Python210 | Fall 2020
# ------------------------------------------------------------------------------
# Lesson04
# File Exercise (copy_file_binary.py)
# Steve Long 2020-10-14 | v0
#
# Requirements:
# =============
#
# [1] Write a program which copies a file from a source, to a destination
#     (without using shutil, or the OS copy command (you are essentially
#     writing a simple version of the OS copy command)).
#
# [2] This should work for any kind of file, so you need to open the files in
#     binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for
#     binary files, you can’t use readline() – lines don’t have any meaning for
#     binary files.
#
# [3] Test it with both [a] text and [b] binary files (maybe a jpeg or
#     something of your choosing).
#
# [4] Advanced: make it work for any size file: i.e. don’t read the entire
#     contents of the file into memory at once. This should only be a few lines
#     of code :-)
#
# Implementation:
# ---------------
#
#   The implementation is much larger than is actually required, but as implied
#   in requirement [4] the section of code that actually performs the
#   read/write op is only 8 lines (and that many because of PEP8 "neatness"
#   requirements.)
#
#   [1] Function copy_file_binary
#   [2] Context read/write ops with 'rb'/'wb' option.
#   [3] Multiple use-cases. See functional test ft_copy_file_binary.
#   [4] Implemented using buffered i/o and optional read size argument.
#
#   Function names, variables, block comments, line continuation, and
#   operator spacing per PEP8 guidelines. Checked with flake8.
#
# Dependencies:
# -------------
#
#   Source data folder "source/" containing the following documents (files):
#
#       robot.jpg
#       samaritaine.jpg
#       widgets.txt
#
#   Target data folder "target/" for copying documents (files) to.
#
# Script Usage:
# -------------
#
#   ./copy_file_binary.py executes functional test ft_copy_file_binary which
#   verifies requirement[3] and verifies function arguments.
#
# Issues:
# -------
#
#   Requirement [4] was a little ambiguous.
#
# History:
# --------
# 000/2020-10-12/sal/Created.
# =============================================================================

import pathlib


def copy_file_binary(source_pathname, target_pathname,
                     allow_overwrite=False, chunk_size=2048):
    """
    copy_file_binary(<source_pathname>, <target_pathname>,
                     <allow_overwrite>, <chunk_size>)
    -------------------------------------------------------------------
    Copy a source file to a destination, optionally overwriting an
    existing file with the same name. Satisfies requirement [1].

    Entry: <source_pathname> ::= (str) A valid source file absolute
                                 path string.
           <target_pathname> ::= (str) A valid target file absolute
                                 path string.
           <allow_overwrite> ::= (bool) When True, allow replacement of
                                 an existing file at <target_pathname>.
                                 Default is False.
           <chunk_size>      ::= (int) Number of bytes to read from
                                 source file at read interval. Must be
                                 greater than zero and multiple of 64.
                                 Default is 2048.
    Exit:  Returns True if successful, False otherwise.
           For issues related to arguments, raises standard Exception
           with custom message.
    Raises: ValueError, FileExistsError, FileNotFoundError, PermissionError
    """
    success = False
    #
    # Begin argument quality assurance.
    #
    message = ""
    if (len(source_pathname) > 0):
        source_path = pathlib.Path(source_pathname)
        if (source_path.exists()):
            if (len(target_pathname) > 0):
                target_path = pathlib.Path(target_pathname)
                if (target_path.exists()):
                    if (allow_overwrite):
                        if ((chunk_size > 0) and ((chunk_size % 64) == 0)):
                            pass
                        else:
                            message \
                                = "Arg chunk_size must be > 0, multiple of 64"
                            raise ValueError(message)
                    else:
                        message = "Overwrite of file {} not allowed" \
                                  .format(target_pathname)
                        raise FileExistsError(message)
                else:
                    pass
            else:
                message = "Arg target_pathname is blank"
                raise ValueError(message)
        else:
            message = "File {} is missing".format(source_pathname)
            raise FileNotFoundError(message)
    else:
        message = "Arg source_pathname is blank"
        raise ValueError(message)
    #
    # End argument quality assurance.
    #
    # The principal functionality. Satisfies requirement [2] and [4].
    # Even without the explicit chunk_size, this technique will still read
    # entire binary files well into the gigabyte range.
    #
    try:
        with open(source_pathname, 'rb') as source_file, \
                open(target_pathname, 'wb') as target_file:
            while True:
                chunk = source_file.read(chunk_size)
                if (not chunk):
                    break
                else:
                    target_file.write(chunk)
    except PermissionError as pex:
        success = False
        raise pex
    else:
        success = True
        return success


def remove_file_no_error(pathname):
    """
    Remove a file (document) on the specified pathname.
    """
    result = False
    path = pathlib.Path(pathname)
    if (path.exists()):
        try:
            path.unlink()
        except FileNotFoundError:
            pass
        finally:
            result = (not path.exists())
    return result


def create_file_no_error(pathname):
    """
    Create a file (document) on the specified pathname.
    """
    result = False
    path = pathlib.Path(pathname)
    if (path.exists()):
        result = True
    else:
        f = open(pathname, "w+")
        f.close()
        result = path.exists()
    return result


def ft_copy_file_binary():
    """
    Test function copy_file_binary with a set of use-cases, printing the
    result for each and summarizing the results with a PASSED or FAILED
    message.
    """
    #
    # Define real and imaginary input and output paths.
    #
    valid_base_name\
        = str(pathlib.Path.cwd())
    imaginary_base_path_name\
        = "{}/{}".format(str(pathlib.Path.cwd().parent), "imaginary")
    existing_source_pathname\
        = "{}/{}".format(valid_base_name, "source/widgets.txt")
    new_target_pathname\
        = "{}/{}".format(valid_base_name, "target/frammitz.txt")
    remove_file_no_error(new_target_pathname)
    existing_target_pathname\
        = "{}/{}".format(valid_base_name, "target/widgets.txt")
    create_file_no_error(existing_target_pathname)
    imaginary_source_pathname\
        = "{}/{}".format(imaginary_base_path_name, "source/widgets.txt")
    imaginary_target_pathname\
        = "{}/{}".format(imaginary_base_path_name, "target/widgets.txt")
    invalid_pathname = ""
    small_bin_source_pathname\
        = "{}/{}".format(valid_base_name, "source/robot.jpg")
    small_bin_target_pathname\
        = "{}/{}".format(valid_base_name, "target/robot.jpg")
    remove_file_no_error(small_bin_target_pathname)

# NOTE: Originally run with movie file "Gravity.mv4" because this was the
#       biggest file available (3.22 GB). DRM rules and Git repository
#       limitations prevent this from being included with the final solution.
#       Instead, a photo of a building in Paris was substituted.

#     large_bin_source_pathname\
#         = "{}/{}".format(valid_base_name, "source/Gravity (HD).m4v")
#     large_bin_target_pathname\
#         = "{}/{}".format(valid_base_name, "target/Gravity (HD).m4v")

    large_bin_source_pathname\
        = "{}/{}".format(valid_base_name, "source/samaritaine.jpg")
    large_bin_target_pathname\
        = "{}/{}".format(valid_base_name, "target/samaritaine.jpg")

    remove_file_no_error(large_bin_target_pathname)
    #
    # Construct use-cases defined by test parameter lists consisting of
    # use-case#, list of input arguments, and expected output from function.
    #
    use_case = [[]]*10
    #
    # Satisfies: requirement [3a]
    #
    use_case[0] =\
        ["1",
         "Copy existing text file to new file",
         [existing_source_pathname, new_target_pathname, True, 2048],
         True
         ]
    use_case[1] =\
        ["2",
         "Copy existing text file to existing file, allowing overwrite",
         [existing_source_pathname, existing_target_pathname, True, 2048],
         True
         ]
    use_case[2] =\
        ["3",
         "Copy existing text file to existing file, disallowing overwrite",
         [existing_source_pathname, existing_target_pathname, False, 2048],
         False
         ]
    use_case[3] =\
        ["4",
         "Copy existing text file to non-existent directory",
         [existing_source_pathname, imaginary_target_pathname, True, 2048],
         False
         ]
    use_case[4] =\
        ["5",
         "Copy non-existent text file to non-existent directory",
         [imaginary_source_pathname, imaginary_target_pathname, True, 2048],
         False
         ]
    use_case[5] =\
        ["6",
         "Copy non-existent text file to invalid file",
         [imaginary_source_pathname, invalid_pathname, True, 2048],
         False
         ]
    use_case[6] =\
        ["7",
         "Copy invalid text file to non-existent file",
         [invalid_pathname, imaginary_target_pathname, True, 2048],
         False
         ]
    #
    # Satisfies: requirement [3b]
    #
    use_case[7] =\
        ["8",
         "Copy small binary file (95 KB)",
         [small_bin_source_pathname, small_bin_target_pathname, True, 2048],
         True
         ]
    #
    # Satisfies: requirement [4]
    #
    use_case[8] =\
        ["9",
         "Copy large binary file (2.5 MG to 3.22 GB)",
         [large_bin_source_pathname, large_bin_target_pathname, True, 2048],
         True
         ]
    use_case[9] =\
        ["10",
         "Invalid chunk size",
         [small_bin_source_pathname, small_bin_target_pathname, True, 5001],
         False
         ]
    #
    # Execute list of functional tests.
    #
    success = True
    msg = ""
    for uc in use_case:
        uc_index = uc[0]
        uc_descr = uc[1]
        uc_args = uc[2]
        uc_src = uc_args[0]
        uc_tgt = uc_args[1]
        uc_aovd = uc_args[2]
        uc_chksz = uc_args[3]
        uc_expected = uc[3]
        uc_actual = False
        try:
            uc_actual = False
            uc_actual = copy_file_binary(uc_src, uc_tgt, uc_aovd, uc_chksz)
            msg = ""
        except (ValueError, FileExistsError, FileNotFoundError,
                PermissionError) as excptn:
            msg = str(excptn)
        finally:
            ok = ((uc_actual == uc_expected) or (uc_actual is None))
            msg = "Use Case {}: {}\n  {}{}"\
                  .format(uc_index,
                          uc_descr,
                          ("OK" if ok else "FAILED"),
                          (f": {msg}" if (len(msg) > 0) else ""))
            print(msg)
            success = success and ok
    return "Functional test for copy_file_binary: {}"\
           .format(("PASSED" if success else "FAILED"))


if __name__ == "__main__":
    print(ft_copy_file_binary())
