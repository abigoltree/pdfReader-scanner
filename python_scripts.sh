finder() {
    ls -R ./programming/*.py
}
val=$(finder)
echo $val
vim -o {$val}
