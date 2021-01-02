import torch
from torch.utils.data import Dataset,DataLoader
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms, utils
from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import math
from datetime import datetime

class ImageDataset(Dataset):
    def __init__(self,root_dir,path_list,transform=None):
        self.root_dir = root_dir
        self.path_list = path_list
        self.transform = transform

        self.data_len = len(path_list)

    def __len__(self):
        return self.data_len
    
    def  __getitem__(self,idx):
        img_name=self.path_list[idx]
        img = Image.open(img_name).convert('RGB')

        if self.transform is not None:
            img=self.transform(img)
        gt img

        lowres=img.filter(ImageFilter.GaussianBlur)
        downsample = transforms.Compose([
            transforms.Resize(64, Image.BICUBIC),
            transforms.Resize(128,Image.BICUBIC),
            transforms.ToTensor()
        ])
        lowres=downsample(lowres)

        gt= transforms.Compose([
            transforms.CenterCrop(128-8-2-4-1-1),
            transforms.ToTensor()
        ])(gt)

        return {'lowres': lowres, 'label':gt}

        def load_dataset(root_dir):
            root_dir=pathlib.Path(root_dir)
            img_paths = list(root_dir.glob('**/*.*'))
            img_paths=[str(path) for path in img_paths]

            transform-transforms.Compose([
                transforms.CenterCrop(400),
                transforms.RandomCrop(128)
            ])

            train_dataset=ImageDataset(root_dir,img_paths,transform)
            train_dataloader=DataLoader(train_dataset,batch_size=64,shuffle=True,num_workers=0)

            print(len(train_dataset), 'image paths imported from', root_dir)

        def load_testset(root_dir):
            root_dir=pathlib.Path(root_dir)
            img_paths= list(root_dir.glob('**/*.*'))
            img_paths= [str(path) for path in img_paths]

            transform = transforms.Compose([
                transforms.CenterCrop(128)
            ])

            test_dataset= ImageDataset(root_dir,img_paths, transform=transform)
            teste_dataloader = DataLoader(test_dataset,batch_size=len(test_dataset),shuffle=False,numworkers=0)
            print(len(test_dataset),'test image paths imported from', root_dir)

            return test_dataloader

            def train(dataloader,resume=False):
                device = torch.device('cuda')
                writer=SummaryWriter()

                n_epochs=1000
                loss_fn=torch.nn.MSELoss().to(device)
                learning_rate= 0.0001

                model = torch.nn.Sequential(
                    torch.nn.Conv2d(3,32,(9,9)),
                    torch.nn.ReLU(),

                    torch.nn.BatchNorm2d(32),

                    torch.nn.Conv2d(32,64,(3,3)),
                    torch.nn.ReLU(),

                    torch.nn.BatchNorm2d(64),

                    torch.nn.Conv2d(64,64,(1,1)),
                    torch.nn.ReLU(),

                    torch.nn.BatchNorm2d(64),

                    torch.nn.Conv2d(64,32,(3,3)),
                    torch.nn.ReLU(),

                    torch.nn.Conv2d(32,3,(5,5))
                )