import eyed3
from eyed3.id3.frames import ImageFrame


# source: https://eyed3.readthedocs.io/en/latest/modules.html
# https://stackoverflow.com/questions/38510694/how-to-add-album-art-to-mp3-file-using-python-3
# https://stackoverflow.com/questions/40515738/using-eyed3-to-embed-album-art-from-url
# https://id3.org/id3v2.3.0#Attached_picture

# Another package:
# https://mutagen.readthedocs.io/en/latest/

class MP3tags:
    def __init__(self):
        self.file: str = ''
        self.title: str = ''
        self.artist: str = ''
        self.album_artist: str = ''
        self.image_front_cover: str = ''
        self.album: str = ''
        self.composer: str = ''
        self.publisher: str = ''
        self.genre: str = ''
        self.copyright: str = ''
        self.language: str = ''
        self.artist_url: str = ''
        self.publisher_url: str = ''
        self.recording_date: str = ''
        self.track_num: int = 0
        self.bpm: int = 0

    def get_artist(self):
        return self.artist

    def remove_image(self, objMp3, desc):
        if (objMp3.tag._images.remove(desc)):
            return True
        else:
            return False

    def remove_all_images(self, objMp3):
        toRemove = [x.description for x in objMp3.tag.images]
        counterRemoved = 0
        for desc in toRemove:
            if (objMp3.tag.images.remove(desc)):
                counterRemoved += 1
        return counterRemoved

    def set_file(self, file):
        self.file = file
        if len(file):
            return eyed3.load(file)
        else:
            return False

    def replace_None(self, s):
        if s == None:
            return ''
        else:
            return s

    def get_tags(self):
        audiofile = self.set_file(self.file)
        self.title = audiofile.tag.title
        self.artist = audiofile.tag.artist
        self.album = audiofile.tag.album
        self.album_artist = audiofile.tag.album_artist
        self.composer = audiofile.tag.composer
        self.publisher = audiofile.tag.publisher
        self.genre = audiofile.tag.genre
        self.artist_url = self.replace_None(audiofile.tag.artist_url)
        self.publisher_url = self.replace_None(audiofile.tag.publisher_url)
        self.copyright = audiofile.tag.copyright
        # self.language = self.replace_None(audiofile.tag.language)
        self.recording_date = self.replace_None(audiofile.tag.recording_date)
        self.track_num = audiofile.tag.track_num
        self.bpm = audiofile.tag.bpm

    def set_tags(self):
        audiofile = self.set_file(self.file)
        # audiofile = eyed3.load(self.file)
        if (audiofile.tag == None):
            audiofile.initTag()
        audiofile.tag.title = self.title
        audiofile.tag.artist = self.artist
        audiofile.tag.album = self.album
        audiofile.tag.album_artist = self.album_artist
        audiofile.tag.composer = self.composer
        audiofile.tag.publisher = self.publisher
        audiofile.tag.genre = self.genre
        audiofile.tag.artist_url = self.artist_url
        audiofile.tag.publisher_url = self.publisher_url
        audiofile.tag.copyright = self.copyright
        audiofile.tag.language = self.language
        audiofile.tag.recording_date = self.recording_date
        if self.track_num:
            audiofile.tag.track_num = self.track_num
        if self.bpm:
            audiofile.tag.bpm = self.bpm

        # self.remove_image(audiofile,'front')
        self.remove_all_images(audiofile)
        if len(self.image_front_cover):
            audiofile.tag.images.set(3, open(self.image_front_cover, 'rb').read(), 'image/jpeg', u'front')
        audiofile.tag.save()
        # edit_mp3()
        return True


mp3tags = MP3tags()
mp3tags.file = "song.mp3"
mp3tags.get_tags()
mp3tags.image_front_cover = 'song2.jpg'
mp3tags.title = 'song name'
mp3tags.artist = 'gal sarig'
mp3tags.genre = 'pop'  # or code 13
# mp3tags.track_number=1
mp3tags.set_tags()


# remove all images
def removeAllImages(objMp3):
    toRemove = [x.description for x in objMp3.tag.images]
    counterRemoved = 0
    for desc in toRemove:
        if (objMp3.tag.images.remove(desc)):
            counterRemoved += 1
    return counterRemoved


def edit_mp3():
    audiofile = eyed3.load("song.mp3")
    removeAllImages(audiofile)

    if (audiofile.tag == None):
        audiofile.initTag()

    # print(audiofile.tag.__dict__.keys())
    # print(audiofile.tag)
    # print(len(audiofile.tag.images), 'art picture(s) found')

    audiofile.tag.artist = "שם האומן"
    audiofile.tag.album = "שם האלבום"
    audiofile.tag.album_artist = "שם אומן באלבום"
    audiofile.tag.title = "שם השיר"
    audiofile.tag.composer = 'מלחין'
    audiofile.tag.track_num = 1
    audiofile.tag.recording_date = '2019'
    audiofile.tag.publisher = 'לייבל'
    audiofile.tag.genre = 'Pop'
    audiofile.tag.bpm = 130
    audiofile.tag.artist_url = 'https://GalSarig.com'
    audiofile.tag.publisher_url = 'https://GalSarig.com'
    audiofile.tag.copyright = 'all rights reserved'
    audiofile.tag.language = 'Hebrew'

    # not working
    # audiofile.tag.disc_number = '12345'
    # audiofile.tag.comment = '111'
    # audiofile.tag.comments = '22222'

    # Clear all tags (excluding images)
    # audiofile.tag.clear()

    # not working
    # audiofile.tag.comments = 'הערות'

    # audiofile.tag.images.set(type_=3, img_data=None, mime_type=None, description=u"you can put a description here", img_url=u"https://upload.wikimedia.org/wikipedia/en/6/60/Recovery_Album_Cover.jpg")
    # audiofile.tag.images.set(ImageFrame.FRONT_COVER, open('song.jpg','rb').read(), 'image/jpeg')
    # print('before',audiofile.tag.images[0]._pic_type)
    audiofile.tag.images.set(3, open('song2.jpg', 'rb').read(), 'image/jpeg', u'front')
    # audiofile.tag.images.set(4, open('song.jpg','rb').read(), 'image/jpeg', u'back')
    # audiofile.tag.images.set(5, open('song.jpg','rb').read(), 'image/jpeg', u'test1')
    # audiofile.tag.images.set(6, open('song.jpg','rb').read(), 'image/jpeg', u'test2')
    # print('after',audiofile.tag.images[0]._pic_type)

    audiofile.tag.save()
    return "mp3 edited"


# Remove images
# remove a single image - in the brackets - the description of the image as set by the set command
# print(audiofile.tag._images.remove('back'), 'removed')

def removeImage(objMp3, desc):
    if (objMp3.tag._images.remove(desc)):
        return True
    else:
        return False

# imageDescriptions = [x.description for x in audiofile.tag.images]
# print('before removing.. ' , len(imageDescriptions) , 'image description(s) found: ' , imageDescriptions)
# print(removeAllImages(audiofile), 'image(s) removed')
# imageDescriptions = [x.description for x in audiofile.tag.images]
# print('after removing.. ' , len(imageDescriptions) , 'image description(s) found: ' , imageDescriptions)

# print(audiofile.tag.images[0].__dict__.keys())
# print(audiofile.tag.images[0]._pic_type)

# print(audiofile.tag.images[1]._pic_type)
# print(artPic)

# print(edit_mp3())
