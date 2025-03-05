from bs4 import BeautifulSoup
import re

class WebScraper:
    def __init__(self, html_file):
        """Initialize the scraper with the provided HTML file"""
        self.html_file = html_file
        self.soup = self.load_html()

    def load_html(self):
        """Load and parse the HTML file"""
        with open(self.html_file, "r", encoding="utf-8") as file:
            return BeautifulSoup(file.read(), "html.parser")

    def find_element(self, tag=None, class_name=None, element_id=None):
        """Find an element by tag, class, or ID"""
        if element_id:
            element = self.soup.find(id=element_id)
        elif class_name:
            element = self.soup.find(class_=class_name)
        elif tag:
            element = self.soup.find(tag)
        else:
            return None
        return element.text if element else None

    def get_links(self, external_only=False):
        """Extract all links, optionally filter only external links"""
        links = [a["href"] for a in self.soup.find_all("a", href=True)]
        if external_only:
            return [link for link in links if re.match(r"^https://", link)]
        return links

    def navigate_tree(self, element_id):
        """Find parent and sibling elements for a given element ID"""
        element = self.soup.find(id=element_id)
        if not element:
            return None
        return {
            "parent_tag": element.parent.name if element.parent else None,
            "next_sibling": element.find_next_sibling().text if element.find_next_sibling() else None
        }

    def extract_table_data(self, table_id):
        """Extract and return table data"""
        table = self.soup.find("table", id=table_id)
        if not table:
            return []
        rows = table.find_all("tr")[1:]  # Skip header row
        return [{"Name": row.find_all("td")[0].text, "Age": row.find_all("td")[1].text} for row in rows if row.find_all("td")]

    def modify_html(self, new_text):
        """Add a new paragraph with given text"""
        new_tag = self.soup.new_tag("p")
        new_tag.string = new_text
        self.soup.body.append(new_tag)
        return "Paragraph added!"

    def add_list_item(self, list_id, item_text):
        """Add an item to a list"""
        ul = self.soup.find("ul", id=list_id)
        if not ul:
            return "No list found!"
        new_li = self.soup.new_tag("li")
        new_li.string = item_text
        ul.append(new_li)
        return f"Added list item: {item_text}"

    def remove_element(self, tag):
        """Remove the first occurrence of a given tag"""
        element = self.soup.find(tag)
        if element:
            element.decompose()
            return f"Removed first <{tag}> element!"
        return f"No <{tag}> element found!"

    def save_modified_html(self, output_file="modified_sample.html"):
        """Save modified HTML to a new file"""
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(str(self.soup))
        return f"Modified HTML saved as {output_file}"

# Usage Example
if __name__ == "__main__":
    scraper = WebScraper("sample.html")

    print("\n Finding elements:")
    print("H1 Tag:", scraper.find_element(tag="h1"))
    print("Class 'class1':", scraper.find_element(class_name="class1"))
    print("ID 'heading2':", scraper.find_element(element_id="heading2"))

    print("\n Extracting links:")
    print("All links:", scraper.get_links())
    print("External links:", scraper.get_links(external_only=True))

    print("\n Navigating HTML tree:")
    print(scraper.navigate_tree("list"))

    print("\n Extracting Table Data:")
    print(scraper.extract_table_data("sampleTable"))

    print("\n Modifying HTML:")
    print(scraper.modify_html("This is a dynamically added paragraph!"))

    print("\n Adding list item:")
    print(scraper.add_list_item("list", "Item 5"))

    print("\n Removing first link:")
    print(scraper.remove_element("a"))

    print("\n  Saving modified HTML:")
    print(scraper.save_modified_html())


