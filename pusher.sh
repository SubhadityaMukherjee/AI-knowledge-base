pyenv activate openml
python posts/create_tag_pages.py
npx quartz build
# mkdocs build
if [ $# -eq 0 ]; then
    echo "No commit message provided"
    exit 1
fi
git add . && git commit -m "$1" && git push
