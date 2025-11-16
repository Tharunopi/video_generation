class outputReader:
    @staticmethod
    def read(file_name:str) -> str:
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                content = f.read()
            
            return content

        except Exception as e:
            print(f"{__name__} -> {e}")