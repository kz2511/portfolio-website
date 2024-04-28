import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from streamlit_extras.mention import mention
import requests



# Set page title
st.set_page_config(page_title="Kunal Zaveri", page_icon="desktop_computer", layout="wide", initial_sidebar_state="auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)


# def load_lottieurl(url):
#     r = requests.get(url)
#     return None if r.status_code != 200 else r.json()
#
#
# def render_lottie(url, width, height):
#     return f"""
#     <html>
#     <head>
#         <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
#     </head>
#     <body>
#         <div id="lottie-container" style="width: {width}; height: {height};"></div>
#         <script>
#             var animation = lottie.loadAnimation({{
#                 container: document.getElementById('lottie-container'),
#                 renderer: 'svg',
#                 loop: true,
#                 autoplay: true,
#                 path: '{url}'
#             }});
#             animation.setRendererSettings({{
#                 preserveAspectRatio: 'xMidYMid slice',
#                 clearCanvas: true,
#                 progressiveLoad: false,
#                 hideOnTransparent: true
#             }});
#         </script>
#     </body>
#     </html>
#     """


# Use local CSS
    # def local_css(file_name):
    #     with open(file_name) as f:
    #         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    #
    #
    # local_css("style/style.css")


# PDF functions
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" type="application/pdf" width="1000" height="900"></embed>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    return f'<a href="{pdf_url}" target="_blank">{link_text}</a>'


img_utown = Image.open("IMG_20230105_234243_827.jpg")
img_lh = Image.open("IMG_20240119_213657_223 (1).jpg")
img_poc = Image.open("images.jpg")
img_groundup = Image.open("download-removebg-preview.png")
img_linkedin = Image.open("linkedin.png")
img_github = Image.open("github.png")
img_email = Image.open("email.png")


def social_icons(width=24, height=24, **kwargs):
    icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

    icons_html = ""
    for name, url in kwargs.items():
        if icon_src := {
            "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
            "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
            "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png",
        }.get(name.lower()):
            icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width,
                                               height=height)

    return icons_html


def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
    with col2:
        b_no_commas = b.replace(',', '')
        st.markdown(b_no_commas)


def txt4(a, b):
    col1, col2 = st.columns([1.5, 2])
    with col1:
        st.markdown(f'<p style="font-size: 25px; color: black;">{a}</p>', unsafe_allow_html=True)
    with col2:  # can't seem to change color besides green
        st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)




# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1, 3, 1))
        with l:
            st.empty()
        with m:
            st.image(img_lh, width=175)
        with r:
            st.empty()

    choose = option_menu(
        "Kunal Zaveri",
        ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Resume", "Contact"],
        icons=['person fill', 'clock history', 'tools', 'book half', 'clipboard', 'paperclip', 'envelope'],
        menu_icon="mortarboard",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f5f5dc"},
            "icon": {"color": "darkorange", "font-size": "20px"},
            "nav-link": {"font-size": "17px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#cfcfb4"},
        }
    )
    linkedin_url = "https://www.linkedin.com/in/kz2511/"
    github_url = "https://github.com/kz2511"
    email_url = "mailto:kunalzaveri11@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11, 2, 0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Kunal Zaveri")
