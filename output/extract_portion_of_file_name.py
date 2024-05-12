"""Kata - extract portion of file name

completed at: 2023-01-30 19:25:50
by: Jakub Červinka

You have to extract a portion of the file name as follows:

* Assume it will start with date represented as long number
* Followed by an underscore
* You'll have then a filename with an extension
* it will always have an extra extension at the end

Inputs:
---
```
1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION

1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34

1231231223123131_myFile.tar.gz2
```

Outputs
---

```
FILE_NAME.EXTENSION

This_is_an_otherExample.mpg

myFile.tar
```

Acceptable characters for random tests:

`abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-0123456789`

The recommended way to solve it is using RegEx and specifically groups.
"""

import re

class FileNameExtractor:
    @staticmethod
    def extract_file_name(dfn):
        acc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_\-0123456789'
        return re.findall(fr'^\d+_([{acc}]+\.[{acc}]+).*$', dfn)[0]
