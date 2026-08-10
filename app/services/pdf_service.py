import fitz


class PDFService:

    @staticmethod
    def extract_text(pdf_path):
        """
        Extract text from every page in a PDF.
        """

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        return {
            "pages": len(document),
            "text": text
        }