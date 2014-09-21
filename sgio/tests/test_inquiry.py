#!/usr/bin/env python
# coding: utf-8

import sys

from sgio.pyscsi.scsi import SCSI
from sgio.pyscsi import scsi_cdb_inquiry as INQUIRY

def main(device):
    s = SCSI(device)

    i = s.inquiry().result
    print i

    i = s.inquiry(evpd = 1, page_code = INQUIRY.VPD.SUPPORTED_VPD_PAGES).result
    print i

if __name__ == "__main__":
    main(sys.argv[1])
