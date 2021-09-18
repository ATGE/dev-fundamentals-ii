import os

class UnixFS:

    @staticmethod
    def rm(filename):
        os.remove(filename)


def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')

import tarfile

def test_tar_mock(mocker):
    def mock_init(*args, **kwargs):
        pass
    mocker.patch(
        "tarfile.open"
    ).return_value.__enter__.return_value.extractall = mock_init
    with tarfile.open("test.tar", "r") as tar:
        tar.extractall("")