finder() {
    ls -R ./*.py
}
val=$(finder)
echo $val
vim -o {$val}
