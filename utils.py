def get_image_dict(image):
    result = {
        'id': image.id,
        'title': image.title,
        'description': image.description,
        'url': image.image.url,
        'uploader': image.uploader,
        'upload_date': image.upload_date,
        'thumbnail': image.thumbnail
    }
    return result

def get_images_dict(images):
    result = []
    for image in images:
        result.append(get_image_dict(image))
    return result

