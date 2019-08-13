from IPython.core.magic import Magics, magics_class, line_magic
from urllib.request import urlopen
import nbformat


@magics_class
class Import(Magics):

    @line_magic('import')
    def import_(self, url):
        with urlopen(url.strip().strip('" \'')) as f:
            nb = nbformat.read(f, as_version=4)
            for cell in nb.cells:
                if cell.cell_type == 'code':
                    self.shell.run_cell(cell.source)


def load_ipython_extension(ipython):
    ipython.register_magics(Import)
