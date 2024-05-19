from rich import print
from rich.table import Table
from rich.console import Console
from os import system, getcwd, environ
import subprocess
from sys import argv

console = Console()

def desktop_environment():
    de = environ.get('XDG_CURRENT_DESKTOP')
    if de == 'ubuntu:GNOME':
        return 'GNOME :footprints: ' + run_command("gnome-shell --version | awk '{print $3}' ").strip("\n")
    elif de == 'KDE':
        return 'KDE'
    elif de == 'XFCE':
        return 'XFCE'
    else:
        return 'Unknown'

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8')


''' Get data from the system '''
user = environ.get('USER')
computer_name = run_command("hostname").strip("\n")
os_name = run_command("cat /etc/os-release | grep 'PRETTY_NAME' ").strip("\n").strip('"').strip('PRETTY_NAME="')   
#os_name = run_command("lsb_release -d | awk '{print $2, $3, $4}' ").strip("\n")
os_codename = run_command("lsb_release -c").strip("Codename: ").strip("\n").strip('\t')
shell = run_command("bash --version | grep 'GNU bash' | awk '{print $2, $4}' ").strip("\n").strip("(1)-release").upper()
py = run_command("python3 --version").strip("\n")
resolution = run_command("xrandr | grep '*' | awk '{print $1, $2}' ").strip("\n").strip("*+")
de = desktop_environment()
wm = run_command("echo $XDG_SESSION_TYPE").strip("\n")
#dm = run_command("cat /etc/X11/default-display-manager").strip("\n")
dm = run_command("lslogins | grep Display | awk {'print $2'}").strip("\n")
terminal = environ.get('TERM')
teminal_emulator = run_command("pstree -sA $$ | awk -F '---' '{print $3}'").strip("\n").upper()
kernel = run_command("uname -r").strip("\n")
uptime = run_command("uptime | uptime | awk '{print $3}' ").strip("\n").strip(",")
host = run_command("cat /sys/devices/virtual/dmi/id/product_name").strip("\n")
cpu = run_command("cat /proc/cpuinfo | grep 'model name' | head -1 | awk '{print $4, $6, $8, $9}' ").strip("\n")
#cpu = run_command("lscpu | grep 'Modellnamn' | awk '{print $2, $3, $4, $5, $7, $8}' ").strip("\n")
gpu = run_command("glxinfo  | grep Device | awk {'print $2, $3, $4, $5, $6'}").strip("Device: ").strip("\n")
audio = run_command("lshw 2> /dev/null -C multimedia  | grep produkt").strip("produkt: ").strip("\n")
packages = run_command("dpkg --get-selections | grep -v deinstall | wc -l").strip("\n")
flatpak = run_command("flatpak list | wc -l").strip("\n")
snap = run_command("snap list | wc -l").strip("\n")

# RAM check for Swedish(Minne) or English(Mem)
totalram = run_command("free -m | grep Minne | awk '{print $2}' ").strip("\n")
if totalram == "":
    totalram = run_command("free -m | grep Mem | awk '{print $2}' ").strip("\n")
totalram = int(totalram) 
totalram /= 1000
totalram = round(totalram, 2)
totalram = str(totalram) 

usedram = run_command("free -m | grep Minne | awk '{print $3}' ").strip("\n")
if usedram == "":
    usedram = run_command("free -m | grep Mem | awk '{print $3}' ").strip("\n")
usedram = int(usedram)
usedram /= 1000
usedram = round(usedram, 2)
usedram = str(usedram)

#active_ram = run_command("cat /proc/meminfo | grep Active: | awk '{print $2}' ").strip("\n").strip("kB")


def print_logo():
    system("cat ~/neo/ubuntu.txt")


# Array for printing table
info = [
    "",
    "[bold red]GNU Linux  :penguin:  " + user + " @ " +computer_name + " [/]",
    "              --------------",
    "[bold red]OS[/]: "        + os_name + " " + os_codename,
    "[bold red]Host[/]: "      + host,
    "[bold red]Kernel[/]: "    + kernel,
    "[bold red]Uptime[/]: "    + uptime,
    "[bold red]Packages[/]: "  + packages + " dpkg, " + flatpak + " flatpak, " + snap + " snap",
    "[bold red]Shell[/]: "     + shell,
    "[bold red]Python[/]: "    + py,
    "[bold red]Resolution[/]: "+ resolution,
    "[bold red]DE[/]: "        + de,
    "[bold red]WM[/]: "        + wm,
    "[bold red]DM[/]: "        + dm,
    "[bold red]Terminal[/]: "  + teminal_emulator + ": " + terminal,
    "[bold red]CPU[/]: "       + cpu,
    "[bold red]GPU[/]: "       + gpu,
    "[bold red]Audio[/]: "     + audio,
    "[bold red]Memory[/]: "    + usedram + " GB / " + totalram + " GB",
    "",
]


def print_table():
    table = Table(show_header=False, show_lines=False, expand=False, show_edge=False, box=None)     
    
    ### TODO: alias neo='path_to_infofetch.py table' do not work from other dir!
    logo_file = "/neo/ubuntu.logo" # ~/neo/ubuntu.logo
    file_path = getcwd()+logo_file

    for a, line in enumerate(open(file_path, "r")):
        line = line.strip("\n")
        line = "[red]" + line + " [/]" 
        table.add_row(line, info[a])

    console.print(table)


def print_info():
    # Print to console
    print(f"    [bold red]GNU Linux  :penguin:  {user} @ {computer_name} [/]")
    print("                  --------------")
    print(f"    [bold red]OS[/]:         {os_name} {os_codename}")
    print(f"    [bold red]Host[/]:       {host}")
    print(f"    [bold red]Kernel[/]:     {kernel}")
    print(f"    [bold red]Uptime[/]:     {uptime}")
    print(f"    [bold red]Packages[/]:   {packages} dpkg, {flatpak} flatpak, {snap} snap")
    print(f"    [bold red]Shell[/]:      {shell}")
    print(f"    [bold red]Python[/]:     {py}")
    print(f"    [bold red]Resolution[/]: {resolution}")
    print(f"    [bold red]DE[/]:         {de} ")
    print(f"    [bold red]WM[/]:         {wm}")
    print(f"    [bold red]DM[/]:         {dm}")
    print(f"    [bold red]Terminal[/]:   {teminal_emulator}: {terminal}")
    print(f"    [bold red]CPU[/]:        {cpu}")
    print(f"    [bold red]GPU[/]:        {gpu}")
    print(f"    [bold red]Audio[/]:      {audio}")
    print(f"    [bold red]Memory[/]:     {usedram} GB / {totalram} GB")


def print_help():
    print_logo()
    print("Usage: \npython3 infofetch.py")
    print("python3 infofetch.py table")
    print("python3 infofetch.py logo")
    print("python3 infofetch.py info")
    print("python3 infofetch.py help or --help or -h")


if __name__ == "__main__":
    args = argv[1:]
    if args == []:
        print_info()
    elif args[0] == "table":
        print_table()
    elif args[0] == "logo":
        print_logo()
    elif args[0] == "info":
        print_info()
    elif  args[0] == "-h" or args[0] == "--help" or args[0] == "help":
        print_help()
    else:
        print("Unknown argument")