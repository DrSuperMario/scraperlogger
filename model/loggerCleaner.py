from typing import Generator
import re



def load_log_from_file(filename) -> Generator:

    try:
        with open(filename) as f:
            for i in f.readlines():
                yield i.strip("\n")

    except OSError:
        print("File not found")   

def add_html_tolog(generator, tag=str, style=str) -> str: 

    """
    
    generator -- generator object to get data from

    tag -- html tag to be used

    class -- css class to be used

    """

    _list_x = []
    data = str
    for i in generator:
        #Here add html 
        log_dates = re.findall(r'(\d+-\d+-\d+ \d+:\d+:\d+,\d+)',i)
        log_data = re.findall(r'([A-z]+)',i)
        _list_x.append(f"""
                            <{tag} class="{style}"><b>{log_dates[0]}</b> {' '.join(log_data)}</{tag}>
                            """)
        data = ''.join(_list_x)
    return data                    

def main():
    print("use: " + load_log_from_file.__name__)


if __name__=="__main__":
    main()