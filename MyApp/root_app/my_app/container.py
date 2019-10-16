import requests


## get the login form
class Container:
    def __init__(self, username, image, total_likes_of_profile, total_likes_of_cover_photo, User):
        self.username = username
        self.image = image
        self.total_likes_of_profile = total_likes_of_profile
        self.total_likes_of_cover_photo = total_likes_of_cover_photo
        self.User = User

    def getUsername(self):
        return self.username

    def getImage(self):
        return self.image

    def getTotalLikesOfProfile(self):
        return self.total_likes_of_profile

    def getTotalLikesOfCoverPhoto(self):
        return self.total_likes_of_cover_photo

    def getUser(self):
        return self.User


def get_json():
    url = 'https://api.unsplash.com/search/collections?page=1&query=nature&client_id=7764b913fbf8ea55e6b940cc2d0ad3daa59ca942c39aa857c1a4279e3f436910'
    username = []
    total_likes_of_profile = []
    total_likes_of_cover_photo = []
    start_loop = 0
    end_loop = 5

    User = list()
    user_data_for_javascript = list()
    try:
        response = requests.get(url)
        unsplash_data = response.json()
        for data_from_json in unsplash_data['results']:
            image_json = data_from_json['cover_photo']['urls']['regular']
            username_json = data_from_json['user']['username']
            total_likes_of_cover_photo_json = data_from_json['cover_photo']['likes']
            # create dictiorny to store image, username, lile images
            # to send the data to javascript
            userDict = {
                'image': image_json,
                'name': username_json,
                'likes': total_likes_of_cover_photo_json
            }
            ##apppedn the data as the list
            total_likes_of_profile.append(data_from_json['user']['total_likes'])
            total_likes_of_cover_photo.append(total_likes_of_cover_photo_json)
            username.append(username_json)
            ##append data to array as array of dictionary
            User.append(userDict.copy())
            print("The data from dictionary {0}".format(len(User)))
    except:
        status = "error"
    ## loop through data api responding from the Api
    # save to image , and username as lists.

    # pass data to after received from the Api to
    # the container
    return Container(username, image_json, total_likes_of_profile, total_likes_of_cover_photo, User)

