#!/bin/bash

comm -12 sig_GF.txt conventional_genes.txt > shared.txt
comm -23 conventional_genes.txt sig_GF.txt > WT_only.txt
comm -13 conventional_genes.txt sig_GF.txt > GF_only.txt