import textwrap
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# template code
# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(10.3,14.8))#8.5, 11

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#06145c', alpha=0.25, linewidth=420)#360
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')
# remove axe
plt.axis('off')

# details
#header
note = '(This resume was generated entirely in Python. For sourcecode, view my Github.)'
Name = 'VICTOR DANIEL'
jobtitle = 'PYTHON DEVELOPER'


plt.annotate(note, (.02,.99), weight='regular', fontsize=9, alpha=.5)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=24)
plt.annotate(jobtitle, (.03,.91), weight='regular', fontsize=10)
contact='Hyderabad, India'
plt.annotate(contact, (.64,.98), weight='regular', fontsize=11, color='#6155a6')
contact='8331013305'
plt.annotate(contact, (.64,.96), weight='regular', fontsize=11, color='#6155a6')
contact='vemavarapu.12345@gmail.com'
plt.annotate(contact, (.64,.94), weight='regular', fontsize=11, color='#6155a6')
contact='linkedin.com/in/victor-daniel-67829a174'
plt.annotate(contact, (.64,.92), weight='regular', fontsize=11, color='#6155a6')
contact='github.com/vemavarapu-daniel'
plt.annotate(contact, (.64,.90), weight='regular', fontsize=11,color='#6155a6')






education_title = 'EDUCATION'
education1='B.Tech - CMR Institution Of Technology'
education1_1='Major - Computer Science and Engineering'
education1_2='Percentage - 6.4 CGPA. Year of passing-2022'

plt.annotate(education_title, (.02,.86), weight='bold', fontsize=12, color='#6155a6')
plt.annotate(education1, (.05,.84), weight='regular', fontsize=10, color='#6155a6')
plt.annotate(education1_1, (.06,.82), weight='regular', fontsize=10, color='#6155a6')
plt.annotate(education1_2, (.06,.80), weight='regular', fontsize=10, color='#6155a6')
education2='XII - bharath ratna jr college(TSBIE)'
education2_1='Science and Mathematics'
education2_2='Percentage - 67.7 %. Year of passing-2018'
plt.annotate(education2, (.05,.78), weight='regular', fontsize=10, color='#6155a6')
plt.annotate(education2_1, (.06,.76), weight='regular', fontsize=10, color='#6155a6')
plt.annotate(education2_2, (.06,.74), weight='regular', fontsize=10, color='#6155a6')
education3='X - Jeevadan High School (SSC)'
education3_1='Percentage - 7.0 CGPA. Year of passing-2016'
plt.annotate(education3, (.05,.72), weight='regular', fontsize=10, color='#6155a6')
plt.annotate(education3_1, (.06,.70), weight='regular', fontsize=10, color='#6155a6')

projecttitle='PROJECTS'
project1='Resume Builder'
project1disc='This project will help users to build great resumes (this resume is built using this project). This project is\
 coded completely in python and plotted using matplotlib library .'
project1disc=(textwrap.fill(project1disc, 60))
plt.annotate(projecttitle, (.02,.66), weight='bold', fontsize=12, color='#6155a6')
plt.annotate(project1, (.05,.638), weight='regular', fontsize=10.5, color='#6155a6')
plt.annotate(project1disc, (.06,.595), weight='regular', fontsize=10, color='#6155a6')
project2='Word of the day'
project2disc= 'This project sends word and its meaning to given mail\
 as well as notification to the computer everyday to improve vocabulary.'
project2disc=textwrap.fill(project2disc,48)
plt.annotate(project2, (.05,.573), weight='regular', fontsize=10.5, color='#6155a6')
plt.annotate(project2disc, (.06,.530), weight='regular', fontsize=10, color='#6155a6')

intershiptitle='INTERNSHIP'
intern1='Bhrath Electronic Limited'
intern1disc='As part of my internship, I got hands on experience of electronic warfare system called \'PROJECT SAMYUTHA\' , as well as \
learning the working models and instruments behind the Missile Technology.'
intern1disc=textwrap.fill(intern1disc,54)
plt.annotate(intershiptitle, (.02,.49), weight='bold', fontsize=12, color='#6155a6')
plt.annotate(intern1, (.05,.465), weight='regular', fontsize=10.5, color='#6155a6')
plt.annotate(intern1disc, (.06,.409), weight='regular', fontsize=10, color='#6155a6')



voltitle='VOLUNTEERED ORGANIZATIONS'
vol1='Aira Foundation'
vol1disc='Aira is a social NGO which works for social cause.\nRole - Board Member'
vol2='U25CMR'
vol2disc='U25cmr is huge youth group in India aimed a sharing ideas and inspiring each other to make a\
difference in the world. \nRole - Tech lead'
vol2disc=textwrap.fill(vol2disc,50)
vol3='Trace Labs'
vol3disc='Trace Labs is a nonprofit organization whose mission is to find missing persons using google\
 and deep web hacking. Role - stage1/3 member'
