import re
from pdf_parser import PDF
from lib.chapter_queue import Chapter

def main():
    pdf = PDF()
    
    all_words = pdf.text.split()
    
    chapters = create_chapters(all_words)
    
    for key in chapters.keys():
        chapter = chapters[key]
        if chapter.hasNext():
            print(f"\nChapter {chapter.name}: {chapter.getNext()}")
    
def create_chapters(words: list[str]) -> dict[int, Chapter]:
    chapters: dict[int, Chapter] = dict()
    lastChapterIndex = 0
    section_limit_increment = 200
    section_limit = section_limit_increment
    current_section = ""
    for i, word in enumerate(words):
        is_word = valid_word(word)
        if not is_word: continue
        
        headline = valid_headline(word)
        if len(headline) > 0:
            match = re.search(r'^[a-z]+', word)
            if match: word = match.group(0)
            
            newChapter = Chapter(headline)
            lastChapterIndex = i
            chapters[lastChapterIndex] = newChapter
        
        is_end_of_sentence = valid_end_of_sentence(word)
        is_last_section = (len(words) - i) < section_limit_increment
        if (is_end_of_sentence or is_last_section) and i >= section_limit:
            chapters[lastChapterIndex].insert(current_section)
            current_section = ""
            # calculate the new word limit
            section_limit = section_limit + section_limit_increment if section_limit + section_limit_increment <= len(words) and not is_last_section else section_limit + (len(words) - section_limit) - 1
        
        current_section = current_section + word + " "
        
    return chapters
            

def valid_headline(word: str) -> str:
        match = re.search(r'([A-Z]{2,})', word)
        if match:
            return match.group(0)
        else:
            return ''

def valid_word(current_word: str) -> bool:
        illegal_characters = ['•', '\\', '_', '.', '/', '']
        
        start_of_word = current_word[0]
        
        if start_of_word in illegal_characters: 
            return False
        
        return True

def valid_end_of_sentence(word: str) -> bool:
    last_char = word[-1]
    if last_char == '.': return True
    if last_char == '!': return True
    if last_char == '?': return True
    if last_char == ':': return True
    
    word_without_last_char = word[:-1]
    if not word_without_last_char.isdigit(): return True
    
    return False
    
if __name__ == "__main__":
    main()
    
    