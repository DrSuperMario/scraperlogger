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
        else:
            raise ValueError("No right param")

    _list_x = []
    data = str
    for i in generator:
        #Here add html 
        log_dates = re.findall(r'(\d+-\d+-\d+ \d+:\d+:\d+,\d+)',i)
        log_data = re.findall(r'([A-z]+)',i)
        _list_x.append(f"""
                            <{tag} class="{check_error_level(log_data[0])[0]}">
                                <b>{log_dates[0]} </b>{check_error_level(log_data[0])[1]} {' '.join(log_data[1:])}
                            </{tag}>
                            """)
        data = ''.join(_list_x)
    return data                    

def main():
    print("use: " + load_log_from_file.__doc__)


if __name__=="__main__":
    main()