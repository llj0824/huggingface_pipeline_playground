from transformers import pipeline;

# december 16, 2022 - pipeline playground
image_classifer = pipeline(task="image-classification")
def imageClassifier(imageUrl):
    return image_classifer(
        images=imageUrl
    )

def transform_scores(scores):
    return {score['label']: score['score'] for score in scores}

while True:
# Get User Argument
    user_input = input("please input url of an image: \n")
    print("Processing:" + user_input)

    # print response
    print(transform_scores(imageClassifier(user_input)))
    print("Do you have more to say?")

