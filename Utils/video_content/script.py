import docx2txt

class Script:
    @staticmethod
    def get_script(path:str=r"C:\Stack overflow\video_generation\Utils\video_content\scripts.docx") -> str:
        script = docx2txt.process(path)
        return script