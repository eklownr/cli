from rich import print
from os import environ
import subprocess


def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8')

''' Get data from the system '''
user = environ.get('USER')
computer_name = run_command("hostname").strip("\n")
#os_name = run_command("cat /etc/os-release | grep 'PRETTY_NAME' ").strip("\n").strip('"').strip('PRETTY_NAME="')   
os_name = run_command("lsb_release -d | awk '{print $2, $3, $4}' ").strip("\n")
shell = run_command("bash --version | grep 'GNU bash' | awk '{print $2, $4}' ").strip("\n").strip("(1)-release").upper()
py = run_command("python3 --version").strip("\n")
resolution = run_command("xrandr | grep '*' | awk '{print $1, $2}' ").strip("\n").strip("*+")
de = run_command("gnome-shell --version").strip("\n")
terminal = environ.get('TERM')
teminal_emulator = run_command("pstree -sA $$ | awk -F '---' '{print $3}'").strip("\n").upper()
kernel = run_command("uname -r").strip("\n")
uptime = run_command("uptime | uptime | awk '{print $3}' ").strip("\n").strip(",")
host = run_command("cat /sys/devices/virtual/dmi/id/product_name").strip("\n")
cpu = run_command("cat /proc/cpuinfo | grep 'model name' | head -1 | awk '{print $4, $5, $6, $7, $8, $9}' ").strip("\n")
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

usedram = run_command("free -m | grep Minne | awk '{print $3}' ").strip("\n")
if usedram == "":
    usedram = run_command("free -m | grep Mem | awk '{print $3}' ").strip("\n")
usedram = int(usedram)
usedram /= 1000
usedram = round(usedram, 2)

#active_ram = run_command("cat /proc/meminfo | grep Active: | awk '{print $2}' ").strip("\n").strip("kB")
#active_ram = int(active_ram) / 1024
#active_ram /= 1000
#active_ram = round(active_ram, 2)

# run: python3 -m rich.emoji
emoji = ":penguin:"

# Print to console
print(f"    [bold red]GNU Linux  :penguin:  {user} @ {computer_name} [/]")
print(f"    [bold red]OS:[/]         {os_name}")
print(f"    [bold red]Host:[/]       {host}")
print(f"    [bold red]Kernel:[/]     {kernel}")
print(f"    [bold red]Uptime:[/]     {uptime}")
print(f"    [bold red]Packages:[/]   {packages} dpkg, {flatpak} flatpak, {snap} snap")
print(f"    [bold red]Shell:[/]      {shell}")
print(f"    [bold red]Python:[/]     {py}")
print(f"    [bold red]Resolution:[/] {resolution}")
print(f"    [bold red]DE:[/]         {de} :footprints:")
print(f"    [bold red]Terminal:[/]   {teminal_emulator}: {terminal}")
print(f"    [bold red]CPU:[/]        {cpu}")
print(f"    [bold red]Memory:[/]     {usedram} GB / {totalram} GB")