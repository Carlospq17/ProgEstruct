#clase para probar cositas
import re
import os

class Appearance:
    """
    Represents the appearance of a term in a given document, along with the
    frequency of appearances in the same one.
    """
    def __init__(self, docId, frequency):
        self.docId = docId
        self.frequency = frequency

    def __repr__(self):
        """
        String representation of the Appearance object
        """
        return str(self.__dict__)

class Database:
    """
    In memory database representing the already indexed documents.
    """
    def __init__(self):
        self.db = dict()

    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.__dict__)

    def get(self, id):
        return self.db.get(id, None)

    def add(self, document):
        """
        Adds a document to the DB.
        """
        return self.db.update({document['id']: document})

    def remove(self, document):
        """
        Removes document from DB.
        """
        return self.db.pop(document['id'], None)

class InvertedIndex:
    """
    Inverted Index class.
    """
    def __init__(self, db):
        self.index = dict()
        self.db = db

    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.index)

    def index_document(self, document):
        """
        Process a given document, save it to the DB and update the index.
        """

        # Remove punctuation from the text.
        print document['text']
        print document['id']
        clean_text = re.sub(r'[^\w\s]','', document['text'])
        terms = clean_text.split(' ')
        appearances_dict = dict()
        # Dictionary with each term and the frequency it appears in the text.
        for term in terms:
            term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
            appearances_dict[term] = Appearance(document['id'], term_frequency + 1)

        # Update the inverted index
        update_dict = { key: [appearance]
                       if key not in self.index
                       else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items() }
        self.index.update(update_dict)
        # Add the document into the database
        self.db.add(document)
        return document

    def lookup_query(self, query):
        """
        Returns the dictionary of terms with their correspondent Appearances.
        This is a very naive search since it will just split the terms and show
        the documents where they appear.
        """
        return { term: self.index[term] for term in query.split(' ') if term in self.index }

def highlight_term(id, term, text):
    replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
    return "--- document {id}: {replaced}".format(id=id, replaced=replaced_text)

def main():
    db = Database()
    index = InvertedIndex(db)
    document1 = {
        'id': '1',
        'text': 'The big sharks of Belgium drink beer.'
    }
    document2 = {
        'id': '2',
        'text': 'Belgium has great beer. They drink beer all the time,,,Belgium.'
    }
    index.index_document(document1)
    index.index_document(document2)


    search_term = raw_input("Enter term(s) to search: ")
    result = index.lookup_query(search_term)

    for term in result.keys():
        for appearance in result[term]:
            # Belgium: { docId: 1, frequency: 1}
            document = db.get(appearance.docId)
            print(highlight_term(appearance.docId, term, document['text']))
        print("-----------------------------")

def read_directory():
    direccion = raw_input("Ingrese la direccion de un archivo de texto...\n")
    onlyfiles = [f for f in os.listdir(direccion) if os.path.isfile(os.path.join(direccion, f))]
    for a in onlyfiles:
        fullPath = direccion + "/"
        isTxt = re.search(".txt", a)
        if isTxt != None:
            fullPath = fullPath + a
            print fullPath

def try_re():
    palabra = "Habló ."
    clean_Text = re.sub(r'[^\w\s]',"",palabra)
    print clean_Text

#main()
#read_directory()
try_re()

#-> /Users/carlospool/Desktop/PE_ACOMP/Proyecto/Python
#-> python indexado.py
