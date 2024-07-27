#!/bin/bash

grep -xFf geneID_expressed_hdac3_WT.txt meta2d_hdac3_WT_pval.txt > sig_hdac3_WT.txt

grep -xFf geneID_expressed_nfil3_WT.txt meta2d_nfil3_WT_pval.txt > sig_nfil3_WT.txt

grep -xFf geneID_expressed_nr1d1_WT.txt meta2d_nr1d1_WT_pval.txt > sig_nr1d1_WT.txt

grep -xFf geneID_expressed_GF.txt meta2d_GF_pval.txt > sig_GF.txt