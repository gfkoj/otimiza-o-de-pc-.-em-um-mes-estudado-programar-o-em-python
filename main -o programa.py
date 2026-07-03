import subprocess
import time
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        " ".join(sys.argv),
        None,
        1
    )
    sys.exit()


def run_command(cmd):
    print(f"\nExecutando: {cmd}") #abra o cmd e começa os comando do wiwndows
    subprocess.run(cmd, shell=True)


def maintenance():
    comandos = [
        "cleanmgr",#limapaz do systeam
        "sfc /scannow",#limpaz systeam
        "dism /online /cleanup-image /restorehealth",# comando de limpazar e mas
        "ipconfig /flushdns"#limpiza de dns
    ]

    for cmd in comandos:
        run_command(cmd)# ele run da os comando do cmd
    time.sleep(2)

def main():
    if not is_admin():
        print("Reiniciando como administrador...")
        run_as_admin()

    print("Iniciando manutenção...")
    time.sleep(2)

    print("\nFinalizado.")

if __name__ == "__main__":
    main()