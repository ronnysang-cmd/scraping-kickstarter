from bs4 import BeautifulSoup
import ipdb

# projects: kickstarter.select("li.project.grid_4")[0]
# title: project.select("h2.bbcard_name strong a")[0].text
# image link: project.select("div.project-thumbnail a img")[0]['src']
# description: project.select("p.bbcard_blurb")[0].text
# location: project.select("ul.project-meta span.location-name")[0].text
# percent_funded: project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")

def create_project_dict():
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()

    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}
    # Iterate through the projects
    for project in kickstarter.select("li.project.grid_4"):
        title_elem = project.select("h2.bbcard_name strong a")
        img_elem = project.select("div.project-thumbnail a img")
        desc_elem = project.select("p.bbcard_blurb")
        loc_elem = project.select("ul.project-meta span.location-name")
        fund_elem = project.select("ul.project-stats li.first.funded strong")
        
        if title_elem and img_elem and desc_elem and loc_elem and fund_elem:
            title = title_elem[0].text
            projects[title] = {
                'image_link': img_elem[0]['src'],
                'description': desc_elem[0].text,
                'location': loc_elem[0].text,
                'percent_funded': fund_elem[0].text.replace("%","")
            }

    # return the projects dictionary
    return projects

