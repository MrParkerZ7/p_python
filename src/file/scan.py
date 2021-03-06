import os
from tkinter import N

from ..module import *


def scan_path(path: str, arrow, logger=print) -> None:
    logger(f'- scaning path={path}')
    listDir = os.listdir(path)
    for dir in listDir:
        subPath = f"{path}\\{dir}"
        arrow(subPath)
        if os.path.isdir(subPath):
            scan_path(subPath, arrow, logger=lambda msg: logger('  ' + msg))


def scan_file(path: str, arrow, logger=print) -> None:
    def exc_file(path):
        if check_is_path_file(path):
            arrow(path)
    scan_path(path, exc_file, logger)


def scan_file_type(path: str, arrow, fileType: str, logger=print) -> None:
    def exc_file(path):
        if check_is_path_file(path) and check_path_file_type(path, fileType):
            arrow(path)
    scan_path(path, exc_file, logger)


def scan_dir(path: str, arrow, logger=print) -> None:
    def check_path_is_dir(path):
        if check_is_path_dir(path):
            arrow(path)
    scan_path(path, check_path_is_dir, logger)


def scan_remove(
        path: str,
        arrowReturnBool,
        non_exist_ok: bool = True,
        logger=print) -> None:

    def check_then_remove(path):
        if arrowReturnBool(path):
            remove_auto(path, non_exist_ok)

    scan_path(path, check_then_remove, logger)


def scan_remove_dir_file(
        path: str,
        dirNames: Iterable[str] = [],
        fileNames: Iterable[str] = [],
        fileTypes: Iterable[str] = [],
        non_exist_ok: bool = True,
        logger=print) -> None:

    def check_then_remove(path):
        sourceName: str = get_source_name_by_path(path)
        if(check_is_path_dir(path)):
            for dirName in dirNames:
                if(dirName == sourceName):
                    remove_auto(path, non_exist_ok)
                    return
        else:
            for typeName in fileTypes:
                if(sourceName.endswith(typeName)):
                    remove_auto(path, non_exist_ok)
                    return
            for fileName in fileNames:
                if(fileName == sourceName):
                    remove_auto(path, non_exist_ok)
                    return

    scan_path(path, check_then_remove, logger)
