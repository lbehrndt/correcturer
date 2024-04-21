import PyPDF2 as pypdf

class PDF: 
    FILE_PATH = "pdf_file/kompro-buch.pdf"
    
    def __init__(self) -> None:
        self.pages = []
        with open(self.FILE_PATH, 'rb') as file:
            self.reader = pypdf.PdfReader(file)
            self.text = self.get_page_text()

    def get_page_text(self) -> str:
        pages = self.reader.pages
        
        text = ""
        for page in pages:
            page_text = page.extract_text()
            text += page_text
            
        return text