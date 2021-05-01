from htmldocx import HtmlToDocx


for i in list(range(8,13)):
    new_parser = HtmlToDocx()
    new_parser.parse_html_file(f'output{i}.html', f'output{i}')