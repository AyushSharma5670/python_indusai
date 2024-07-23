import urllib.request
from html.parser import HTMLParser

class SimpleWebScraper(HTMLParser):
    def _init_(self):
        super()._init_()
        self.in_header = False
        self.in_footer = False
        self.in_paragraph = False
        self.headers = []
        self.footers = []
        self.paragraphs = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.in_header = True
        elif tag == 'footer':
            self.in_footer = True
        elif tag == 'p':
            self.in_paragraph = True
        elif tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.images.append(attr[1])

    def handle_endtag(self, tag):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.in_header = False
        elif tag == 'footer':
            self.in_footer = False
        elif tag == 'p':
            self.in_paragraph = False

    def handle_data(self, data):
        if self.in_header:
            self.headers.append(data.strip())
        elif self.in_footer:
            self.footers.append(data.strip())
        elif self.in_paragraph:
            self.paragraphs.append(data.strip())

def fetch_html(url):
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                return response.read().decode('utf-8')
            else:
                print(f"Error: Received response status code {response.status}")
                return None
    except Exception as e:
        print(f"Error fetching the HTML: {e}")
        return None

def main():
    url = input("Enter the URL of the website to scrape: ")
    html_content = fetch_html(url)

    if html_content:
        parser = SimpleWebScraper()
        parser.feed(html_content)
        
        print("Headers:")
        for header in parser.headers:
            print(f"  {header}")
        
        print("\nFooters:")
        for footer in parser.footers:
            print(f"  {footer}")

        print("\nParagraphs:")
        for paragraph in parser.paragraphs:
            print(f"  {paragraph}")

        print("\nImages:")
        for image in parser.images:
            print(f"  {image}")
    else:
        print("Could not fetch the HTML content. Please check the URL and try again.")

if _name_ == "_main_":
    main()
