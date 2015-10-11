"""
This module contains functions for downloading and verifying data from
the internet.
"""

def download_data(url):
    """
    Download and save data from a url.

    Parameters
    ----------
    url : string
        The full url pointing to the data to be downloaded

    Returns
    -------
    data : str
         Return the data that results from reading the downloaded info, e.g.
         f.read() where f is the handle to the data buffer.

    Hint
    ----
    Consider the urllib2 or wget python modules
    """
    return NotImplemented

def save_data(data, output_filename):
    """
    Save data to file.

    If the file already exists, the function will not save the data and return
    1

    Parameters
    ----------
    data : str
         String containing the data you wish to write out to a file

    output_filename : str
         Path (full or relative) to the file you will save the data into.

    Returns
    -------
    out : int
        Return 0 if the data was saved successfully. Return 1 if the file 
        already exists.

    Hint
    ----
    Check out the os module for determining whether a file exists already.
    """
    return NotImplemented

def verify_data(data, known_checksum):
    """
    This function verifies the data by comparing it to the known sha1 hash for
    the given data.

    Parameters
    ----------
    data : str
         The data to be verified

    known_checksum : str
         The sha1 hash with which to compare the result of hashing data

    Returns
    -------
    out : bool
        Return True if the hashes match, False otherwise

    Hint
    ----
    Check out the hashlib module
    """
    return NotImplemented
        


