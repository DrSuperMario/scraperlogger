from typing import Generator
import re
from pathlib import Path



def load_log_from_file(filename='temp/scraper.log') -> Generator:

    try:
        file = Path("/home/drmario/python/projects/SIGNAL-Scraper/log/scraper.log")
        if(file.exists()):
            filename = file
       
            
        with open(filename) as f:
            for i in f.readlines():
                i = i.strip("\n")
                log_dates = re.findall(r'[(\d+\-|:)]+',i)
                log_data = re.findall(r'([A-z]+)',i)
                yield log_dates+log_data

    except OSError:
        raise FileNotFoundError("File not Found")

def add_html_tolog(generator, tag=str, style=str, newest_first=False) -> str: 

    """

    generator -- generator object to get data from

    tag -- html tag to be used

    class -- css class to be used

    """

    def check_error_level(error) -> str:
        if(error=="ERROR"):
            return """list-group-item list-group-item-danger""","""
                     <span style='color:red;'><b>ERROR</b></span> 
                    """
        elif(error=="INFO"):
            return  """list-group-item""","""
                     <span style='color:black;'><b>INFO</b></span> 
                    """
        elif(error=="WARNING"):
            return """list-group-item list-group-item-warning""","""
                     <span style='color:black;'><b>WARNING</b></span> 
                    """
 

    _list_x = list()
    data = str()

    if(newest_first):
        generator = sorted(generator, key=lambda x: ' '.join(x[0]+x[1]), reverse=True)
    else:
        generator = sorted(generator, key=lambda x: ' '.join(x[0]+x[1]), reverse=False)
        
    for i in generator:
        #Here add html 
        if(i[3]=="-"):
            breakpoint()
        _list_x.append(f"""
                            <{tag} class="{check_error_level(i[3])[0]}">
                                <b>{' '.join(i[:2])} </b>{check_error_level(i[3])[1]} {' '.join(i[4:])}
                            </{tag}>
                            """)
        data = ''.join(_list_x)
    return data                    

def main():
    print("use: " + load_log_from_file.__doc__)


if __name__=="__main__":
    main()