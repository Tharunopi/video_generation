class fileReader:
    @staticmethod
    def read_script(path:str="Script_txt_file\script.txt", encoding:str="utf-8") -> str|None:
        try:
            with open(path, "r", encoding=encoding) as f:
                content = f.read()
            return content

        except Exception as e:
            print(f"{__name__} -> {e}")
            return None