vol3disc=textwrap.fill(vol3disc,50)
plt.annotate(voltitle, (.02,.367), weight='bold', fontsize=11.5, color='#6155a6')
plt.annotate(vol1, (.05,.345), weight='regular', fontsize=10, color='#6155a6')
plt.annotate(vol1disc, (.06,.315), weight='regular', fontsize=10, color='#6155a6')
plt.annotate(vol2, (.05,.293), weight='regular', fontsize=10, color='#6155a6')
plt.annotate(vol2disc, (.06,.248), weight='regular', fontsize=10, color='#6155a6')
plt.annotate(vol3, (.05,.230), weight='regular', fontsize=10, color='#6155a6')
plt.annotate(vol3disc, (.06,.190), weight='regular', fontsize=10, color='#6155a6')

techtitle='TECHNICAL SKILLS'
tech='PYTHON'
plt.annotate(techtitle, (0.64,.85), weight='bold', fontsize=13, color='#6155a6')
plt.annotate(tech, (.66,.825), weight='regular', fontsize=9, color='#6155a6')
circle=Circle((.79,0.83),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.81,0.83),.0053, color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.83,0.83),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.85,0.83),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.87,0.83),.0052, fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)

tech='HTML'
plt.annotate(tech, (.66,.805), weight='regular', fontsize=9, color='#6155a6')
circle=Circle((.79,0.81),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.81,0.81),.0053, color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.83,0.81),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.85,0.81),.0053,fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.87,0.81),.0052, fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)

tech='CSS'
plt.annotate(tech, (.66,.785), weight='regular', fontsize=9, color='#6155a6')
circle=Circle((.79,0.79),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.81,0.79),.0053, color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.83,0.79),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.85,0.79),.0053,fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.87,0.79),.0052, fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)


tech='BOOTSTRAP'
plt.annotate(tech, (.66,.765), weight='regular', fontsize=9, color='#6155a6')
circle=Circle((.79,0.77),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.81,0.77),.0053, color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.83,0.77),.0053,fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.85,0.77),.0053,fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.87,0.77),.0052, fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)

tech='C LANGUAGE'
plt.annotate(tech, (.66,.745), weight='regular', fontsize=8.5, color='#6155a6')
circle=Circle((.79,0.75),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.81,0.75),.0053, fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.83,0.75),.0053,fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.85,0.75),.0053,fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.87,0.75),.0052, fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)

tech='DJANGO'
plt.annotate(tech, (.66,.7255), weight='regular', fontsize=9, color='#6155a6')
circle=Circle((.79,0.73),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.81,0.73),.0053,fill=False, color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.83,0.73),.0053,fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.85,0.73),.0053,fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.87,0.73),.0052, fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)

tech='DATA SCIENCE'
plt.annotate(tech, (.66,.7055), weight='regular', fontsize=8, color='#6155a6')
circle=Circle((.79,0.71),.0053,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.81,0.71),.0053,fill=False, color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.83,0.71),.0053,fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.85,0.71),.0053,fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)
circle=Circle((.87,0.71),.0052, fill=False,color='#a1a1a1')
plt.gca().add_patch(circle)

nontechtitle='NON-TECHNICAL SKILLS'
plt.annotate(nontechtitle, (0.64,.66), weight='bold', fontsize=11, color='#6155a6')
nontech='COMMUNICATION'
plt.annotate(nontech, (.66,.64), weight='regular', fontsize=9, color='#6155a6')
nontech='TIME MANAGEMENT'
plt.annotate(nontech, (.66,.62), weight='regular', fontsize=9, color='#6155a6')
nontech='CO-OPERATION'
plt.annotate(nontech, (.66,.60), weight='regular', fontsize=9, color='#6155a6')
nontech='ADAPTABILITY'
plt.annotate(nontech, (.66,.58), weight='regular', fontsize=9, color='#6155a6')
nontech='STORY TELLING'
plt.annotate(nontech, (.66,.56), weight='regular', fontsize=9, color='#6155a6')
nontech='PROBLEM-SOLVING'
plt.annotate(nontech, (.66,.54), weight='regular', fontsize=9, color='#6155a6')
nontech='LEADERSHIP'
plt.annotate(nontech, (.66,.52), weight='regular', fontsize=9, color='#6155a6')

hobtitle='HOBBIES'
plt.annotate(hobtitle, (0.645,.48), weight='bold', fontsize=11, color='#6155a6')
hob='~ Knowing about military technologies'
plt.annotate(hob, (.66,.46), weight='regular', fontsize=10, color='#6155a6')
hob='~ Knowing about Space and aliens'
plt.annotate(hob, (.66,.44), weight='regular', fontsize=10, color='#6155a6')
hob='~ Playing badminton'
plt.annotate(hob, (.66,.42), weight='regular', fontsize=10, color='#6155a6')
hob='~ Cooking food'
plt.annotate(hob, (.66,.40), weight='regular', fontsize=10, color='#6155a6')
hob='~ Making music'
plt.annotate(hob, (.66,.38), weight='regular', fontsize=10, color='#6155a6')

plt.axhline(y=.1, xmin=0, xmax=1, color='#ffffff', linewidth=50)
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
arr_code = mpimg.imread('qrcode_linktr.ee.png')
imagebox = OffsetImage(arr_code, zoom=0.21)
ab = AnnotationBbox(imagebox, (0.82, 0.10))
ax.add_artist(ab)
click='Click or Scan'
plt.annotate(click, (.772,.022), weight='regular', fontsize=10)














plt.savefig('beta1.pdf', dpi=500, bbox_inches='tight')
