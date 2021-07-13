## change encoding
### change path/to/destination
    find . -type f -exec iconv -f euc-kr -t utf-8 "{}" -o path/to/destination/"{}" \;
