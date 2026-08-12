from app.services.llm_service import LLMService


class QuestionRewriter:

    @staticmethod
    def rewrite(question, history):

        if not history:
            return question

        conversation = ""
        for msg in history:

            role = msg.role if hasattr(msg, "role") else msg["role"]
            content = msg.content if hasattr(msg, "content") else msg["content"]

            conversation += f"{role}: {content}\n"

        prompt = f"""
You are an AI assistant.

Your job is to rewrite the user's latest question into a complete standalone question.

Use the conversation history.

If the question is already complete, return it unchanged.

Conversation:
{conversation}

Latest Question:
{question}

Standalone Question:
"""

        return LLMService.generate(prompt).strip()