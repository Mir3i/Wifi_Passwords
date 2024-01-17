import subprocess
#ext_Password return Key Content from Text (Command line "Netsh wlan show profile name='Profile 1' key=clear ")
def ext_Password(wifi):
    Start = wifi.find("Key Content")
    if Start != -1:
        Start = wifi.find(":", Start)
        if Start != -1:
            End = wifi.find("\n", Start)
            if End != -1:
                password = wifi[Start + 1:End].strip()
                return password
    return None 
#ext_Wifi return Wifi Names from Text (Command line "netsh wlan show profiles")
def ext_Wifi(text):
    l = text.split('\n')
    All_Profiles = []
    for i in l:
        index = i.find(':')
        if index != -1:
            index_2 = i[index + 1:].strip()
            All_Profiles.append(index_2)
    return All_Profiles
#run and write cmd with subprocess.run().stdout
cmd = (subprocess.run('netsh wlan show profiles', capture_output=True, text=True, shell=True).stdout)
cmd = cmd[cmd.find("All User Profile")-4:]
#cmd contain list of Wifi Names
cmd = ext_Wifi(cmd)
for i in range(len(cmd)):
    text = subprocess.run(f'Netsh wlan show profile name= "{cmd[i]}" key=clear', capture_output=True, text=True, shell=True).stdout
    print(cmd[i],":",ext_Password(text))

