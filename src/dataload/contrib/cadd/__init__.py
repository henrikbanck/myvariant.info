# -*- coding: utf-8 -*-

from .cadd_parser import load_data as _load_data


CADD_INPUT_FILE = 'http://krishna.gs.washington.edu/download/CADD/v1.0/whole_genome_SNVs_inclAnno.tsv.gz'


def load_data():
    cadd_data = _load_data(CADD_INPUT_FILE)
    return cadd_data


