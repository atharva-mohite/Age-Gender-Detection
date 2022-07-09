import glob, os

# Specify the Current directory
dir_curr = os.path.dirname(os.path.abspath(__file__))

# Printing and verifying the Current directory
print(dir_curr)

dir_curr = 'data/obj'

# Percentage of images to be used for the test set are taken to be 10%
testPercent = 10;

# Creating train.txt and test.txt files
train_set= open('data/train.txt', 'w')
test_set = open('data/test.txt', 'w')

# Distributing the images/annotations into train.txt and test.txt files according to 
# testPercent specified

count = 1
test_indx = round(100 / testPercent)
for filenamepath in glob.iglob(os.path.join(dir_curr, "*.jpg")):

    title, ext = os.path.splitext(os.path.basename(filenamepath))

    if count == test_indx:
        count = 1
        test_set.write("data/obj" + "/" + title + '.jpg' + "\n")
    else:
        train_set.write("data/obj" + "/" + title + '.jpg' + "\n")
        count = count + 1

for filenamepath in glob.iglob(os.path.join(dir_curr, "*.png")):
    title, ext = os.path.splitext(os.path.basename(filenamepath))

    if count == test_indx:
        count = 1
        test_set.write("data/obj" + "/" + title + '.png' + "\n")
    else:
        train_set.write("data/obj" + "/" + title + '.png' + "\n")
        count = count + 1

# We have provided the support for “.jpg” and ".png" format images. If you have to process other image formats 
# like “.jpeg”, please uncomment the below code. 


# <---------------for .jpeg format images------------------------------>
# for filenamepath in glob.iglob(os.path.join(dir_curr, "*.jpeg")):
#     title, ext = os.path.splitext(os.path.basename(filenamepath))

#     if count == test_indx:
#         count = 1
#         test_set.write("data/obj" + "/" + title + '.jpeg' + "\n")
#     else:
#         train_set.write("data/obj" + "/" + title + '.jpeg' + "\n")
#         count = count + 1
