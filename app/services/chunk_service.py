import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkService:

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=100,

        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]

    )

    @classmethod
    def chunk_pages(
        cls,
        pages
    ):

        chunks = []

        chunk_index = 0

        for page in pages:

            text = page["text"].strip()

            if not text:
                continue

            split = cls.splitter.split_text(text)

            for chunk in split:

                chunks.append({

                    "chunk_id": str(uuid.uuid4()),

                    "chunk_index": chunk_index,

                    "page": page["page"],

                    "text": chunk

                })

                chunk_index += 1

        return chunks