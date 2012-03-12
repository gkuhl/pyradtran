#! /usr/bin/env python
# coding: utf-8

from subprocess import PIPE, Popen

EXAMPLE = {
    'atmosphere_file': '../data/atmmod/afglus.dat',
    'solar_file':      '../data/solar_flux/atlas_plus_modtran',
    'wavelength':      '310.0 311.0'
}

def parse(inp):
    """\
    Parse input dictionary.
    """
    lines = ['\t'.join(item) for item in inp.iteritems()]
    return '\n'.join(lines)


def uvspec(stdin):
    """\
    Call uvspec with given 'stdin'.
    """
    p = Popen('../bin/uvspec', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(stdin)

    return stdout, stderr


if __name__ == '__main__':
    inp = parse(EXAMPLE)
    stdout, stderr = uvspec(inp)

    print 'STDOUT:'
    print stdout
    print 'STDERR:'
    print stderr
