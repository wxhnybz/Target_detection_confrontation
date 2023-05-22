import os
import cv2
import PIL.Image as Image
import torch
import numpy as np
import torchvision.models as models
# import imagenet_stubs
# from imagenet_stubs.imagenet_2012_labels import name_to_label, label_to_name
# from art.estimators.classification import PyTorchClassifier
from matplotlib import pyplot as plt
from art.attacks.evasion import AdversarialPatch

target_label = 'toaster'
image_shape = (3, 224, 224)
clip_values = (0, 1)
nb_classes  =1000
batch_size = 16
scale_min = 0.4
scale_max = 0.6
rotation_max = 22.5
learning_rate = 0.005
max_iter = 1000
preprocessing = ([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])

def get_files_list(raw_dir):
    files_list = []
    for filepath,dirnames,filenames in os.walk(raw_dir):
        for filename in filenames:
            files_list.append(filepath+'/'+filename)
    return files_list

def predict_model(classifier, image, k=5):
    show_image = Image.fromarray((255*image.transpose(2,1,0)).astype(np.uint8))
    plt.imshow(show_image)
    plt.show()
    predicits = classifier.predict(image)
    indice = np.argmax(predicits)
    print(indice)
    name = label_to_name(indice)
    print(name)

def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("using {} device.".format(device))
    net = models.resnet50(pretrained=True)
    net.eval()

    classifier = PyTorchClassifier(
        model=net,
        clip_values=(0, 1),
        loss=None,
        preprocessing=preprocessing,
        input_shape=(3, 224, 224),
        nb_classes=1000,
    )

    images_list = list()

    for image_path in imagenet_stubs.get_image_paths():
        im = cv2.imread(image_path)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im = cv2.resize(im, (224, 224))
        im = [(im.T / 255).astype(np.float32)]
        images_list.append(im)

    images = np.vstack(images_list)
    target_name = 'toaster'
    label = name_to_label(target_name)
    print('target_label:{}-{}'.format(target_label, label))
    y_one_hot = np.zeros(1000)
    y_one_hot[label] = 1.0
    y_target = np.tile(y_one_hot, (images.shape[0], 1))

    attack = AdversarialPatch(classifier=classifier, rotation_max=rotation_max, scale_min=scale_min,
                              scale_max=scale_max,
                              learning_rate=learning_rate, max_iter=max_iter, batch_size=batch_size,
                              patch_shape=(3, 224, 224))
    patch, patch_mask = attack.generate(x=images, y=y_target)
    patched_images = attack.apply_patch(images, scale=0.5)

    predict_model(classifier, patched_images[0])

    print('Finished Training')



if __name__ == '__main__':
    main()
