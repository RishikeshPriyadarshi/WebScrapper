from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt




# creating root object
root = Tk()


# defining size of window
root.geometry("1000x450")


# setting up the title of window
root.title("RESUME SCREENING BASED ON JOB DESCRIPTION")



#============================================#

# clicked function 1
def clicked1():
    messagebox.showinfo('INFO', 'FILE SELECTED')
    
 
        
#Resume file opening function
def openfile_resume():
    global pdfReader
    path2 = filedialog.askopenfilename()
    pdfFileObj = open(path2)
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    temp=pdfReader
    num_pages = temp.numPages
    clicked1()





# Function to screen resume
def screen(pdfReader,num_pages):
    count = 0
    text = ""
    # Extract text from every page on the file
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
    # Convert all strings to lowercase
    text = text.lower()
    # Remove numbers
    text = re.sub(r'\d+','',text)
    # Remove punctuation
    text = text.translate(str.maketrans('','',string.punctuation))
    # Create dictionary with industrial and system engineering key terms by area
    terms = {'Python Deveplor':['Python','Web Frameworks','Flask','Django','JavaScript','CSS','HTML',
                            'OOPs','Data Structures','Object Relational Mappers','ORM','SQL',
                            'Scikit learn','MatPlotib','NumPy','Artificial Intelligence','AI',
                            'Machine Learning','ML','Deep Learning','Natural Language Processing',
                            'NLP','Make','coding','programming','Jinja 2','SVN','Mercurial','Git','Big data'],
        'Full Stack Developer':['HTML','CSS','JavaScript','Data Structures','Python','Perl','Php','Node.js','React',
                                'Angular','JSON','DOM','Git','GitHub','Ruby','Java','Web architecture',
                                'XML','Sql','coding','programming','Mysql','NoSQL','UI & UX','Mysql','NPM','SQL','Jquery','Ajax'],
        'Java Deveplor':['Java','Object-Oriented Programming','Data Structures','Oops','Abstraction','Apache','Sonatype',
                           'Java Beans','Java Server Pages','programming','Servlets','Java EE','Bazel','Nexus','Cmake','Gradle',
                           'TestNG','Selenium','coding','Big data','Spring framework','Spring','Kotlin','Jenkins','Maven',],
        'Data analytics':['analytics','api','aws','big data','JBoss','Jetty','clustering',
                           'coding','data','database','data mining','data science','deep learning','hadoop',
                           'hypothesis test','machine learning','modeling','nosql','nlp',
                           'predictive','python','r','programming','sql','tableau','text mining',
                           'visualuzation'],
        'Android Developer':['Android Development','Android','HTML','CSS','C++','Java','Kotlin','Android Studio','XML','SQL',
                      'sql','Android Testing','coding','Testing','Android Software Development Kit','SDK','GIT','UI',
                      'UX','User Interface','Eclipse','Xamarin','programming','JSP','Oracle','Scrum','Gradle','JSON']}
    # Initializie score counters for each area
    python_cand = 0
    Fullst_cand = 0
    Java_cand = 0
    Data_cand = 0
    Andro_cand = 0
    # Create an empty list where the scores will be stored
    scores = []
    # Obtain the scores for each area
    for area in terms.keys():

        if area == 'Python Deveplor':
            for word in terms[area]:
                if word in text:
                    python_cand += 1
            scores.append(python_cand)

        elif area == 'Full Stack Developer':
            for word in terms[area]:
                if word in text:
                    Fullst_cand += 1
            scores.append(Fullst_cand)

        elif area == 'Java Deveplor':
            for word in terms[area]:
                if word in text:
                    Java_cand += 1
            scores.append(Java_cand)

        elif area == 'Data analytics':
            for word in terms[area]:
                if word in text:
                    Data_cand += 1
            scores.append(Data_cand)

        else:
            for word in terms[area]:
                if word in text:
                    Andro_cand += 1
            scores.append(Andro_cand)
    # Create a data frame with the scores summary
    summary = pd.DataFrame(scores,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)
    print(summary)
    # Create pie chart visualization
    pie = plt.figure(figsize=(10,10))
    plt.pie(summary['score'], labels=summary.index, explode = (0.1,0,0,0,0,0), autopct='%1.0f%%',shadow=True,startangle=90)
    plt.title('Industrial Engineering Candidate - Resume Decomposition by Areas')
    plt.axis('equal')
    plt.show()
    # Save pie chart as a .png file
    pie.savefig('resume_screening_results.png')


        
# exit function
def qExit():
    root.destroy()


# labels for heading
lblInfo = Label(root, font=('arial', 30, 'bold'),
                text="  RESUME SCREENING ",
                fg="Black", bd=10, anchor='w')
lblInfo.grid(row=1, column=2)



# labels line 1
lblline1 = Label(root, font=('arial', 16, 'bold'),
                 text="==============================", bd=16, anchor="w")
lblline1.grid(row=3, column=2)



# labels for the key entry
lblkey = Label(root, font=('arial', 12, 'bold'),
               text="CHOOSE THE RESUME", bd=16, anchor="w")
lblkey.grid(row=6, column=1)


# resume button
btnchoose2 = Button(root, padx=16, bd=10, fg="white", font=('arial', 10, 'bold'), width=7, text="CHOOSE", bg="grey",command = openfile_resume)
btnchoose2.grid(row=6, column=2)


# resume button
btnchoose3 = Button(root, padx=16, bd=10, fg="white", font=('arial', 10, 'bold'), width=7, text="SCREEN", bg="grey",command = ' lambda :screen(resume_final())')
btnchoose3.grid(row=8, column=2)


# labels line 2
lblline2 = Label(root, font=('arial', 16, 'bold'),
                 text="==============================", bd=16, anchor="w")
lblline2.grid(row=7, column=2)


# labels for Name
lblname = Label(root, font=('arial', 16, 'bold'),
               text="Ridhanshu Jasrotia (2017359)", bd=16, anchor="w")
lblname.grid(row=9, column=2)


# Exit button
btnExit = Button(root, padx=16, bd=10, fg="white", font=('arial', 10, 'bold'), width=7, text="Exit", bg="grey",
                 command=qExit)
btnExit.grid(row=8, 
column=3)


# keeps window alive
root.mainloop()