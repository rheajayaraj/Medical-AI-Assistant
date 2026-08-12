from app.services.search_service import SearchService
from app.services.llm_service import LLMService


class RAGService:

    def __init__(self):
        self.search_service = SearchService()

    def ask(self, query):

        search_results = self.search_service.search(
            query=query,
        )

        print('///////////////////////////////////////')
        print(search_results)

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

            Answer ONLY using the information provided in the context.

            If the answer is not present in the context, reply exactly:

            "I could not find this information in the uploaded report."

            Do not make up values.
            Do not use outside medical knowledge.
            Do not guess.

            Context:
            {context}

            Question:
            {query}

            Answer:
            """

        answer = LLMService.generate(prompt)

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