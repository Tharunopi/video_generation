from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

class longShortMemory:
    @staticmethod
    def get_memory(conn_string:str) -> SqliteSaver:
        try:
            conn = sqlite3.connect(conn_string, check_same_thread=False)
            return SqliteSaver(conn)
        
        except Exception as e:
            print(f"{__name__} -> {e}")