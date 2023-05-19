from flask import Flask, jsonify
import json
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# <div category = "anxious, uncertain" class = "prayer" data-id = "23" >
# <h1 class = "prayer-title" key = "title" url = "/prayers/23" >
#             "Windex for Negativity"
#         </h1>
# <p class="arabic" key="arabic" url="/prayers/23"> اللهم اغسلني من السلبية </p>
# <p class="transliteration" key="transliteration" url="/prayers/23">
#                             Allahumma iGsilnee min assalbiyah
#                         </p>
# <p class="translation" key="translation" url="/prayers/23">Oh Allah wash away my negativity.</p>
# <section class="audio-box" src="">
# <audio controls="">
# <source src="" type="audio/mpeg"/>
# </audio><br/>
# <a class="hidden" data-placement="bottom" data-toggle="download" href="" title="Download Du'a Audio Clip"><br/><i class="fa fa-download fa-4x" style="margin-bottom: 0.1em;"></i></a><br/>
# </section>
# <br/>
# <i class="fa fa-heart fa-5x toggle-heart" data-id="23"></i>
# <p>613
#                     likes
#                 </p><br/>
# <div class="social-share-button" data-desc="" data-img="" data-title="Oh Allah wash away my negativity.
#  اللهم اغسلني من السلبية " data-url="https://www.sujood.co/#id=23" data-via="">
# <a class="ssb-icon ssb-twitter" data-site="twitter" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Twitter"></a>
# <a class="ssb-icon ssb-facebook" data-site="facebook" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Facebook"></a>
# <a class="ssb-icon ssb-google_plus" data-site="google_plus" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Google+"></a>
# <a class="ssb-icon ssb-tumblr" data-site="tumblr" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Tumblr"></a>
# <a class="ssb-icon ssb-pinterest" data-site="pinterest" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Pinterest"></a>
# <a class="ssb-icon ssb-email" data-site="email" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Email"></a>
# </div>
# </div>


# <div category="weak" class="prayer" data-id="35">
# <h1 class="prayer-title" key="title" url="/prayers/35">
#             "You are my Lord"
#         </h1>
# <p class="arabic" key="arabic" url="/prayers/35">اَللّهمَّ إِلَيْكَ أَشْكُوْ ضُعْفَ قُوَّتِيْ ، وَقِلَّةَ حِيْلَتِيْ ، وَهَوَانِيْ عَلَى النَّاسِ ، يَا أَرْحَمَ الرَّاحِمِيْنَ ، أَنْتَ 
# رَبُّ الْمُسْتَضْعَفِيْنَ ، وَأَنْتَ رَبِّي</p>
# <p class="transliteration" key="transliteration" url="/prayers/35">
#                             Allahuma inni ashku ilayka du'fa quwati wa qilata heelati wa hawaani ala annaas. yaa arham araahimin, anta rab almustadafeena wa anta rabi

#                         </p>
# <p class="translation" key="translation" url="/prayers/35">Oh, Allah, I appeal to you for the weakness in my strength,
# and my limited power, and the treatment of contempt and humiliation from people. To you, the most Merciful of all the Merciful ones, you are the Lord of the oppressed, and you are my Lord.</p>
# <section class="audio-box" src="">
# <audio controls="">
# <source src="" type="audio/mpeg"/>
# </audio><br/>
# <a class="hidden" data-placement="bottom" data-toggle="download" href="" title="Download Du'a Audio Clip"><br/><i class="fa fa-download fa-4x" style="margin-bottom: 0.1em;"></i></a><br/>
# </section>
# <br/>
# <i class="fa fa-heart fa-5x toggle-heart" data-id="35"></i>
# <p>1944
#                     likes
#                 </p><br/>
# <div class="social-share-button" data-desc="" data-img="" data-title="Oh, Allah, I appeal to you for the weakness in my strength,
# and my limited power, and the treatment of contempt and humiliation from people. To you, the most Merciful of all the Merciful ones, you are the Lord of the oppressed, and you are my Lord.
# اَللّهمَّ إِلَيْكَ أَشْكُوْ ضُعْفَ قُوَّتِيْ ، وَقِلَّةَ حِيْلَتِيْ ، وَهَوَانِيْ عَلَى النَّاسِ ، يَا أَرْحَمَ الرَّاحِمِيْنَ ، أَنْتَ رَبُّ الْمُسْتَضْعَفِيْنَ ، وَأَنْتَ رَبِّي" data
# -url="https://www.sujood.co/#id=35" data-via="">
# <a class="ssb-icon ssb-twitter" data-site="twitter" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Twitter"></a>
# <a class="ssb-icon ssb-facebook" data-site="facebook" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Facebook"></a>
# <a class="ssb-icon ssb-google_plus" data-site="google_plus" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Google+"></a>
# <a class="ssb-icon ssb-tumblr" data-site="tumblr" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Tumblr"></a>
# <a class="ssb-icon ssb-pinterest" data-site="pinterest" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Pinterest"></a>
# <a class="ssb-icon ssb-email" data-site="email" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Email"></a>
# </div>
# </div>


