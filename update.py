# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import time

from urllib.request import urlretrieve
from urllib.error import URLError

from zipfile import ZipFile
from shutil import copyfile

folder_to_install = "C:\\aeron"
folder_to_download = "C:\\aeron\\downloads"


def check_folder(_path):
    try:
        if not os.path.isdir(_path):
            os.makedirs(_path)
    except Exception:
        pass


def log(msg, *params):
    print(msg, *params)


def progress(downloaded, block_size, total_size):
    global download_size
    download_size = total_size
    completed = int(downloaded / (total_size // block_size) * 100)
    sys.stdout.write("\r|" + "█" * completed + " " *
                     (100 - completed) + "|{}%".format(completed))


def download(url, filename):
    start = time.time()
    try:
        urlretrieve(url, filename, progress)
    except URLError:
        sys.stderr.write("The URL is invalid.\n")
        exit(0)
    except Exception as e:
        sys.stderr.write("An error occured\n")
        sys.stderr.write(type(e), e)
        exit(0)
    end = time.time()
    print("\n", end="")
    time_taken = end - start
    download_speed = round(download_size / (time_taken * 1024), 2)
    if download_speed >= 1024:
        sys.stdout.write("Downloaded in " + str(round(time_taken, 2)) +
                         "s (" + str(download_speed / 1024) + " MB/s)" + "\n")
    if download_speed < 1024:
        sys.stdout.write("Downloaded in " + str(round(time_taken, 2)) +
                         "s (" + str(download_speed) + " kB/s)" + "\n")
    if download_speed < 1:
        sys.stdout.write("Downloaded in " + str(round(time_taken, 2)) +
                         "s (" + str(download_speed * 1024) + " B/s)" + "\n")


def install_project_git_typescript(name_project: str, create_service=False):
    try:
        log(f"Instalando {name_project}")

        folderProject = f'{folder_to_install}\\{name_project}'
        if os.path.exists(folderProject) is True:
            command_download = f'cd "{folderProject}" && git reset --hard && git pull'
            print(command_download)
            os.system(command_download)

            command_install_build = f'cd "{folderProject}" && npm i --legacy-peer-deps && npm run build'
            print(command_install_build)
            os.system(command_install_build)

            log(f"{name_project} instalado com sucesso!")
        else:
            log(f"Projeto {name_project} já instalado")
    except Exception as e:
        log(e)


def executeCommandPowershellAsAdm(command):
    try:
        commandExecute = f'powershell -Command "Start-Process powershell -ArgumentList \'{command}\' -Verb RunAs"'
        log(commandExecute)
        subprocess.Popen(commandExecute, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
        log('Comando executado')
    except Exception as e:
        log(e)


def outros():
    pass


if __name__ == "__main__":
    try:
        check_folder(folder_to_install)
        check_folder(folder_to_download)
        # instalar_python()

        # log("Instalando Poetry")
        # executeCommandPowershellAsAdm(
        #    '(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -')

        install_project_git_typescript("upload-certificates")
        install_project_git_typescript("webscraping-nfe-nfce-go-v2")
        install_project_git_typescript("webscraping-nfse-goiania-v2")

        log("Setando ExecutionPolicy")
        executeCommandPowershellAsAdm(
            "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force")

        log('Processo finalizado, aperte qualquer tecla pra sair')

        os.system('pause > nul')
    except Exception:
        os.system('pause > nul')
