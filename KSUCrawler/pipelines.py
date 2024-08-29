from bs4 import BeautifulSoup


class BodyTextPipeline:
    def process_item(self, item, spider):
        if 'body' in item:
            soup = BeautifulSoup(item['body'], 'html.parser')

            # Removes unnecessary text
            for tag in soup(["script", "style", "a", "img"]):
                tag.extract()

            text = soup.get_text(separator=' ')
            words = text.split()
            item['body'] = words

        return item