# <div category="aroused, desire" class="prayer" data-id="31">
# <h1 class="prayer-title" key="title" url="/prayers/31">
#             "Fire Alarm"
#         </h1>
# <p class="arabic" key="arabic" url="/prayers/31">اللهم اطفئ نار الشهوات من قلبى ، واصرف عنه كل شئ لا يرضيك عنى </p>
# <p class="transliteration" key="transliteration" url="/prayers/31">
#                             Allahumma iTfa' naara ash-shahawaati min qalbee, wa aSrid 3anhu kulla shay' la yardeek
#                         </p>
# <p class="translation" key="translation" url="/prayers/31">Oh Allah! Extinguish the fire of desires in my heart and redirect my heart to all that which pleases you.</p>
# <section class="audio-box" src="">
# <audio controls="">
# <source src="" type="audio/mpeg"/>
# </audio><br/>
# <a class="hidden" data-placement="bottom" data-toggle="download" href="" title="Download Du'a Audio Clip"><br/><i class="fa fa-download fa-4x" style="margin-bottom: 0.1em;"></i></a><br/>
# </section>
# <br/>
# <i class="fa fa-heart fa-5x toggle-heart" data-id="31"></i>
# <p>654
#                     likes
#                 </p><br/>
# <div class="social-share-button" data-desc="" data-img="" data-title="Oh Allah! Extinguish the fire of desires in my heart and redirect my heart to all that which pleases you.
# اللهم اطفئ نار الشهوات من قلبى ، واصرف عنه كل شئ لا يرضيك عنى " data-url="https://www.sujood.co/#id=31" data-via="">
# <a class="ssb-icon ssb-twitter" data-site="twitter" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Twitter"></a>
# <a class="ssb-icon ssb-facebook" data-site="facebook" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Facebook"></a>
# <a class="ssb-icon ssb-google_plus" data-site="google_plus" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Google+"></a>
# <a class="ssb-icon ssb-tumblr" data-site="tumblr" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Tumblr"></a>
# <a class="ssb-icon ssb-pinterest" data-site="pinterest" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Pinterest"></a>
# <a class="ssb-icon ssb-email" data-site="email" href="#" onclick="return SocialShareButton.share(this);" rel="nofollow" title="Share to Email"></a>
# </div>
# </div>

@app.route('/')
def index():
    url = 'https://www.sujood.co/'
    response = requests.get(url)

    i = BeautifulSoup(response.text, 'html.parser')
    s1 = i.find_all('div', attrs={'class': 'prayer'})
    print(len(s1))
    

    f = open('sujood.json', encoding="utf8")
    data = json.load(f)

    datas = []
    for i in s1:
        print(i.get('category'),)
        print("\n")
        # soup = BeautifulSoup(i["data"], 'html.parser')
        datas.append({
            'title': i.find('h1').text,
            'arabic': i.find('p', attrs={'class': 'arabic'}).text,
            "transliteration": i.find('p', attrs={'class': 'transliteration'}).text,
            "translation": i.find('p', attrs={'class': 'translation'}).text,
            "audio": i.find('source', attrs={'type': 'audio/mpeg'}).get('src'),
            "category": i.get('category'),
        })

    return jsonify(datas)

if __name__ == '__main__':
    app.run(debug=True)


