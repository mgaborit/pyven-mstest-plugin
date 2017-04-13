import os

from pyven.exceptions.parser_exception import ParserException
from pyven.plugins.plugin_api.parser import Parser

from mstest_plugin.mstest import MSTest

class MSTestParser(Parser):
    COUNT = 0
    SINGLETON = None
    
    def __init__(self, cwd):
        MSTestParser.COUNT += 1
        super(MSTestParser, self).__init__(cwd)
    
    def parse(self, node, project):
        objects = []
        members = self.parse_process(node)
        errors = []
        file = node.find('file').text
        if file == '':
            errors.append('Missing test file')
        (path, filename) = os.path.split(file)
        arguments = []
        for argument in node.xpath('arguments/argument'):
            arguments.append(argument.text)
        if len(errors) > 0:
            e = ParserException('')
            e.args = tuple(errors)
            raise e
        objects.append(MSTest(self.cwd, members[0], path, filename, arguments))
        return objects
        
def get(cwd):
    if MSTestParser.COUNT <= 0 or MSTestParser.SINGLETON is None:
        MSTestParser.SINGLETON = MSTestParser(cwd)
    MSTestParser.SINGLETON.cwd = cwd
    return MSTestParser.SINGLETON