import os
from lxml import etree

from pyven.results.results_parser import ResultsParser

class TRXParser(ResultsParser):

    def __init__(self):
        super(TRXParser, self).__init__()
        self.tree = None
    
    def parse(self, file):
        result = []
        if os.path.isfile(file):
            tree = etree.parse(file)
            doc_element = tree.getroot()
            result = self._parse_trx(doc_element)
        else:
            msg = ['TRX report not found']
            self.errors.append(msg)
        return result
        
    def _parse_trx(self, node):
        query = '/vs:TestRun/vs:Results/vs:UnitTestResult[@outcome="Failed"]'
        for failed_test in node.xpath(query, namespaces={'vs' : 'http://microsoft.com/schemas/VisualStudio/TeamTest/2010'}):
            name = failed_test.get('testName')
            msg = ['Test ' + name]
            message = failed_test.xpath('vs:Output/vs:ErrorInfo/vs:Message', namespaces={'vs' : 'http://microsoft.com/schemas/VisualStudio/TeamTest/2010'})
            if message is not None and len(message) > 0 and message[0].text is not None:
                msg.append(message[0].text)
            self.errors.append(msg)

            