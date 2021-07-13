## change one file

    iconv -c -f euc-kr -t utf-8 file_to_change.txt > changed_file.txt

## change all file recursively
### change path/to/destination
    find . -type f -exec iconv -f euc-kr -t utf-8 "{}" -o path/to/destination/"{}" \;
