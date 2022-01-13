import eyed3
from eyed3.id3.frames import ImageFrame

# source: https://eyed3.readthedocs.io/en/latest/modules.html
# https://stackoverflow.com/questions/38510694/how-to-add-album-art-to-mp3-file-using-python-3
# https://stackoverflow.com/questions/40515738/using-eyed3-to-embed-album-art-from-url
# https://id3.org/id3v2.3.0#Attached_picture

# Another package:
# https://mutagen.readthedocs.io/en/latest/

audiofile = eyed3.load("song.mp3")

if (audiofile.tag == None):
    audiofile.initTag()

# print(audiofile.tag.__dict__.keys())
# print(audiofile.tag)
print(len(audiofile.tag.images) , 'art picture(s) found')

audiofile.tag.artist = "שם האומן"
audiofile.tag.album = "שם האלבום"
audiofile.tag.album_artist = "שם אומן באלבום"
audiofile.tag.title = "שם השיר"
audiofile.tag.composer = 'מלחין'
audiofile.tag.track_num = 1
audiofile.tag.recording_date= '2019'
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
audiofile.tag.images.set(3, open('song2.jpg','rb').read(), 'image/jpeg',u'front')
# audiofile.tag.images.set(4, open('song.jpg','rb').read(), 'image/jpeg', u'back')
# audiofile.tag.images.set(5, open('song.jpg','rb').read(), 'image/jpeg', u'test1')
# audiofile.tag.images.set(6, open('song.jpg','rb').read(), 'image/jpeg', u'test2')
# print('after',audiofile.tag.images[0]._pic_type)




# Remove images
# remove a single image - in the brackets - the description of the image as set by the set command
# print(audiofile.tag._images.remove('back'), 'removed')

def removeImage(objMp3,desc):
    if(objMp3.tag._images.remove(desc)):
        return True
    else:
        return False

# remove all images
def removeAllImages(objMp3):
    toRemove = [x.description for x in objMp3.tag.images]
    counterRemoved = 0
    for desc in toRemove:
        if(objMp3.tag.images.remove(desc)):
            counterRemoved += 1
    return counterRemoved


# imageDescriptions = [x.description for x in audiofile.tag.images]
# print('before removing.. ' , len(imageDescriptions) , 'image description(s) found: ' , imageDescriptions)
# print(removeAllImages(audiofile), 'image(s) removed')
# imageDescriptions = [x.description for x in audiofile.tag.images]
# print('after removing.. ' , len(imageDescriptions) , 'image description(s) found: ' , imageDescriptions)

# print(audiofile.tag.images[0].__dict__.keys())
# print(audiofile.tag.images[0]._pic_type)

# print(audiofile.tag.images[1]._pic_type)
# print(artPic)

audiofile.tag.save()
