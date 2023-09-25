#!/bin/bash
#python3 backlink_reset.py
python3 create_tag_pages.py
#node docs/grapher.js
#/home/erago/.yarn/bin/note-link-janitor docs/
#/home/erago/.yarn/bin/note-link-janitor docs/architectures/
#/home/erago/.yarn/bin/note-link-janitor docs/applications/
#/home/erago/.yarn/bin/note-link-janitor docs/federated/
#python3 zettelcon.py -f "docs/" -n 10
if [ $# -eq 0 ]; then
    echo "No commit message provided"
    exit 1
fi
git add . && git commit -m "$1" && git push
