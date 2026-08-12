from app.services.search_service import SearchService
from app.services.llm_service import LLMService
from app.services.question_rewriter import QuestionRewriter
from app.services.history_service import ChatHistoryService

class RAGService:

    def __init__(self):
        self.search_service = SearchService()

    def ask(self, query, session_id):
        history = ChatHistoryService.get_history(
            session_id
        )

        rewritten_question = QuestionRewriter.rewrite(
            question=query,
            history=history
        )

        search_results = self.search_service.search(
            query=rewritten_question,
        )

        if not search_results["results"]:
            return {
                "answer": "I couldn't find relevant information in the uploaded reports.",
                "sources": []
            }

        context = ""

        for r in search_results["results"]:
            page = r["metadata"].get("page", "?")

            context += f"""
            Page {page}

            {r["document"]}

            ------------------------
            """

        prompt = f"""
            You are a medical AI assistant.

            Answer ONLY using the provided context.

            If the answer is not present, say you don't know.

            Context:
            {context}

            Current Question:
            {query}

            Answer:
            """

        answer = LLMService.generate(prompt)

        ChatHistoryService.save_message(
            session_id,
            "user",
            query
        )

        ChatHistoryService.save_message(
            session_id,
            "assistant",
            answer
        )

        return {
            "answer": answer,
            "sources": [
                {
                    "page": r["metadata"]["page"],
                    "filename": r["metadata"]["filename"],
                    "score": round(r["score"], 2)
                }
                for r in search_results["results"]
            ]
        }