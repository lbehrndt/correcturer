from pdf_parser import PDFParser

def main():
    parser = PDFParser()
    
    sections = parser.parse_pdf().get_sections()
    
    for i, section in enumerate(sections):
        print(f'Section {i+1}: {section}\n')
        
if __name__ == "__main__":
    main()