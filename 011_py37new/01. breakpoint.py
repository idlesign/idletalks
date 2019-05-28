
# PEP-553: http://pythonz.net/peps/named/0553/

###############################################################################

a = 1
b = 2

# import pdb; pdb.set_trace()
# import pudb; pudb.set_trace()
# import ipdb; ipdb.set_trace()
# import web_pdb; web_pdb.set_trace()

# breakpoint()


###############################################################################

# export PYTHONBREAKPOINT=ipdb.set_trace
# export PYTHONBREAKPOINT=web_pdb.set_trace
# export PYTHONBREAKPOINT=0

def configure_pydev() -> None:
    try:
        import pydevd
        import sys

        sys.breakpointhook = pydevd.settrace

    except ImportError:
        pass


configure_pydev()
breakpoint()

c = 3
d = 4


###############################################################################
