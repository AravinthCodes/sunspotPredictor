from importlib.metadata import distributions  
import os, time
from importlib.metadata import metadata
import pkg_resources

lib = []
for dist in distributions():
    lib.append(time.ctime(os.path.getctime(dist._path)))
    # print("%s %s: %s" % (dist.metadata["Name"], dist.version, time.ctime(os.path.getctime(dist._path))))

print(sorted(lib))

_package_name ='plotly'
_package = pkg_resources.working_set.by_key[_package_name]
print([str(r) for r in _package.requires()])
['tenacity>=6.2.0', 'packaging']