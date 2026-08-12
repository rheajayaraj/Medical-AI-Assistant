import pymupdf


class PDFService:

    @staticmethod
    def extract_text(pdf_path):
        """
        Extract text from every page in a PDF.
        """

        document = pymupdf.open(pdf_path)

        pages = []

        for page_number, page in enumerate(document):

            pages.append({

                "page": page_number + 1,

                "text": page.get_text()

            })

        document.close()

        return pages