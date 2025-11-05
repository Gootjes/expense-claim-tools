# expense-claim-tools
Python tools that smooth the process of filing expense claims that require pdf files only

## Usage
### Convert images to pdf files
This tool converts images to a pdf file per image file.
```py
python -m imageconverter *.png *.jpg *.jpeg
```

### Add text to pdf files
This tool adds a number to each pdf file depending on its file name.
For example, file `001-expenses-day-1.pdf` will be processed to add `001` to the bottom left of every page.
```py
python -m textadder *.pdf
```

### Merge pdf files into one
This tool merges multiple pdf files into a single pdf file named `merged.pdf`
```py
python -m pdfmerger *.pdf
```
