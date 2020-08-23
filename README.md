# youtube_search-fork
This fork adds the ability to search for channels, latest content of a channel and adds videos published date.

Python function for searching for youtube videos to avoid using their heavily rate-limited API

To avoid using the API, this uses the form on the youtube homepage and scrapes the resulting page.

## Installation
`pip install youtube-search-fork`

## Example Usage
For a basic search (and all of the current functionality), you can use the search tool as follows:

```python
from youtube_search import YoutubeSearch

videos = YoutubeSearch('search terms', max_results=10).videos_to_json()
channels = YoutubeSearch('search terms', max_results=10).channels_to_json()

print(results)

# returns a json string

########################################

videos = YoutubeSearch('search terms', max_results=10).videos_to_dict()
channels = YoutubeSearch('search terms', max_results=10).channels_to_dict()

print(results)
# returns a dictionary like this:
[{'id': 'UCJWCJC...CieLOLQ', 'name': 'channelName', 'suscriberCountText': '200.000', 'thumbnails': ['URL1', 'URL2'], 'url_suffix': '/user/channelName'}]

#########################################
# Get a channel info and videos:
data = YoutubeSearch.channelInfo(channel_id)

channelInfo = data[0]
print(channelInfo)
$> {'id': 'UCjr2bPAyPV.....8Q', 'name': 'Channel Name', 'avatar': 'https://yt3.ggpht.com/a/AATXAJzuPoT_2M54dus-P2qXgnbY0MPxbkzvwv3muxQn=s176-c-k-c0x00ffffff-no-rj', 'subCount': '24K'}

channelVideoList = data[1]
print(channelVideoList)
$> [{'videoTitle': 'Video title goes here', 'id': 'video_id_here', 'channelName': 'Channel Name', 'views': '17 hours ago', 'timeStamp': '13,661 views', 'videoThumb': 'https://i.ytimg.com/vi/3eC4Hp4MNBA/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4....5o_2mazZd40g_xc_3917M5w', 'channelUrl': '/channel/UCjr2bPA.......gT3W8Q'}, {...}, {...}, ...]
```
