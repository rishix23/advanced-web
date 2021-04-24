# -*- coding: utf-8 -*-
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Inches, Cm
from docx.shared import Pt

def template1():
    # initiate a new word document with custom margins
    document = Document()
    sections = document.sections
    for section in sections:
        section.top_margin = Cm(1.5)
        section.bottom_margin = Cm(1.5)
        section.left_margin = Cm(1.5)
        section.right_margin = Cm(1.5)

    # style = document.styles['Normal']
    # font = style.font
    # font.name = 'Calibri (Headings)'
    # font.size = Pt(12)

    obj_styles = document.styles
    obj_charstyle = obj_styles.add_style('CommentsStyle', WD_STYLE_TYPE.CHARACTER)
    obj_font = obj_charstyle.font
    obj_font.size = Pt(12)
    obj_font.name = 'Times New Roman'

    # add user info to document on upper right-hand corner
    address = "Guildford, UK"
    telephone = "07950974823"
    email = "rp00463@surrey.ac.uk"

    paragraph = document.add_paragraph()
    paragraph.add_run('Location: ').bold = True
    paragraph.add_run(address)
    run = paragraph.add_run()
    run.add_break()
    paragraph.add_run("Telephone: ").bold = True
    paragraph.add_run(telephone) # replace with input
    run = paragraph.add_run()
    run.add_break()
    paragraph.add_run("Email: ").bold = True
    paragraph.add_run(email)
    street_address_p_format = paragraph.paragraph_format
    street_address_p_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # set all variables to inputs from front-end
    name = "Rishi Patel"
    professional_profile = "I love working in teams and I am a great problem solver."

    education = "University of Surrey"
    education_date = "2017-2021"

    work_experience = "IBM"
    work_experience_date = "2019-2020"

    volunteering_experience = "Food bank"
    volunteering_experience_date = "2012-2016"
    
    skills = ["tennis, C#"]

    certificates_achievements = ""

    # add name to document
    document.add_heading(name, 0)

    # profile section
    document.add_heading('Professional Profile', level=1)
    professional_profile_p = document.add_paragraph(professional_profile)

    # education section
    document.add_heading('Education', level=1)
    education_p = document.add_paragraph(style='List Bullet')

    # add for loop here

    education_p.add_run(education, style = 'CommentsStyle').bold = True
    run = education_p.add_run()
    run.add_break()
    education_p.add_run(education_date)

    # work experience section
    document.add_heading('Work Expereince', level=1)
    work_experience_p = document.add_paragraph(style='List Bullet')
    # add for loop here

    work_experience_p.add_run(work_experience).bold = True
    run = work_experience_p.add_run()
    run.add_break()
    work_experience_p.add_run(work_experience_date)

    # volunteering experience section
    document.add_heading('Volunteering', level=1)
    volunteering_p = document.add_paragraph(style='List Bullet')
    # add for loop here
    volunteering_p.add_run(volunteering_experience).bold = True
    run = volunteering_p.add_run()
    run.add_break()
    volunteering_p.add_run(volunteering_experience_date)

    # skills section
    document.add_heading('Skills', level=1)
    skills_p = document.add_paragraph(style='List Bullet')
    for skill in skills:
        skills_p.add_run(skill)

    # Achievments/Accolades/Certificates section
    document.add_heading('Achievments/Accolades/Certificates', level=1)
    certificates_achievements_p = document.add_paragraph(style='List Bullet')
    # add for loop here
    certificates_achievements_p.add_run(certificates_achievements).bold = True

    document.add_picture('butterfly.png', width=Inches(3))

    # # document.add_page_break()

    document.save('demo.docx')

if __name__ == "__main__":
    template1()