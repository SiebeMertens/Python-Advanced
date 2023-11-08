import subprocess
  
def ping():
    print("**********************************************")
    tepingen = input("Voer de hostname of ip'adress van het apparaat dat u wilt pingen: ")

    resultOfPing = subprocess.run(['ping', tepingen], capture_output=True, text=True, check=True) 
    print(resultOfPing.stdout)
    teloggen = str(resultOfPing)
    
    fp = open("pinglog.txt", 'a')
    fp.write(f"<--- PING NAAR {tepingen} --->\n")
    fp.write("************************************\n")
    fp.write(f"{teloggen} \n")
    fp.close()