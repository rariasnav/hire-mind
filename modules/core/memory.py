from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory

def get_memory(buffer_type="window", k=5):
    """
    Returns a memory object to be used in the agent or RAG chain.
    - buffer_type: "window" (recent k messages) or "full" (entire conversation)
    - k: number of recent exchanges to remember
    """
    if buffer_type == "window":
        return ConversationBufferWindowMemory(
            k=k, 
            memory_key="chat_history", 
            input_key="question",
            return_messages=True,
            output_key="answer"
        )
    else:
        return ConversationBufferMemory(
            memory_key="chat_history",
            input_key="question",
            return_messages=True
        )