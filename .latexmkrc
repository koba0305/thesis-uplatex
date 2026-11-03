$pdf_mode = 3;
$latex = 'uplatex -kanji=utf8 -synctex=1 -interaction=nonstopmode -halt-on-error %O %S';
$biber = 'biber %O %B';
$bibtex = 'upbibtex %O %B';
$dvipdf = 'dvipdfmx %O -o %D %S';
$makeindex = 'mendex -U %O -o %D %S';
$max_repeat = 5;
