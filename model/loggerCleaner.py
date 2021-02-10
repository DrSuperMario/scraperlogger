from typing import Generator
from dataclasses import dataclass

import re
from pathlib import Path

from util.search_log import search_log_files




@dataclass
class LoadLog():

    filename: Path
    re_dates: re
    re_text: re
    re_special: re
    

    def __init__(self):

        self.re_dates = re.compile(r'[(\d+\-|:)]+')
        self.re_text = re.compile(r'([A-z]+)')
        self.re_special = re.compile(r'[\W]')
        self.filename = search_log_files()

    def __doc__(self):
        #
        #
        #Write some Doc pleasseeee! For mee
        #
        #
        ...
    
    def __str__(self):
        return "LoggerCleaner Module"


    def load_log_from_file(self) -> Generator:

        try:

            #breakpoint()
            with open(Path(self.filename)) as f:
                for i in f.readlines():
                    i = i.strip("\n")
                    log_dates = re.findall(self.re_dates, i)
                    log_data = re.findall(self.re_text, i)
                    yield log_dates+log_data

        except OSError:
            raise FileNotFoundError("File not Found")

    def add_html_tolog(self, tag=str, style=str, oldest_first=False) -> str: 

        """

        generator -- generator object to get data from

        tag -- html tag to be used

        class -- css class to be used

        """
        generator = self.load_log_from_file()

        def check_error_level(error) -> str:

            try:
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
                elif(error=="NONE"):
                    return """list-group-item""","""
                            <span style='color:black;'><b>NONE</b></span> 
                            """
            except ValueError or TypeError:
                return """list-group-item""","""
                            <span style='color:black;'><b>NONE</b></span> 
                            """
    

        _list_x = list()
        data = str()

        if(oldest_first):
            generator = sorted(generator, key=lambda x: ' '.join(x[0]+x[1]), reverse=False)
        else:
            generator = sorted(generator, key=lambda x: ' '.join(x[0]+x[1]), reverse=True)

        for i in generator:
            #Here add html 
            
            #Cathing a NoneType object
            if(i[3] is None or re.match(self.re_special,i[3])): i[3] = "NONE"

            _list_x.append(f"""
                                <{tag} class="{check_error_level(i[3])[0]}">
                                    <b>{' '.join(i[:2])} </b>{check_error_level(i[3])[1]} {' '.join(i[4:])}
                                </{tag}>
                                """)
            data = ''.join(_list_x)
        return data                    