class ContextService:

    @staticmethod
    def build_context(search_results):

        contexts = []

        for result in search_results:

            metadata = result["metadata"]

            context = (
                f"Document: {metadata['filename']}\n"
                f"Page: {metadata['page']}\n\n"
                f"{result['document']}"
            )

            contexts.append(context)

        return "\n\n------------------------\n\n".join(contexts)