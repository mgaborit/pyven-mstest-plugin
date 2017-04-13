import zipfile, os
import mstest_plugin.constants

def zip_pvn():
    if not os.path.isdir(os.path.join(os.environ.get('PVN_HOME'), 'plugins')):
        os.makedirs(os.path.join(os.environ.get('PVN_HOME'), 'plugins'))
    zf = zipfile.ZipFile(os.path.join(os.environ.get('PVN_HOME'), 'plugins', 'mstest-plugin_' + mstest_plugin.constants.VERSION + '.zip'), mode='w')
    
    zf.write('__init__.py')
    
    zf.write('mstest_plugin/__init__.py')
    zf.write('mstest_plugin/constants.py')
    zf.write('mstest_plugin/parser.py')
    zf.write('mstest_plugin/mstest.py')
    zf.write('mstest_plugin/trx_parser.py')
    
if __name__ == '__main__':
    zip_pvn()
