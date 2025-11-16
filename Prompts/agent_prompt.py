from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate

class agenticPrompts:
    @staticmethod
    def scene_agent_prompt():
        try:
            prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", ),
                    ("user", "{script}")
                ]
            )

        except Exception as e:
            print(f"{__name__} -> {e}")