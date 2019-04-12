def scrape():    
    {
    "cells": [
    {
    "cell_type": "code",
    "execution_count": 3,
    "metadata": {},
    "outputs": [],
    "source": [
        "from bs4 import BeautifulSoup\n",
        "import requests\n",
        "from splinter import Browser\n",
        "from splinter.exceptions import ElementDoesNotExist"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 4,
    "metadata": {},
    "outputs": [],
    "source": [
        "url = \"https://mars.nasa.gov/news\""
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 5,
    "metadata": {},
    "outputs": [],
    "source": [
        "response = requests.get(url)"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 6,
    "metadata": {},
    "outputs": [],
    "source": [
        "soup = BeautifulSoup(response.text, 'html.parser')"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 7,
    "metadata": {},
    "outputs": [
        {
        "data": {
        "text/plain": [
        "'News  – NASA’s Mars Exploration Program'"
        ]
        },
        "execution_count": 7,
        "metadata": {},
        "output_type": "execute_result"
        }
    ],
    "source": [
        "Marstitle = soup.title.text.strip()\n",
        "Marstitle"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": []
    },
    {
    "cell_type": "code",
    "execution_count": 8,
    "metadata": {},
    "outputs": [
        {
        "data": {
        "text/plain": [
        "'Managed by the Mars Exploration Program and the Jet Propulsion Laboratory for NASA’s Science Mission Directorate'"
        ]
        },
        "execution_count": 8,
        "metadata": {},
        "output_type": "execute_result"
        }
    ],
    "source": [
        "MarsP = soup.p.text.strip()\n",
        "MarsP"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 9,
    "metadata": {},
    "outputs": [],
    "source": [
        "from splinter import Browser\n",
        "from bs4 import BeautifulSoup"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 10,
    "metadata": {},
    "outputs": [],
    "source": [
        "executable_path = {'executable_path': 'chromedriver.exe'}\n",
        "browser = Browser('chrome', **executable_path, headless=False)"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 11,
    "metadata": {},
    "outputs": [],
    "source": [
        "url = \"http://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
        "browser.visit(url)"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 14,
    "metadata": {},
    "outputs": [],
    "source": [
        "   \n",
        "html = browser.html\n",
        "soup = BeautifulSoup(html, 'html.parser')\n",
        " \n",
        "\n",
        "browser.click_link_by_partial_text('FULL IMAGE')\n",
        "    \n",
        " "
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 15,
    "metadata": {},
    "outputs": [],
    "source": [
        "   browser.click_link_by_partial_text('more info')\n",
        "    "
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 16,
    "metadata": {},
    "outputs": [],
    "source": [
        "html = browser.html\n",
        "soup = BeautifulSoup(html, 'html.parser')\n",
        "images = soup.findAll(attrs ={\"main_image\"})\n",
        "for image in images:\n",
        "    url_image = image.attrs['src']\n",
        "    featured_image = ['https://www.jpl.nasa.gov/' + url_image]     \n",
        "    "
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 17,
    "metadata": {},
    "outputs": [
        {
        "data": {
        "text/plain": [
        "['https://www.jpl.nasa.gov//spaceimages/images/largesize/PIA00063_hires.jpg']"
        ]
        },
        "execution_count": 17,
        "metadata": {},
        "output_type": "execute_result"
        }
    ],
    "source": [
        "featured_image"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 18,
    "metadata": {},
    "outputs": [],
    "source": [
        "url = \"https://twitter.com/marswxreport?lang=en\"\n",
        "browser.visit(url)\n",
        "html = browser.html\n",
        "soup = BeautifulSoup(html, 'html.parser')"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 19,
    "metadata": {},
    "outputs": [
        {
        "data": {
        "text/plain": [
        "'InSight sol 114 (2019-03-23) low -96.8ºC (-142.2ºF) high -15.5ºC (4.1ºF)\\npressure at 7.30 hPapic.twitter.com/pZKYYDzZST'"
        ]
        },
        "execution_count": 19,
        "metadata": {},
        "output_type": "execute_result"
        }
    ],
    "source": [
        "results = soup.find_all('li', class_='js-stream-item stream-item stream-item ')\n",
        "for result in results:\n",
        "    mars_weather = result.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text\n",
        "\n",
        "mars_weather"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 20,
    "metadata": {},
    "outputs": [],
    "source": [
        "url = \"https://space-facts.com/mars/\"\n",
        "browser.visit(url)\n",
        "html = browser.html\n",
        "soup = BeautifulSoup(html, 'html.parser')"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 21,
    "metadata": {},
    "outputs": [],
    "source": [
        "import pandas as pd"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 22,
    "metadata": {},
    "outputs": [
        {
        "data": {
        "text/plain": [
        "[                      0                              1\n",
        " 0  Equatorial Diameter:                       6,792 km\n",
        " 1       Polar Diameter:                       6,752 km\n",
        " 2                 Mass:  6.42 x 10^23 kg (10.7% Earth)\n",
        " 3                Moons:            2 (Phobos & Deimos)\n",
        " 4       Orbit Distance:       227,943,824 km (1.52 AU)\n",
        " 5         Orbit Period:           687 days (1.9 years)\n",
        " 6  Surface Temperature:                  -153 to 20 °C\n",
        " 7         First Record:              2nd millennium BC\n",
        " 8          Recorded By:           Egyptian astronomers]"
        ]
        },
        "execution_count": 22,
        "metadata": {},
        "output_type": "execute_result"
        }
    ],
    "source": [
        "tables = pd.read_html(url)\n",
        "tables"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 23,
    "metadata": {},
    "outputs": [],
    "source": [
        "df = tables[0]"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 24,
    "metadata": {},
    "outputs": [],
    "source": [
        "df.columns = ['Description', 'Data']"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 25,
    "metadata": {},
    "outputs": [
        {
        "data": {
        "text/html": [
        "<div>\n",
        "<style scoped>\n",
        "    .dataframe tbody tr th:only-of-type {\n",
        "        vertical-align: middle;\n",
        "    }\n",
        "\n",
        "    .dataframe tbody tr th {\n",
        "        vertical-align: top;\n",
        "    }\n",
        "\n",
        "    .dataframe thead th {\n",
        "        text-align: right;\n",
        "    }\n",
        "</style>\n",
        "<table border=\"1\" class=\"dataframe\">\n",
        "  <thead>\n",
        "    <tr style=\"text-align: right;\">\n",
        "      <th></th>\n",
        "      <th>Description</th>\n",
        "      <th>Data</th>\n",
        "    </tr>\n",
        "  </thead>\n",
        "  <tbody>\n",
        "    <tr>\n",
        "      <th>0</th>\n",
        "      <td>Equatorial Diameter:</td>\n",
        "      <td>6,792 km</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>1</th>\n",
        "      <td>Polar Diameter:</td>\n",
        "      <td>6,752 km</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>2</th>\n",
        "      <td>Mass:</td>\n",
        "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>3</th>\n",
        "      <td>Moons:</td>\n",
        "      <td>2 (Phobos &amp; Deimos)</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>4</th>\n",
        "      <td>Orbit Distance:</td>\n",
        "      <td>227,943,824 km (1.52 AU)</td>\n",
        "    </tr>\n",
        "  </tbody>\n",
        "</table>\n",
        "</div>"
        ],
        "text/plain": [
        "            Description                           Data\n",
        "0  Equatorial Diameter:                       6,792 km\n",
        "1       Polar Diameter:                       6,752 km\n",
        "2                 Mass:  6.42 x 10^23 kg (10.7% Earth)\n",
        "3                Moons:            2 (Phobos & Deimos)\n",
        "4       Orbit Distance:       227,943,824 km (1.52 AU)"
        ]
        },
        "execution_count": 25,
        "metadata": {},
        "output_type": "execute_result"
        }
    ],
    "source": [
        "df.head()"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 26,
    "metadata": {
        "scrolled": true
    },
    "outputs": [
        {
        "data": {
        "text/plain": [
        "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Description</th>\\n      <th>Data</th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>0</th>\\n      <td>Equatorial Diameter:</td>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>1</th>\\n      <td>Polar Diameter:</td>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>2</th>\\n      <td>Mass:</td>\\n      <td>6.42 x 10^23 kg (10.7% Earth)</td>\\n    </tr>\\n    <tr>\\n      <th>3</th>\\n      <td>Moons:</td>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>4</th>\\n      <td>Orbit Distance:</td>\\n      <td>227,943,824 km (1.52 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>5</th>\\n      <td>Orbit Period:</td>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>6</th>\\n      <td>Surface Temperature:</td>\\n      <td>-153 to 20 °C</td>\\n    </tr>\\n    <tr>\\n      <th>7</th>\\n      <td>First Record:</td>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>8</th>\\n      <td>Recorded By:</td>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
        ]
        },
        "execution_count": 26,
        "metadata": {},
        "output_type": "execute_result"
        }
    ],
    "source": [
        " html_table = df.to_html()\n",
        "html_table"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 27,
    "metadata": {},
    "outputs": [],
    "source": [
        "url = \"https://astrogeology.usgs.gov/search/results/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
        "browser.visit(url)\n",
        "html = browser.html\n",
        "soup = BeautifulSoup(html, 'html.parser')"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 28,
    "metadata": {},
    "outputs": [],
    "source": [
        "\n",
        "test = browser.find_by_css('div.description')\n",
        " "
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 29,
    "metadata": {},
    "outputs": [],
    "source": [
        "hemisphere_list = []\n",
        "for i in range(len(test)):\n",
        "    dict1 = {}\n",
        "    browser.find_by_css('div.description')[i].find_by_css('h3').click()\n",
        "    sample = browser.find_link_by_text('Sample').first\n",
        "    dict1['image_url'] = sample['href']\n",
        "    #print(sample['href'])                                           \n",
        "    text = browser.find_by_css('h2.title').text\n",
        "    dict1['title'] = text\n",
        "    hemisphere_list.append(dict1)\n",
        "    browser.back()"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 30,
    "metadata": {},
    "outputs": [
        {
        "data": {
        "text/plain": [
        "[{'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',\n",
        "  'title': 'Cerberus Hemisphere Enhanced'},\n",
        " {'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',\n",
        "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
        " {'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',\n",
        "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
        " {'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',\n",
        "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
        ]
        },
        "execution_count": 30,
        "metadata": {},
        "output_type": "execute_result"
        }
    ],
    "source": [
        "hemisphere_list"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": []
    }
    ],
    "metadata": {
    "kernelspec": {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
    },
    "language_info": {
    "codemirror_mode": {
        "name": "ipython",
        "version": 3
    },
    "file_extension": ".py",
    "mimetype": "text/x-python",
    "name": "python",
    "nbconvert_exporter": "python",
    "pygments_lexer": "ipython3",
    "version": "3.7.0"
    }
    },
    "nbformat": 4,
    "nbformat_minor": 2
    }


