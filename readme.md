# Hexview

## installation

copy `/src/hexview` to your [python site-packages folder](https://stackoverflow.com/questions/31384639/what-is-pythons-site-packages-directory) or execute in `/src`.

## usage:

```bash
$ python -m hexview [-h]
                    [-t {hex,dec,oct,bin}]
                    [-l LINE_LEN]
                    [-o FILE]
                    filename

positional arguments:
  filename     The file to be
               viewed

options:
  -h, --help   show this help
               message and exit
  -t {hex,dec,oct,bin}, --type {hex,dec,oct,bin}
               The data type to
               display
  -l LINE_LEN, --line-len LINE_LEN
               The number of bytes
               per line

output:
  -o FILE, --output FILE
               Write output to FILE
               instead of stdout
```