# Create header
if choose == "About Me":
    with st.container():
        left_column, middle_column, right_column = st.columns((1, 0.2, 0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Python Developer and Data Science Enthusiast")
            st.write(
                "👋🏻 Hi, I am  Kunal Zaveri, a seasoned Python Developer with 2+ years of hands-on experience. Specializing in crafting robust applications using Python, Django, DRF, and Flask, I excel in delivering efficient solutions tailored to client needs. Proficient in RESTful services, I leverage my expertise to build scalable web applications while also mastering web scraping techniques using Scrapy, Playwright, and Selenium. With a keen eye for detail and a knack for problem-solving, I ensure the delivery of high-quality, reliable software solutions every time")
            st.write(
                "🏋🏻 In addition, I like to exercise in the gym, run, write, listen music and... enjoy eating good food in my free time!")
            st.write(
                "📄 [Kunal Zaveri Resume](https://drive.google.com/file/d/1-sTLi33kFAI4OSPCZumLV_Bw99_pzwHR/view?usp=sharing)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_utown)

# Create section for Work Experience
elif choose == "Experience":
    # st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((2, 4))
        with image_column:
            st.image(img_groundup, use_column_width='always')
        with text_column:
            st.subheader("Associate Software Engineer(Python), [Inexture Solutions](https://www.inexture.com/)")
            st.write("*July 2022 to Present*")
            st.markdown("""
            - Designed, coded, and debugged a wide range of applications, including operations, reporting, data analysis, and web applications, using Python to ensure optimal performance and functionality.
            - Showcased expertise in delivering effective web scraping solutions, leveraging libraries like BeautifulSoup, Scrapy, and Playwright to extract valuable data from diverse sources.
            - Demonstrated strong communication skills by effectively handling client inquiries and providing accurate time estimations for project completion, ensuring transparency and client satisfaction throughout the development process.
            - Utilized Version Control Systems like GIT proficiently to maintain organized code versions and configurations, facilitating collaboration and code management within development teams.
            - Leveraged a comprehensive skill set encompassing Object-Oriented Python, Django, PostgreSQL, Exception Handling, and Collections to develop robust RESTful services, ensuring scalability and efficiency in software development projects.
            """)
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)

# Create section for Technical Skills
elif choose == "Technical Skills":
    # st.write("---")
    st.header("Technical Skills")
    txt3("Programming Languages", "`Python`, `SQL`")
    txt3("Data Visualization",
         "`ggplot2`, `matplotlib`, `seaborn`, `Plotly`,`Tableau`, `Power BI`, `Google Data Studio`")
    txt3("Database Systems",
         "`MySQL`, `PostgreSQL`, `SQLite`, `NoSQL`")
    txt3("Cloud Platforms",
         "`Amazon Web Services`, `Heroku`, `Streamlit Cloud`")
    txt3("Version Control", "`Git`, `Docker`")
    txt3("Design and Front-end Development", "`HTML`, `CSS`, `Streamlit`")
    txt3("Data Science Techniques",
         "`Regression`, `Clustering`, `Association Rules Mining`, `Random Forest`, `Decison Trees`, `Sentiment Analysis`")
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`")
    txt3("Task Management Tools", "`Asana`, `Slack`, `Jira`, `Trello` ")


elif choose == "Education":
    st.header("Education")
    with st.container():
        image_column, text_column = st.columns((2, 4))
        with image_column:
            st.image(img_poc, use_column_width='always')
        with text_column:
            st.subheader(
                "Bachelor of Engineering in Information Technology, [Ganpat University (GUNI), India](https://www.ganpatuniversity.ac.in/)")
            st.write(
                "Coursework: Mathematics for Engineers, Physics for Engineers, Data Structures and Algorithms, Database Management Systems, Operating Systems, Software Engineering Principles, Web Technologies, Cloud Computing, Artificial Intelligence and Machine Learning, Capstone Project")
            st.markdown("""
                   - [NSS](https://nss.gov.in/) - During NSS, I explored many things: communication skills, time management skills, working across teams, overcoming stage fright, management skills, and adapting to village life
                   - Throughout college, I explored numerous experiences, learned new things, attended classes, and enjoyed spending time with friends.
                   """)


elif choose == "Projects":
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3, 1))
        with text_column:
            st.header("**1) Language Data Extraction**")
            st.markdown("""
                - This project involves scraping data from two websites. We extract words from one site and compare them with content from the other. If there's a match, we create a docx file mirroring the original website's structure, font, and layout. We also check if existing docx sentences match scraped words, adding matching sentences to the new docx. Additionally, we convert any phonetic letters in scraped words to their normal form for readability.
            """)
            st.subheader("*Roles and Responsibilities in the Project*")
            st.markdown("""
                - Created the documentation of scrap words from the website 
                - We also need to change phonetic letters into normal letters while scrapping words from the website 
                - Created the docx from the given words scraped by and created individually docs for every individual word 
                - While scrapping from a website and creating a docx of every word we should need to make sure the docx should have some content as the website has where bold or italic letters are present there should be bold and italic letters available in the docx file also 
                - We also need to check some phonetic words should remain the same while saving the docx files 
                - We need to create different variations of the source words and match all the variations in the given source sentences docx if any word matched with any sentences present in the word and send that sentences in our created target docx. There are also some conditions while pasting the source sentences in the docx.
            """)
            st.write("Technology Used: Python, Scrapy, Selenium, BeautifulSoup")

    with st.container():
        text_column, image_column = st.columns((3, 1))
        with text_column:
            st.header("**2) Data Extraction Tool**")
            st.markdown("""
                - This advanced system extracts valuable data from diverse websites, utilizing Scrapy for structured information retrieval and Selenium for dynamic content capture. The scraped data seamlessly integrates into an ElasticSearch-based search engine through Django Rest Framework. The project stands as a testament to my skills in web scraping, automation, and building efficient search solutions, providing users with a refined and efficient experience in accessing and navigating vast amounts of data.
             """)
            st.subheader("*Roles and Responsibilities in the Project*")
            st.markdown("""
                - Employed Scrapy for structured data extraction and Selenium for dynamic content capture, ensuring comprehensive coverage of the target website. Additionally, successfully tackled the challenging task of extracting data from PDFs by identifying common structures and implementing a strategy for data retrieval.
                - Implemented data transformation processes to organize and structure the scraped information for efficient storage and retrieval.
                - Designed and implemented integration with ElasticSearch, ensuring optimal indexing and mapping of scraped data into Elasticsearch for fast and accurate search functionalities.
                - Developed a user-friendly search engine using ElasticSearch, enabling users to interact with and retrieve information effortlessly.
                - Implemented advanced search functionalities, such as full-text search, filters, and sorting, to enhance the user experience.
                - Conducted thorough testing of the scraping tool to ensure accurate data extraction, handling edge cases to improve data quality.
             """)
            st.write("*Technology Used:-* Selenium, Scrapy, ElasticSearch, BeautifulSoup, Django Rest Framework. ")

    with st.container():
        text_column, image_column = st.columns((3, 1))
        with text_column:
            st.header("**3) Online Marketplace Data Extraction**")
            st.markdown("""
                - In this project, our objective was to scrape product numbers from various E-commerce websites using Scrapy and Selenium. The task involved extracting data for specific URLs provided. When a user pastes a URL from the target site, the information for that particular product is scraped and made visible to the end user. Additionally, we implemented an API to send the scraping response, ensuring that the end user can view this information seamlessly
               """)
            st.subheader("*Roles and Responsibilities in the Project*")
            st.markdown("""
                   - We started with Selenium for scraping over 100 ecommerce sites, but faced memory errors on servers.
                   - Transitioned to Scrapy for better resource usage and server compatibility.
                   - Dealt with dynamic content challenges by moving from Selenium to Scrapy.
                   - Developed an innovative solution using script tags like application/ld+json for extracting dynamic content.
                   - Created a Universal Scraper using meta tags for extracting data from diverse ecommerce sites, along with a specialized Shopify scraper. 
                """)
            st.write("*Technology Used:-* Scrapy, Selenium, Flask")

    with st.container():
        text_column, image_column = st.columns((3, 1))
        with text_column:
            st.header("**4)Scrap Metal Yard Harvesting**")
            st.markdown("""
                - In this project, I utilized Python, Scrapy, and Selenium to extract data from Facebook and various other sites. I developed a PostgreSQL pipeline to efficiently store and update the extensive data. Implemented a mechanism to drop incomplete data lacking essential fields. Demonstrates expertise in large-scale data extraction, storage, and maintenance.
               """)
            st.subheader("*Roles and Responsibilities in the Project*")
            st.markdown("""
                   - When scraping data from websites, it's important to ensure that if required fields' data is not available, it is not scraped and added to the database.
                   - When scraping data from Facebook, we need to ensure that our session ID is not detected.
                   - I've implemented a pipeline in the code to save data into the database, ensuring there are no duplicate records, and removing data from the database which are not avaiable on the sites.
                   - Additionally, I'm downloading images while scraping from the URL and storing them in an S3 bucket. The links to these images are also stored in the S3 bucket.
                   - The client needs to monitor the scraping process for any errors. We've set up email notifications and Spidermon for monitoring during the scraping process.
                   - To ensure ease of future modifications, I've structured the project so that if anything changes on the website, the client only needs to modify one section of the code, and the code will run smoothly again
                """)
            st.write("*Technology Used:-*  Scrapy, Selenium, AWS, Spidermon")



elif choose == "Resume":
    resume_url = "https://drive.google.com/file/d/1-sTLi33kFAI4OSPCZumLV_Bw99_pzwHR/view?usp=sharing"
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume (1 page)**"), unsafe_allow_html=True)
    show_pdf("KunalZaveri_resume.pdf")
    with open("KunalZaveri_resume.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume (1 page)",
            data=file,
            file_name="KunalZaveri_resume.pdf",
            mime="application/pdf"
        )

elif choose == "Contact":
    # Create section for Contact
    # st.write("---")
    st.header("Contact")


    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            if icon_src := dict(
                    linkedin="https://cdn-icons-png.flaticon.com/512/174/174857.png",
                    github="https://cdn-icons-png.flaticon.com/512/25/25231.png",
                    email="https://cdn-icons-png.flaticon.com/512/561/561127.png",
            ).get(name.lower()):
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width,
                                                   height=height)

        return icons_html


    with st.container():
        text_column, mid, image_column = st.columns((1, 0.2, 0.5))
        with text_column:
            st.write(
                "Let's connect! You may either reach out to me at kunalzaveri11@gmail.com")
            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/kz2511/"
            github_url = "https://github.com/kz2511"
            email_url = "mailto:kunalzaveri11@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
        with mid:
            st.empty()

st.markdown("*Copyright © 2024 Kunal Zaveri*")
