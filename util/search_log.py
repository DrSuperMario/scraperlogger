from pathlib import Path
import os
import platform


def search_log_files(p_dir=None) -> str:

    list_of_logs = list()

    try:
        
        if(platform.system() == 'Windows'):
            p_dir = r"C:\Users\mario\OneDrive\Desktop\Python\Projects"
        else:
            p_dir = r"/home/drmario/python/projects"
            
    except TypeError:
        print("No such device")
        
    p = Path(p_dir)

    for i in p.glob('**/*.log'):
        if(i.name == "scraper.log"):
            list_of_logs.append(i)
        
    return list_of_logs[1]


if __name__=="__main__":
    search_log_files()