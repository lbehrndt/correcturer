import PyPDF2 as pypdf

class PDFParser: 
    FILE_PATH = "pdf_file/kompro-buch.pdf"
    
    def __init__(self) -> None:
        pass

    def parse_pdf(self):

        with open(self.FILE_PATH, 'rb') as file:
            reader = pypdf.PdfReader(file)
            
            page_range = range(len(reader.pages))
            text = ''
            
            print(reader.pages)
            for page in page_range:
                text += reader.pages[page].extract_text()
            
            self.pdf_text = text;
        
        return self;
    
    def get_sections(self) -> list:
        stripped_text = ' '.join(self.pdf_text.split())
        
        all_words: list[str] = stripped_text.split(' ')
        
        print(all_words)
        
        word_limit_increment = 300
        # set initial word limit to 300
        word_limit = word_limit_increment
        current_section = ''
        sections = []
        is_last_section = False
        for i, word in enumerate(all_words):
            is_valid_word = self.validWord(word)
            if not is_valid_word: continue
            
            current_section = current_section + word + ' '
            is_end_of_sentence = self.validEndOfSentence(word)
            is_last_section = (len(all_words) - i) < word_limit_increment
            
            # always add a whole sentence
            if i >= word_limit and (is_end_of_sentence or is_last_section):
                sections.append(current_section)
                current_section = ''
                
                # calculate the new word limit
                word_limit = word_limit + word_limit_increment if word_limit + word_limit_increment <= len(all_words) and not is_last_section else word_limit + (len(all_words) - word_limit) - 1
            
        return sections
        
    def validEndOfSentence(self, current_word: str) -> bool:
        if not current_word.endswith('.'): 
            return False
        
        word_without_period = current_word.removesuffix('.')
        if word_without_period.isdigit():
            return False
        
        return True
    
    def validWord(self, current_word: str) -> bool:
        illegal_characters = ['•', '\\', '_', '.', '…', '/', '']
        
        start_of_word = current_word[0]
        
        if start_of_word in illegal_characters: 
            return False
        
        return True
        
