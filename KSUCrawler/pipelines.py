import re
from bs4 import BeautifulSoup
from string import punctuation


class BodyTextPipeline:
    def process_item(self, item, spider):
        if 'body' in item:
            soup = BeautifulSoup(item['body'], 'html.parser')

            # Removes unnecessary text
            for tag in soup(["script", "style", "a", "img"]):
                tag.extract()

            text = soup.get_text(separator=' | ',strip=True)
            words = text.split()
            clean_words = []
            word_pattern = re.compile(r'^[a-zA-Z]+$')
            for word in words:
                clean_word = word.strip(punctuation)
                if word_pattern.match(clean_word):
                    clean_words.append(clean_word)
            item['body'] = clean_words

        return item
