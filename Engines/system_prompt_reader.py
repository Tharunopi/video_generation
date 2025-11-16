class promptReaderEngine:
    @staticmethod
    def read(prompt_name:str) -> str:
        try:
            path = f"System_prompts\{prompt_name}.txt"
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            return content

        except Exception as e:
            print(f"{__name__} -> {e}")