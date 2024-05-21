from docxtpl import DocxTemplate

template = DocxTemplate("template.docx")

context = {
    "name": "Иван",
    "items": [{"product":"телефон", "price":300},
              {"product":"планшет", "price":700}

]
}

template.render(context)

template.save("generated.docx")